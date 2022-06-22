from io import StringIO

# from xml.etree import ElementTree

NS = {"html": "http://www.w3.org/1999/xhtml"}


class HtmlCollections:
    """Helper class to parse HTML collections"""

    def __init__(self, collections):
        self.collections = collections
