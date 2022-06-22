import os
from inspect import isfunction

from sphinxcontrib.collections.drivers import Driver


class FunctionDriver(Driver):
    def run(self):
        self.info("Run function...")

        if not isfunction(self.config["source"]):
            self.error("Source option must be a user-defined function. Nothing else.")
            return

        try:
            function = self.config["source"]
            result = function(self.config)
        except Exception as e:
            self.error("Problems during executing function", e)

        write_result = self.config.get("write_result", True)
        if write_result and result is not None:
            try:
                with open(self.config["target"], "w") as target_file:
                    target_file.writelines(result.split("\n"))
            except IOError as e:
                self.error("Problems during writing function result to file", e)

    def clean(self):
        try:
            os.remove(self.config["target"])
            self.info("File deleted: {}".format(self.config["target"]))
        except FileNotFoundError:
            pass  # Already cleaned? I'm okay with it.
        except IOError as e:
            self.error("Problems during cleaning for collection {}".format(self.config["name"]), e)
