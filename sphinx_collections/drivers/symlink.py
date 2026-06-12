"""
symlink
=======

Creates a symlink (symbolic link) from ``target`` to ``source``.

``target`` must be a folder inside your documentation project.

Please note, config option  ``source`` is used as the name where the symlink shows to,
as this is our data source for additional sphinx files.
And ``target`` is the path where the symlink starts, because this defines the place
where the extra sphinx files shall be stored.

If executed on Windows 10, special privileges may be needed for creating symlinks.
Please see `os.symlink() <https://docs.python.org/3/library/os.html#os.symlink>`_
details for constraints.

This symlink driver can deal with links to folders and files.

.. code-block:: python

    collections = {
      'my_files': {
         'driver': 'symlink',
         'source': '../extra_files/',
         'target': 'my_data/'
      }
    }

Clean up behavior
-----------------
During clean up the symlink gets unlinked/removed.

"""

import os
import shutil

from sphinx_collections.drivers import Driver


class SymlinkDriver(Driver):
    def run(self):
        self.info("Creating symlink...")
        source = self.get_path(self.config["source"])
        target = self.get_path(self.config["target"]).rstrip(os.sep)
        self.create_target_dir(target)

        if not os.path.exists(source):
            self.error(f"Source {source} does not exist")
            return

        target_abspath = os.path.abspath(target)

        try:
            if os.path.exists(target_abspath):
                if os.path.islink(target):
                    self.info(f"Symlink already exists: {target_abspath}")
                else:
                    self.error(f"Existing target {target_abspath} is not a symlink")
            else:
                os.symlink(source, target)

        except FileExistsError:
            # due to paralell builds for different builders (html, pdf, needs,...)
            # symlinking seems to fail sometimes due to already existing link.
            self.info("Symlink seems to exist already, continue with normal processing.")
            if not os.path.islink(target):
                self.error(f"existing target {target_abspath} is no symlink")
        except OSError as e:
            self.error("Problems during creating of symlink.", e)

    def clean(self):
        target = self.get_path(self.config["target"]).rstrip(os.sep)
        try:
            if os.path.exists(os.path.abspath(target)):
                if not os.path.islink(target):
                    shutil.rmtree(target)
                else:
                    os.unlink(target)
                self.info(f"Symlink removed: {target}")
            else:
                self.info(f"Symlink already cleaned: {target}.")
        except FileNotFoundError:
            # Already cleaned? I'm okay with it.
            self.info(f"Symlink already cleaned: {target}.")
        except OSError as e:
            self.error("Problems during cleaning for collection {}".format(self.config["name"]), e)
