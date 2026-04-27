extensions = ["sphinx_collections"]

collections = {
    "active_via_tag": {
        "driver": "string",
        "source": "Tag activated content",
        "target": "active_via_tag/file.txt",
        "active": False,
        "tags": ["enable_collection"],
        "final_clean": False,
    },
    "inactive_no_tag": {
        "driver": "string",
        "source": "Should not appear",
        "target": "inactive_no_tag/file.txt",
        "active": False,
        "tags": ["never_set_tag"],
        "final_clean": False,
    },
}

project = "collections tag test"
master_doc = "index"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
