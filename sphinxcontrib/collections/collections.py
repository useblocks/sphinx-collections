import os
import sphinx

from pkg_resources import parse_version

from sphinxcontrib.collections.drivers.copy import CopyDriver
from sphinxcontrib.collections.drivers import DRIVERS


sphinx_version = sphinx.__version__
if parse_version(sphinx_version) >= parse_version("1.6"):
    from sphinx.util import logging
else:
    import logging

    logging.basicConfig()  # Only need to do this once


LOG = logging.getLogger(__name__)
VERSION = 0.1
COLLECTIONS = []


def setup(app):

    # Initiates all needed Drivers for sphinx-collections
    CopyDriver('copy')

    # Registers config options
    app.add_config_value('collections', {}, 'html')

    # Connects handles to events
    app.connect('config-inited', process_collections)
    app.connect('config-inited', execute_collections)

    return {'version': VERSION,
            'parallel_read_safe': False,
            'parallel_write_safe': True}


def process_collections(app, config):
    LOG.info('Read in collections ...')
    for name, collection in config.collections.items():
        COLLECTIONS.append(Collection(app, name, **collection))
        LOG.info('Collection {} read in.'.format(name))


def execute_collections(app, config):
    LOG.info('Executing collections ...')
    for collection in COLLECTIONS:
        try:
            LOG.info('Executing {} ... '.format(collection.name))
            collection.run()
        except Exception as e:
            LOG.error('Error executing driver {} for collection {}. {}'.format(collection.driver.name,
                                                                               collection.name, e))
        LOG.info('  done.')


class Collection:
    def __init__(self, app, name, **kwargs):
        self.app = app
        self.name = name

        driver_name = kwargs.get('driver', None)
        if driver_name is None or driver_name not in DRIVERS.keys():
            raise Exception('Unknown driver: {}'.format(driver_name))
        self.driver = DRIVERS[kwargs['driver']]
        self.active = bool(kwargs.get('active', True))

        target = kwargs.get('target', None)
        if target is None:
            target = os.path.join('_collections', self.name)
        if not os.path.isabs(target):
            target = os.path.join(app.confdir, target)
        self.target = target

        if not os.path.exists(target):
            os.makedirs(target, exist_ok=True)

        self.result = None

        self.conf = kwargs
        self.conf['target'] = target

    def run(self):
        self.result = self.driver.run(self.conf)
