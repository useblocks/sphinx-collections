Changelog
=========

Unreleased
----------

This release renamed the Python package from ``sphinxcontrib.collections`` to ``sphinx_collections``.

- ‼️ Dissolve sphinxcontrib namespace package (:pr:`38`)

  The ``sphinxcontrib`` namespace has been removed completely and the package
  is now a standalone package named ``sphinx_collections``. This simplifies
  packaging and avoides conflicts. The PyPI package name is still ``sphinx-collections``.

  **Migration guide:**

  1. **Update your Sphinx conf.py:**

     .. code-block:: python

        # OLD (no longer works)
        extensions = [
            "sphinxcontrib.collections",
        ]

        # NEW (required for 0.3.0+)
        extensions = [
            "sphinx_collections",
        ]

  #. **Update any custom driver imports in your code** (if you created custom drivers):

     .. code-block:: python

        # OLD
        from sphinxcontrib.collections.api import register_driver
        from sphinxcontrib.collections.drivers import Driver

        # NEW
        from sphinx_collections.api import register_driver
        from sphinx_collections.drivers import Driver

.. _`release:0.3.0`:

0.3.0
-----

:Released: 30.10.2025
:Full Changelog: `v0.2.0...v0.3.0 <https://github.com/useblocks/sphinx-collections/compare/0.2.0...6f088a9>`__

This is a release after a long time, to bring the package up to date with latest
packaging and CI practices. Also some minor fixes and improvements have been made.

.. note:: The PyPI released failed due to a packaging issue. Please use 0.3.1.

- 🔧 Year 2025 package infrastructure (:pr:`29`)

  - Introduce ``uv``, ``ruff``, ``tox`` with a PEP compliant pyproject.toml file.
    ``hatch`` is used for the sphinxcontrib namespace support.
  - Updated package classifiers.
  - Also dropped Python 3.9 support as it reached end-of-life.
    This is the reason to jump to version 0.3.0.
  - Added CI for lint / test / docs and auto-release on tag creation.
  - Added dependabot config.

- 🔧 Remove namespace init (:pr:`35`, :issue:`25`)

  The ``__init__.py`` files for the ``sphinxcontrib`` namespace have been removed
  to avoid conflicts with other packages in the same namespace.

.. _`release:0.2.0`:

0.2.0
-----

:Released: 15.02.2024

.. _`release:0.0.1`:

0.0.1
-----

* Initial version with basic feature set.
