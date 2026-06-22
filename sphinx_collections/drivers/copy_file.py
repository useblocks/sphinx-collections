import os
from shutil import copy2

from sphinx_collections.drivers import Driver


class CopyFileDriver(Driver):
    def run(self):
        self.info("Copy file...")

        source = self.config["source"] if os.path.exists(self.config["source"]) else self.get_source_path()

        if not os.path.exists(source):
            self.error(f"Source {source} does not exist")
            return

        target = self.config["target"]
        self.create_target_dir(target)

        try:
            self.info(f"cp {source} {target}")
            copy2(source, target)
        except Exception as e:
            self.error(f"copy file from {source} to {target} failed: {e}")

    def clean(self):
        try:
            os.remove(self.config["target"])
            self.info("File deleted: {}".format(self.config["target"]))
        except FileNotFoundError:
            pass  # Already cleaned? I'm okay with it.
        except OSError as e:
            self.error("Problems during cleaning for collection {}".format(self.config["name"]), e)
