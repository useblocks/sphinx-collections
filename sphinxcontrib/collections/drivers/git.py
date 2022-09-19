"""
git
===

``git`` driver clones a given repository into a target folder.

URL must be given by ``source`` parameter.

.. code-block:: python

    collections = {
        'my_files': {
            'driver': 'git',
            'source': 'https://github.com/useblocks/sphinx_dummy.git',
        }
    }

``Sphinx-Collections`` will clone the given repository into ``_collections/my_files/``.

.. hint::

   ``Git`` binary must be installed on the system, so that the used Python library ``gitpython`` can use it.

Clean up behavior
-----------------
During clean up the local repository clone gets deleted.

"""


from shutil import rmtree

from git import Repo

from sphinxcontrib.collections.drivers import Driver


class GitDriver(Driver):
    def run(self):
        self.info("Cloning git repository...")

        try:
            Repo.clone_from(self.config["source"], self.config["target"])
        except Exception as e:
            self.error("Problems during cloning repository.", e)

    def clean(self):
        try:
            rmtree(self.config["target"])
            self.info("Repository deleted: {}".format(self.config["target"]))
        except FileNotFoundError:
            # Already cleaned? I'm okay with it.
            self.info("Cloned repository folder already cleaned.")
        except IOError as e:
            self.error("Problems during cleaning for collection {}".format(self.config["name"]), e)
