import os

from shutil import copytree, ignore_patterns, rmtree

from sphinxcontrib.collections.drivers import Driver


class CopyDriver(Driver):

    def run(self):
        if not os.path.exists(self.config['source']):
            self.error('Source {} does not exist'.format(self.config['source']))
            return

        try:
            copytree(self.config['source'],
                     self.config['target'],
                     ignore_patterns(*self.config['ignore']))
        except IOError as e:
            self.error('Problems during copying files.', e)

    def clean(self):
        try:
            rmtree(self.config['target'])
            self.info('Folder deleted: {}'.format(self.config['target']))
        except IOError as e:
            self.error('Problems during cleaning for collection {}'.format(self.config['name']), e)
