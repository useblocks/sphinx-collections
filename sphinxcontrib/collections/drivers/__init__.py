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

        self._prefix = '  {}: ({}) '.format(self.collection, self.name)

        if config is None:
            config = {}
        self.config = config

    def run(self):
        raise NotImplementedError('run() function must be implemented by driver {} itself.'.format(self.name))

    def clean(self):
        raise NotImplementedError('clean() function must be implemented by driver {} itself.'.format(self.name))

    def error(self, message, e=None):
        """
        Raises exception, if driver is in safe mode.
        Otherwise just a log message gets printed.

        :param message: String
        :param e: Traceback object
        :return: None
        """
        if e is not None and isinstance(e, BaseException):
            if self.config['safe']:
                raise ColectionsDriverError('{}{}'.format(self._prefix, message)) from e
            self._log.error(('{}{} - {}'.format(self._prefix, message, e)))
        else:
            if self.config['safe']:
                raise ColectionsDriverError('{}{}'.format(self._prefix, message))
            self._log.error(('{}{}'.format(self._prefix, message)))

    def info(self, message):
        self._log.info('{}{}'.format(self._prefix, message))

    def debug(self, message):
        self._log.debug('{}{}'.format(self._prefix, message))


class ColectionsDriverError(BaseException):
    pass
