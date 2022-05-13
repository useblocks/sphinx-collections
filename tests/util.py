from io import StringIO
#from xml.etree import ElementTree

NS = {"html": "http://www.w3.org/1999/xhtml"}


class HtmlNeed:
    """Helper class to parse HTML needs"""

    def __init__(self, need):
        self.need = need

    @property
    def id(self):
        found_id = self.need.find(".//html:a[@class='reference internal']", NS)
        if found_id is None:
            found_id = self.need.find(".//html:a[@class='reference internal']", {"html": ""})
        return found_id.text

    @property
    def title(self):
        found_title = self.need.find(".//html:span[@class='needs_title']", NS)
        if found_title is None:
            found_title = self.need.find(".//html:span[@class='needs_title']", {"html": ""})
        return found_title[0].text if found_title else None  # title[0] aims to the span_data element
