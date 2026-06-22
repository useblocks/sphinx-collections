from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "test_app",
    [
        {
            "buildername": "html",
            "srcdir": "doc_test/config_jinja_multiple_with_dir",
            "confoverrides": {"collections_final_clean": False},
        }
    ],
    indirect=True,
)
def test_config_jinja_multiple_with_dir(test_app):
    app = test_app
    app.build()
    generated1 = Path(app.srcdir, "_collections", "leaf", "my_jinja_test_for_max.rst")
    generated2 = Path(app.srcdir, "_collections", "leaf", "my_jinja_test_for_sandra.rst")
    assert generated1.exists()
    assert generated2.exists()
    txt1 = generated1.read_text()
    txt2 = generated2.read_text()
    assert "Hey Hooo!" in txt1
    assert "Max" in txt1
    assert "Hey Hooo!" in txt2
    assert "Sandra" in txt2
