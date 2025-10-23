import os

from jinja2 import Template

from sphinxcontrib.collections.drivers import Driver


class ReportDriver(Driver):
    def run(self):
        from sphinxcontrib.collections.collections import COLLECTIONS

        self.info("Add collection report to file...")

        template_path = os.path.join(os.path.dirname(__file__), "report.rst.template")
        with open(template_path) as template_file:
            template = Template(template_file.read())
        result = template.render(collections=COLLECTIONS)
        try:
            with open(self.config["target"], "w") as target_file:
                target_file.write(result)
        except OSError as e:
            self.error("Problems during writing collection report to file", e)

    def clean(self):
        try:
            os.remove(self.config["target"])
            self.info("Collection report deleted: {}".format(self.config["target"]))
        except FileNotFoundError:
            pass  # Already cleaned? I'm okay with it.
        except OSError as e:
            self.error("Problems during cleaning for collection {}".format(self.config["name"]), e)
