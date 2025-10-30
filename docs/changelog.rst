Changelog
=========

.. _`release:0.3.0`:

0.3.0
-----

:Released: 30.10.2025
:Full Changelog: `v0.2.0...v0.3.0 <https://github.com/useblocks/needs-config-writer/compare/0.2.0...6f088a9>`__

This is a relase after a long time, to bring the package up to date with latest
packaging and CI practices. Also some minor fixes and improvements have been made.

- 🔧 Year 2025 package infrastructure (:pr:`29`)

  - Introduce ``uv``, ``ruff``, ``tox`` with a PEP compliant pyproject.toml file.
    ``hatch`` is used for the sphinxcontrib namespace support.
  - Updated package classifiers.
  - Also dropped Python 3.9 support as it reached end-of-life.
    This is the reason to jump to version 0.3.0.
  - Added CI for lint / test / docs and auto-release on tag creation.
  - Added dependabot config.

- 🔧 Remove namespace init (:pr:`35`, :issue:`25`)

  This was done to avoid conflicts with other packages using the same namespace.

.. _`release:0.2.0`:

0.2.0
-----

:Released: 15.02.2024

.. _`release:0.0.1`:

0.0.1
-----

* Initial version with basic feature set.
