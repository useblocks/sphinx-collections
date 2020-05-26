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
      'my_files: {
         'driver': 'symlink',
         'source': '../extra_files/',
         'target': 'my_data/'
         }
      }
   }

Clean up behavior
-----------------
During clean up the symlink gets unlinked/removed.

"""

import os

from sphinxcontrib.collections.drivers import Driver


class SymlinkDriver(Driver):

    def run(self):
        self.info('Creating symlink...')
        source = self.get_path(self.config['source'])
        target = self.get_path(self.config['target'])

        if not os.path.exists(source):
            self.error('Source {} does not exist'.format(source))
            return

        try:
            os.symlink(source, target)
        except IOError as e:
            self.error('Problems during creating of symlink.', e)
        except OSError as e:
            self.error('Problems during creating of symlink. '
                       'Maybe unprivileged user if running on Windows 10.', e)

    def clean(self):
        source = self.get_path(self.config['source'])
        target = self.get_path(self.config['target'])
        try:
            os.unlink(target)
            self.info('Symlink removed: {}'.format(target))
        except FileNotFoundError:
            # Already cleaned? I'm okay with it.
            self.info('Symlink already cleaned: {}.'.format(target))
        except IOError as e:
            self.error('Problems during cleaning for collection {}'.format(self.config['name']), e)

