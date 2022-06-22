import os
from shutil import copyfile

from sphinxcontrib.collections.drivers import Driver


class CopyFileDriver(Driver):
    def run(self):
        self.info("Copy file...")

        if not os.path.exists(self.config["source"]):
            self.error("Source {} does not exist".format(self.config["source"]))
            return

        try:
            copyfile(self.config["source"], self.config["target"])
        except IOError as e:
            self.error("Problems during copying file.", e)

    def clean(self):
        try:
            os.remove(self.config["target"])
            self.info("File deleted: {}".format(self.config["target"]))
        except FileNotFoundError:
            pass  # Already cleaned? I'm okay with it.
        except IOError as e:
            self.error("Problems during cleaning for collection {}".format(self.config["name"]), e)
