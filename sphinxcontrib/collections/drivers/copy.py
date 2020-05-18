import os

from shutil import copytree, ignore_patterns

from sphinxcontrib.collections.drivers import Driver


class CopyDriver(Driver):

    def run(self, config):
        if not os.path.exists(config['source']):
            self.log.error('source does not exist')

        try:
            copytree(config['source'], config['target'], ignore_patterns(*config['ignore']), dirs_exist_ok=True)
        except IOError as e:
            self.log.error(e)



