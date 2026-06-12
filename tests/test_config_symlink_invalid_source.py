import shutil

import pytest

from sphinx_collections.drivers import CollectionsDriverError
from tests.conftest import copy_srcdir_to_tmpdir


def test_config_symlink_invalid_source(make_app, sphinx_test_tempdir):
    srcdir = copy_srcdir_to_tmpdir("doc_test/config_symlink_invalid_source", sphinx_test_tempdir)

    try:
        with pytest.raises(CollectionsDriverError):
            make_app(buildername="html", srcdir=srcdir)
    finally:
        # Ensure copied test source is removed like other tests
        shutil.rmtree(sphinx_test_tempdir, ignore_errors=True)
