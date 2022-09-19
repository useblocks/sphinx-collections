from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "test_app",
    [{"buildername": "html", "srcdir": "doc_test/config_symlink", "datadir": "doc_test/config_symlink_data"}],
    indirect=True,
)
def test_config_symlink(test_app):
    app = test_app
    app.build()
    html = Path(app.outdir, "index.html").read_text()

    assert '<link rel="next" title="Awesome" href="_collections/my_data/awesome.html" />' in html

    html = Path(app.outdir, "_collections/my_data/awesome.html").read_text()

    assert "Awesome, this is nice" in html
