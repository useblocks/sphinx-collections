import os

extensions = ["sphinx_collections"]

collections = {
    "jinja_test": {
        "driver": "jinja",
        "source": "templates/say_hello.rst.template",
        "target": "leaf/my_jinja_test_for_{{name|lower}}.rst",
        "data": [
            {"name": "Max", "city": "Munich"},
            {"name": "Sandra", "city": "Barcelone"},
        ],
        "multiple_files": True,
        "active": True,
    }
}


test_dir = os.path.dirname(__file__)

project = "collections test docs"
master_doc = "index"

author = "team useblocks"
version = "1.0"
release = "1.0"

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
