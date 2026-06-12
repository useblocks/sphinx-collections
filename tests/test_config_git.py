from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "test_app",
    [
        {
            "buildername": "html",
            "srcdir": "doc_test/config_git",
            "confoverrides": {"collections_final_clean": False},
        }
    ],
    indirect=True,
)
def test_config_git(test_app):
    app = test_app
    app.build()

    target = Path(app.confdir, "_collections/mydata")

    assert target.exists()
    assert target.is_dir()
    # repository clone should contain a .git directory
    assert (target / ".git").exists()
