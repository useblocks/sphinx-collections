import os

extensions = ["sphinx_collections"]

collections = {
    "my_repo": {"driver": "git", "source": "https://github.com/useblocks/sphinx_dummy.git", "target": "mydata/"}
}


test_dir = os.path.dirname(__file__)

project = "collections test docs"
master_doc = "index"

author = "team useblocks"
version = "1.0"
release = "1.0"

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
