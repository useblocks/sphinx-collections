"""Pytest conftest module containing common test configuration and fixtures."""

from pathlib import Path
import shutil

import pytest

from sphinx_collections import collections as _collections_module

pytest_plugins = "sphinx.testing.fixtures"


@pytest.fixture(autouse=True)
def _reset_collections_registry():
    # Why: COLLECTIONS is a module-level list mutated by config-inited handlers,
    # so it leaks between tests sharing an xdist worker.
    _collections_module.COLLECTIONS.clear()
    yield
    _collections_module.COLLECTIONS.clear()


def copy_srcdir_to_tmpdir(srcdir, tmp):
    srcdir = Path(__file__).parent.resolve() / srcdir
    tmproot = Path(tmp) / Path(srcdir).name
    shutil.copytree(srcdir, tmproot)
    return tmproot


@pytest.fixture(scope="function")
def test_app(make_app, sphinx_test_tempdir, request):
    # get builder parameters from test case
    builder_params = request.param

    # copy test srcdir to test temporary directory sphinx_test_tempdir
    srcdir = builder_params.get("srcdir", None)
    src_dir = copy_srcdir_to_tmpdir(srcdir, sphinx_test_tempdir)

    # copy external test dir to test temporary directory sphinx_test_tempdir
    external_data_dir = builder_params.get("datadir", None)
    if external_data_dir is not None:
        copy_srcdir_to_tmpdir(external_data_dir, sphinx_test_tempdir)

    # return sphinx.testing fixture make_app and new srcdir which in sphinx_test_tempdir
    app = make_app(
        buildername=builder_params.get("buildername", "html"),
        srcdir=src_dir,
        # builddir=builder_params.get("builddir", None),  # sphinx 3.5.4 not compatible
        freshenv=builder_params.get("freshenv", None),
        confoverrides=builder_params.get("confoverrides", None),
        status=builder_params.get("status", None),
        warning=builder_params.get("warning", None),
        tags=builder_params.get("tags", None),
        docutilsconf=builder_params.get("docutilsconf", None),
        parallel=builder_params.get("parallel", 0),
    )

    try:
        yield app
    finally:
        # cleanup test temporary directory
        shutil.rmtree(sphinx_test_tempdir, True)
