from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "test_app",
    [
        {
            "buildername": "html",
            "srcdir": "doc_test/config_report",
            "confoverrides": {"collections_final_clean": False},
        }
    ],
    indirect=True,
)
def test_config_report(test_app):
    app = test_app
    app.build()

    report_file = Path(app.srcdir, "_collections", "report.rst")
    assert report_file.exists()

    contents = report_file.read_text()
    assert "my_string" in contents
    assert "my_report" in contents
    assert "**Active**: True" in contents
    assert "**Executed**: True" in contents
