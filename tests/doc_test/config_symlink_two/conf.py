import os

extensions = ["sphinx_collections"]

collections = {
    "my_files": {
        "driver": "symlink",
        "source": "../config_symlink_data",
        "target": "my_data/one",
    },
    "my_other_files": {
        "driver": "symlink",
        "source": "../config_symlink_data",
        "target": "my_data/two",
    },
}


test_dir = os.path.dirname(__file__)

project = "collections test docs"
master_doc = "index"

author = "team useblocks"
version = "1.0"
release = "1.0"

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
