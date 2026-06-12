from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "test_app",
    [
        {
            "buildername": "html",
            "srcdir": "doc_test/config_symlink_two",
            "datadir": "doc_test/config_symlink_data",
            "confoverrides": {"collections_final_clean": False},
        }
    ],
    indirect=True,
)
def test_config_symlink_two_targets(test_app):
    app = test_app
    app.build()

    html = Path(app.outdir, "index.html").read_text()
    assert '<link rel="next" title="Awesome" href="_collections/my_data/one/awesome.html" />' in html

    base_dir = Path(app.confdir, "_collections", "my_data")
    assert base_dir.exists()

    symlink_one = base_dir / "one"
    symlink_two = base_dir / "two"
    assert symlink_one.is_symlink()
    assert symlink_two.is_symlink()

    page_one = Path(app.outdir, "_collections", "my_data", "one", "awesome.html")
    page_two = Path(app.outdir, "_collections", "my_data", "two", "awesome.html")
    assert page_one.exists()
    assert page_two.exists()
    assert "Awesome, this is nice" in page_one.read_text()
    assert "Awesome, this is nice" in page_two.read_text()
