from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "test_app",
    [
        {
            "buildername": "html",
            "srcdir": "doc_test/config_git_with_dir",
            "confoverrides": {"collections_final_clean": False},
        }
    ],
    indirect=True,
)
def test_config_git_with_dir(test_app):
    app = test_app
    app.build()

    target = Path(app.confdir, "_collections/leaf/mydata")

    assert target.exists()
    assert target.is_dir()
    assert (target / ".git").exists()
