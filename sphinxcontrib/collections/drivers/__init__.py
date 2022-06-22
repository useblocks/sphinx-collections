import os

import sphinx
from pkg_resources import parse_version

sphinx_version = sphinx.__version__
if parse_version(sphinx_version) >= parse_version("1.6"):
    from sphinx.util import logging
else:
    import logging

    logging.basicConfig()  # Only need to do this once


class Driver:
    def __init__(self, collection, config=None):
        self._log = logging.getLogger(__name__)
        self.name = self.__class__.__name__
        self.collection = collection

        self._prefix = "  {}: ({}) ".format(self.collection, self.name)

        if config is None:
            config = {}
        self.config = config

    def run(self):
        """
        Is the main routine for the driver.

        Must be implement by the parent driver class.
        """
        raise NotImplementedError("run() function must be implemented by driver {} itself.".format(self.name))

    def clean(self):
        """
        Cares about cleaning up the working space from actions performed in run().

        Gets called normally at the beginning and add the end of collection handling.

        Must be implement by the parent driver class.
        """
        raise NotImplementedError("clean() function must be implemented by driver {} itself.".format(self.name))

    def error(self, message, e=None):
        """
        Raises exception, if driver is in safe mode.
        Otherwise just a log message gets printed.

        :param message: String
        :param e: Traceback object
        :return: None
        """
        if e is not None and isinstance(e, BaseException):
            if self.config["safe"]:
                raise ColectionsDriverError("{}{}".format(self._prefix, message)) from e
            self._log.error(("{}{} - {}".format(self._prefix, message, e)))
        else:
            if self.config["safe"]:
                raise ColectionsDriverError("{}{}".format(self._prefix, message))
            self._log.error(("{}{}".format(self._prefix, message)))

    def info(self, message):
        """
        Writes a log message of level INFO.

        Sets collection and driver information as prefix in front of the message

        :param message: string
        :return: None
        """
        self._log.info("{}{}".format(self._prefix, message))

    def debug(self, message):
        """
        Writes a log message of level DEBUG.

        Sets collection and driver information as prefix in front of the message

        :param message: string
        :return: None
        """
        self._log.debug("{}{}".format(self._prefix, message))

    def get_source_path(self):
        """
        Returns absolute source path.
        If source was configured as relative path, the absolute path is calculated
        taking documentation confdir as base folder.

        :return: path string
        """
        source = self.config.get("source", None)
        if source is None:
            self.error("Source must be defined")
        if not os.path.isabs(source):
            source = os.path.join(self.config["confdir"], source)
        return source

    def get_path(self, path):
        """
        Returns absolute path.
        If path is given as relative path, the absolute path is calculated
        taking documentation confdir as base folder.

        :return: path string
        """
        if path is None:
            self.error("Path must be defined")
        if not isinstance(path, str):
            self.debug("This functions makes mostly sense for string source only.")
            return path
        if not os.path.isabs(path):
            path = os.path.join(self.config["confdir"], path)
        return path


class ColectionsDriverError(BaseException):
    pass
