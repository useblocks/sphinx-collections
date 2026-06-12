import os

extensions = ["sphinx_collections"]

collections = {
    "my_string": {
        "driver": "string",
        "source": "Hello report world",
        "target": "hello.txt",
        "active": True,
    },
    "my_report": {
        "driver": "report",
        "target": "report.rst",
        "active": True,
    },
}


test_dir = os.path.dirname(__file__)

project = "collections test docs"
master_doc = "index"

author = "team useblocks"
version = "1.0"
release = "1.0"

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
