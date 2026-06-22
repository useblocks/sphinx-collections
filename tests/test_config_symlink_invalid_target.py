from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "test_app",
    [
        {
            "buildername": "html",
            "srcdir": "doc_test/config_symlink_invalid_target",
            "datadir": "doc_test/config_symlink_data",
            "confoverrides": {"collections_final_clean": False},
        }
    ],
    indirect=True,
)
def test_config_symlink_invalid_target(test_app):
    app = test_app
    app.build()
    html = Path(app.outdir, "index.html").read_text()

    assert "TEST COLLECTIONS SYMLINK DRIVER INVALID TARGET" in html

    assert '<link rel="next" title="Awesome" href="_collections/my_data/awesome.html" />' not in html
    assert "placeholder.txt" not in html

    target = Path(app.confdir, "_collections/my_data")
    assert target.is_symlink()
