import os
import sphinx

from pkg_resources import parse_version

from sphinxcontrib.collections.drivers.copy import CopyDriver

sphinx_version = sphinx.__version__
if parse_version(sphinx_version) >= parse_version("1.6"):
    from sphinx.util import logging
else:
    import logging

    logging.basicConfig()  # Only need to do this once


LOG = logging.getLogger(__name__)
VERSION = 0.1
COLLECTIONS = []

DRIVERS = {
    'copy': CopyDriver
}


def setup(app):

    # Registers config options
    app.add_config_value('collections', {}, 'html')
    app.add_config_value('collections_target', '_collections', 'html')
    app.add_config_value('collections_clean', True, 'html')
    app.add_config_value('collections_final_clean', True, 'html')

    # Connects handles to events
    app.connect('config-inited', collect_collections)
    app.connect('config-inited', clean_collections)
    app.connect('config-inited', execute_collections)
    app.connect('build-finished', final_clean_collections)

    return {'version': VERSION,
            'parallel_read_safe': False,
            'parallel_write_safe': True}


def collect_collections(app, config):
    LOG.info('Read in collections ...')
    for name, collection in config.collections.items():
        COLLECTIONS.append(Collection(app, name, **collection))


def clean_collections(app, config):
    if not bool(app.config['collections_clean']):
        return

    LOG.info('Clean collections ...')
    for collection in COLLECTIONS:
        collection.clean()


def execute_collections(app, config):
    LOG.info('Executing collections ...')
    for collection in COLLECTIONS:
        try:
            collection.run()
        except Exception as e:
            LOG.error('Error executing driver {} for collection {}. {}'.format(collection.driver.name,
                                                                               collection.name, e))


def final_clean_collections(app, exception):
    if not bool(app.config['collections_final_clean']):
        return

    LOG.info('Final clean of collections ...')
    for collection in COLLECTIONS:
        collection.final_clean()


class Collection:
    def __init__(self, app, name, **kwargs):
        self.app = app
        self.name = name
        self._log = LOG

        self.active = bool(kwargs.get('active', True))

        self._prefix = '  {}: '.format(self.name)

        target = kwargs.get('target', None)
        if target is None:
            target = self.name
        if not os.path.isabs(target):
            target = os.path.join(app.confdir, app.config['collections_target'], target)

        clean = bool(kwargs.get('clean', True))
        if clean is None:
            clean = app.config['collections_clean']
        self.needs_clean = clean

        final_clean = bool(kwargs.get('final_clean', True))
        if final_clean is None:
            final_clean = app.config['collections_final_clean']
        self.needs_final_clean = final_clean

        # Check if we manipulate data only in documentation folder.
        # Any other location is not allowed.
        if not os.path.realpath(target).startswith(os.path.realpath(app.confdir)):
            raise CollectionsException(
                'Target path is not part of documentation folder\n'
                'Target path: {}\n'
                'Sphinx app conf path: {}'.format(os.path.realpath(target),
                                                  os.path.realpath(app.confdir)))

        self.target = target

        if not os.path.exists(target):
            os.makedirs(target, exist_ok=True)

        self.result = None

        self.config = kwargs
        self.config['name'] = self.name
        self.config['target'] = target
        if 'safe' not in self.config.keys():
            self.config['safe'] = True

        driver_name = kwargs.get('driver', None)
        if driver_name is None or driver_name not in DRIVERS.keys():
            raise Exception('Unknown driver: {}'.format(driver_name))
        self.driver = DRIVERS[kwargs['driver']](self.name, self.config)

        self.info('Initialised')

    def run(self):
        if self.active:
            self.info('Execution started')
            self.result = self.driver.run()
            self.info('Execution done')
        else:
            self.info('Not active. No execution')

    def clean(self):
        if self.needs_clean and self.active:
            self.info('Cleaning...')
            self.driver.clean()

    def final_clean(self):
        if self.needs_final_clean and self.active:
            self.info('Final Cleaning...')
            self.driver.clean()

    def info(self, message):
        self._log.info('{}{}'.format(self._prefix, message))

    def warn(self, message):
        self._log.warn('{}{}'.format(self._prefix, message))

    def error(self, message):
        if self.config['safe']:
            raise CollectionsException('{}{}'.format(self._prefix, message))
        self._log.info('{}{}'.format(self._prefix, message))


class CollectionsException(BaseException):
    pass
