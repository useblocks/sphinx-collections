from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "test_app",
    [{"buildername": "html", "srcdir": "doc_test/config_tags", "tags": ["enable_collection"]}],
    indirect=True,
)
def test_tag_activates_collection(test_app):
    app = test_app
    app.build()

    activated = Path(app.confdir, "_collections", "active_via_tag", "file.txt")
    assert activated.exists()
    assert activated.read_text() == "Tag activated content"

    inactive = Path(app.confdir, "_collections", "inactive_no_tag", "file.txt")
    assert not inactive.exists()


@pytest.mark.parametrize(
    "test_app",
    [{"buildername": "html", "srcdir": "doc_test/config_tags"}],
    indirect=True,
)
def test_no_tag_keeps_collection_inactive(test_app):
    app = test_app
    app.build()

    activated = Path(app.confdir, "_collections", "active_via_tag", "file.txt")
    inactive = Path(app.confdir, "_collections", "inactive_no_tag", "file.txt")
    assert not activated.exists()
    assert not inactive.exists()
