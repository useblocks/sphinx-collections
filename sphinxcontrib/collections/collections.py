import os

import sphinx
from pkg_resources import parse_version

from sphinxcontrib.collections.drivers.copy_file import CopyFileDriver
from sphinxcontrib.collections.drivers.copy_folder import CopyFolderDriver
from sphinxcontrib.collections.drivers.function import FunctionDriver
from sphinxcontrib.collections.drivers.git import GitDriver
from sphinxcontrib.collections.drivers.jinja import JinjaDriver
from sphinxcontrib.collections.drivers.report import ReportDriver
from sphinxcontrib.collections.drivers.string import StringDriver
from sphinxcontrib.collections.drivers.symlink import SymlinkDriver

sphinx_version = sphinx.__version__
if parse_version(sphinx_version) >= parse_version("1.6"):
    from sphinx.util import logging
else:
    import logging

    logging.basicConfig()  # Only need to do this once

LOG = logging.getLogger(__name__)
COLLECTIONS = []

DRIVERS = {
    "copy_folder": CopyFolderDriver,
    "copy_file": CopyFileDriver,
    "string": StringDriver,
    "function": FunctionDriver,
    "report": ReportDriver,
    "symlink": SymlinkDriver,
    "jinja": JinjaDriver,
    "git": GitDriver,
}


def collect_collections(app, config):
    LOG.info("Read in collections ...")
    for name, collection in config.collections.items():
        COLLECTIONS.append(Collection(app, name, **collection))


def clean_collections(app, config):
    LOG.info("Clean collections ...")
    for collection in COLLECTIONS:
        collection.clean()


def execute_collections(app, config):
    LOG.info("Executing collections ...")
    for collection in COLLECTIONS:
        try:
            collection.run()
        except Exception as e:
            LOG.error(
                "Error executing driver {} for collection {}. {}".format(collection.driver.name, collection.name, e)
            )


def final_clean_collections(app, exception):
    LOG.info("Final clean of collections ...")
    for collection in COLLECTIONS:
        collection.final_clean()


class Collection:
    def __init__(self, app, name, **kwargs):
        self.app = app
        self.name = name
        self.executed = False
        self._log = LOG

        self.active = bool(kwargs.get("active", True))
        tags = kwargs.get("tags", [])

        # Check if tags are set and change active to True if this is the case
        self.tags = tags
        for tag in tags:
            if tag in self.app.tags.tags.keys() and self.app.tags.tags[tag]:
                self.active = True

        self._prefix = "  {}: ".format(self.name)

        collection_main_folder = os.path.join(app.confdir, app.config["collections_target"])

        target = kwargs.get("target", None)
        if target is None:
            target = self.name
        if not os.path.isabs(target):
            if not os.path.exists(collection_main_folder):
                os.makedirs(collection_main_folder, exist_ok=True)
            target = os.path.join(collection_main_folder, target)

        if not os.path.exists(os.path.dirname(target)):
            os.makedirs(os.path.dirname(target), exist_ok=True)

        self.target = target

        clean = kwargs.get("clean", None)
        if clean is None:
            clean = app.config["collections_clean"]
        self.needs_clean = clean

        final_clean = kwargs.get("final_clean", None)
        if final_clean is None:
            final_clean = app.config["collections_final_clean"]
        self.needs_final_clean = final_clean

        self.config = kwargs
        self.config["name"] = self.name
        self.config["confdir"] = self.app.confdir
        self.config["target"] = target
        if "safe" not in self.config.keys():
            self.config["safe"] = True

        # Driver init
        driver_name = kwargs.get("driver", None)
        if driver_name is None or driver_name not in DRIVERS.keys():
            raise Exception("Unknown driver: {}".format(driver_name))
        self.driver = DRIVERS[kwargs["driver"]](self.name, self.config)

        # Check if we manipulate data only in documentation folder.
        # Any other location is not allowed.
        target_inside_confdir = (
            os.path.abspath(target).startswith(os.path.abspath(app.confdir))
            if driver_name == "symlink"
            else os.path.realpath(target).startswith(os.path.realpath(app.confdir))
        )

        if not target_inside_confdir:
            raise CollectionsException(
                "Target path is not part of documentation folder\n"
                "Target path abs: {}\n"
                "Target path: {}\n"
                "Sphinx app conf path: {}\n".format(
                    os.path.abspath(target), os.path.realpath(target), os.path.realpath(app.confdir)
                )
            )

        self.result = None

        self.info("Initialised")

    def __repr__(self):
        return self.name

    def run(self):
        if self.active:
            self.result = self.driver.run()

            self.executed = True

    def clean(self):
        if self.needs_clean and self.active:
            self.driver.clean()

    def final_clean(self):
        if self.needs_final_clean and self.active:
            self.driver.clean()

    def info(self, message):
        self._log.info("{}{}".format(self._prefix, message))

    def warn(self, message):
        self._log.warn("{}{}".format(self._prefix, message))

    def error(self, message):
        if self.config["safe"]:
            raise CollectionsException("{}{}".format(self._prefix, message))
        self._log.info("{}{}".format(self._prefix, message))


class CollectionsException(BaseException):
    pass
