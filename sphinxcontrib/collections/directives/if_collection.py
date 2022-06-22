import sphinx
from docutils import nodes
from docutils.parsers.rst import Directive, directives
from docutils.statemachine import ViewList
from pkg_resources import parse_version
from sphinx.util.nodes import nested_parse_with_titles

import sphinxcontrib.collections.collections

sphinx_version = sphinx.__version__
if parse_version(sphinx_version) >= parse_version("1.6"):
    from sphinx.util import logging
else:
    import logging
logger = logging.getLogger(__name__)


class CollectionsIf(nodes.General, nodes.Element):
    pass


class CollectionsIfDirective(Directive):
    """
    Directive to add content based on executed collections.
    """

    has_content = True
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {}

    def __init__(self, *args, **kw):
        super(CollectionsIfDirective, self).__init__(*args, **kw)
        self.log = logging.getLogger(__name__)

    @property
    def docname(self):
        return self.state.document.settings.env.docname

    @property
    def env(self):
        return self.state.document.settings.env

    def run(self):
        collections = sphinxcontrib.collections.collections.COLLECTIONS
        search_cols = [x.strip() for x in self.arguments[0].split(",")]

        found = False
        for search_col in search_cols:
            if search_col == "":
                continue

            for collection in collections:
                if collection.name.upper() == search_col.upper() and collection.executed:
                    found = True
                    break

            if found:
                break

        collection_node = nodes.container()
        if found:
            rst = ViewList()
            for line in self.content:
                rst.append(line, self.docname, self.lineno)
            node_collection_content = nodes.Element()
            node_collection_content.document = self.state.document
            nested_parse_with_titles(self.state, rst, node_collection_content)
            collection_node += node_collection_content.children

        return [collection_node]
