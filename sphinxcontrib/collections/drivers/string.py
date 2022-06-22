import os

from sphinxcontrib.collections.drivers import Driver


class StringDriver(Driver):
    def run(self):
        self.info("Add string to file...")

        if not isinstance(self.config["source"], str):
            self.error("Source option must be a string. Nothing else.")
            return

        try:
            with open(self.config["target"], "w") as target_file:
                target_file.writelines(self.config["source"].split("\n"))
        except IOError as e:
            self.error("Problems during writing string to file", e)

    def clean(self):
        try:
            os.remove(self.config["target"])
            self.info("File deleted: {}".format(self.config["target"]))
        except FileNotFoundError:
            pass  # Already cleaned? I'm okay with it.
        except IOError as e:
            self.error("Problems during cleaning for collection {}".format(self.config["name"]), e)
