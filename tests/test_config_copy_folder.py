from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "test_app",
    [{"buildername": "html", "srcdir": "doc_test/config_copy_folder", "datadir": "doc_test/config_copy_folder_data"}],
    indirect=True,
)
def test_config_string(test_app):
    app = test_app
    app.build()
    html = Path(app.outdir, "index.html").read_text()

    assert "This is a include example for copy_folder" in html
    assert "Second include example for copy_folder" in html
    assert "This should not bee included cause not copied" not in html
