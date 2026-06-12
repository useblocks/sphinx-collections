from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "test_app",
    [
        {
            "buildername": "html",
            "srcdir": "doc_test/config_jinja_single_with_dir",
            "confoverrides": {"collections_final_clean": False},
        }
    ],
    indirect=True,
)
def test_config_jinja_single_with_dir(test_app):
    app = test_app
    app.build()
    generated = Path(app.srcdir, "_collections", "leaf", "my_jinja_test.rst")
    assert generated.exists()
    txt = generated.read_text()
    assert "Hey Hooo!" in txt
    assert "Max" in txt
    assert "Munich" in txt
