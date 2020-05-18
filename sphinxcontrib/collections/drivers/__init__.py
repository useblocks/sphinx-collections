import sphinx

from pkg_resources import parse_version

sphinx_version = sphinx.__version__
if parse_version(sphinx_version) >= parse_version("1.6"):
    from sphinx.util import logging
else:
    import logging

    logging.basicConfig()  # Only need to do this once


DRIVERS = {}


class Driver:

    def __init__(self, name, func=None, conf=None, active=True):
        self.log = logging.getLogger(__name__)
        self.name = name
        if func is None:
            func = self.run
        self.func = func

        if conf is None:
            conf = {}
        self.conf = conf
        self.active = active

        self._register()

    def _register(self):
        if self.name not in DRIVERS.keys():
            DRIVERS[self.name] = self

    def run(self, config):
        raise NotImplementedError('run() function must be implemented by driver {} itself.'.format(self.name))


class ColectionsDriverError(BaseException):
    pass
