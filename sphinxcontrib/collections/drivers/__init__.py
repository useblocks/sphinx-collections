import os

from sphinx.util import logging


class Driver:
    def __init__(self, collection, config=None):
        self._log = logging.getLogger(__name__)
        self.name = self.__class__.__name__
        self.collection = collection

        self._prefix = f"  {self.collection}: ({self.name}) "

        if config is None:
            config = {}
        self.config = config

    def run(self):
        """
        This is the main routine for the driver.

        The run method must be implement by the subclassed driver.
        """
        raise NotImplementedError(f"run() function must be implemented by the driver {self.name} itself.")

    def clean(self):
        """
        Cares about cleaning up the working space from actions performed in run().

        Gets called normally at the beginning and add the end of collection handling.

        Must be implement by the parent driver class.
        """
        raise NotImplementedError(f"clean() function must be implemented by driver {self.name} itself.")

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
                raise ColectionsDriverError(f"{self._prefix}{message}") from e
            self._log.error(f"{self._prefix}{message} - {e}")
        else:
            if self.config["safe"]:
                raise ColectionsDriverError(f"{self._prefix}{message}")
            self._log.error(f"{self._prefix}{message}")

    def info(self, message):
        """
        Writes a log message of level INFO.

        Prefixes collection information and driver name in front of the message.

        :param message: string
        :return: None
        """
        self._log.info(f"{self._prefix}{message}")

    def debug(self, message):
        """
        Writes a log message of level DEBUG.

        Sets collection and driver information as prefix in front of the message

        :param message: string
        :return: None
        """
        self._log.debug(f"{self._prefix}{message}")

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
