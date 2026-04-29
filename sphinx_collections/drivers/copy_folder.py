import os
from shutil import copytree, ignore_patterns, rmtree

from sphinx_collections.drivers import Driver


class CopyFolderDriver(Driver):
    def run(self):
        self.info("Copy folder...")

        source = self.config["source"] if os.path.exists(self.config["source"]) else self.get_source_path()

        if not os.path.exists(source):
            self.error(f"Source {source} does not exist")
            return

        try:
            target = self.config["target"]
            copytree(source, target, ignore=ignore_patterns(*self.config.get("ignore", [])))
        except OSError as e:
            self.error("Problems during copying folder.", e)

    def clean(self):
        try:
            rmtree(self.config["target"])
            self.info("Folder deleted: {}".format(self.config["target"]))
        except FileNotFoundError:
            pass  # Already cleaned? I'm okay with it.
        except OSError as e:
            self.error("Problems during cleaning for collection {}".format(self.config["name"]), e)
