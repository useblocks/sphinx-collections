# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import datetime

from sphinx_collections.api import register_driver
from sphinx_collections.drivers import Driver

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = "sphinx-collections"
copyright = f"{datetime.datetime.now().year}, team useblocks"
author = "team useblocks"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx_collections",
    "sphinx.ext.extlinks",
]

suppress_warnings = ["config.cache"]
"""Required due to my_func being not picklable for cache."""


def my_func(config):
    string = "This data gets written into {}".format(config["target"])
    return string


class MyDriver(Driver):
    def run(self):
        self.info("Run for source {}".format(self.config["source"]))

    def clean(self):
        self.info("Clean")


register_driver("my_driver", MyDriver)


collections = {
    "driver_test": {
        "driver": "my_driver",
        "source": "../tests/dummy/",
        "active": False,
    },
    "copy_folder_test": {
        "driver": "copy_folder",
        "source": "../tests/dummy/",
        "ignore": ["*.dat"],
        "active": False,
    },
    "copy_file_test": {
        "driver": "copy_file",
        "source": "../tests/dummy/dummy.rst",
        "target": "dummy_new.rst",
        "active": False,
    },
    "string_test": {
        "driver": "string",
        "source": "Take **this**!!!",
        "target": "dummy_string.rst",
        "active": False,
    },
    "function_test": {
        "driver": "function",
        "source": my_func,
        "target": "dummy_function.rst",
        "active": False,
    },
    "report": {
        "driver": "report",
        "target": "doc_collection_report.rst",
        "active": True,
    },
    "symlink_test": {
        "driver": "symlink",
        "source": "../tests/dummy/",
        "active": False,
    },
    "jinja_test": {
        "driver": "jinja",
        "source": "examples/jinja_template.rst.temp",
        "target": "my_jinja_test_{{name}}.rst",
        "data": {"name": "me", "city": "munich"},
        "active": False,
    },
    "jinja_test_multiple": {
        "driver": "jinja",
        "source": "examples/jinja_template.rst.temp",
        "target": "my_jinja_test_{{name|lower}}.rst",
        "multiple_files": True,
        "data": [
            {"name": "Marco", "city": "Munich"},
            {"name": "Daniel", "city": "Soest"},
        ],
        "active": False,
    },
    "git_test": {
        "driver": "git",
        "source": "https://github.com/useblocks/sphinx_dummy.git",
        "active": False,
    },
}

collections_final_clean = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "alabaster"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_sidebars = {
    "**": ["about.html", "navigation.html", "searchbox.html"],
}

html_theme_options = {
    "logo": "sphinx_collections_logo.png",
    "logo_name": False,
    # 'description': "an extension for sphinx",
    "logo_text_align": "center",
    "github_user": "useblocks",
    "github_repo": "sphinx-collections",
    "github_banner": True,
    "github_button": True,
    "github_type": "star",
    "fixed_sidebar": True,
    "extra_nav_links": {
        "collections@PyPi": "https://pypi.python.org/pypi/sphinx-collections/",
        "collections@github": "https://github.com/useblocks/sphinx-collections",
    },
}

extlinks = {
    "pr": ("https://github.com/useblocks/sphinx-collections/pull/%s", "PR #%s"),
    "issue": (
        "https://github.com/useblocks/sphinx-collections/issues/%s",
        "issue #%s",
    ),
}
