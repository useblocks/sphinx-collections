from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "test_app",
    [
        {
            "buildername": "html",
            "srcdir": "doc_test/config_symlink_with_dir",
            "datadir": "doc_test/config_symlink_data",
        }
    ],
    indirect=True,
)
def test_config_symlink_with_dir(test_app):
    app = test_app
    app.build()
    html = Path(app.outdir, "index.html").read_text()

    assert '<link rel="next" title="Awesome" href="_collections/leaf/my_data/awesome.html" />' in html

    html = Path(app.outdir, "_collections/leaf/my_data/awesome.html").read_text()

    assert "Awesome, this is nice" in html
