import sphinx

from pkg_resources import parse_version

from sphinxcontrib.collections.directives.if_collection import CollectionsIf, CollectionsIfDirective

from sphinxcontrib.collections.collections import collect_collections, clean_collections, \
    execute_collections, final_clean_collections

sphinx_version = sphinx.__version__
if parse_version(sphinx_version) >= parse_version("1.6"):
    from sphinx.util import logging
else:
    import logging

    logging.basicConfig()  # Only need to do this once

LOG = logging.getLogger(__name__)
VERSION = 0.1


def setup(app):
    """
    Configures Sphinx

    Registers:

    * config values
    * receivers for events
    * directives
    """

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

    app.add_node(CollectionsIf)
    app.add_directive('if-collection', CollectionsIfDirective)
    app.add_directive('ifc', CollectionsIfDirective)

    return {'version': VERSION,
            'parallel_read_safe': True,
            'parallel_write_safe': True}
