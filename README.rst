**Complete documentation**: http://sphinx-collections.readthedocs.io/en/latest/

.. From here shared with index.rst of docs folder. #SHARED_CONTENT

Welcome to
==========

.. image:: https://github.com/useblocks/sphinx-collections/raw/master/docs/_static/sphinx_collections_logo.png
   :align: center

``Sphinx-Collections`` is a Sphinx extension to collect and generate additional files from different sources.
These files are added to the Sphinx Source Folder, so that Sphinx takes them into account for the overall
documentation build.

``Sphinx Collections`` supports multiple collections, where each collection has its own
source and target folder, specific configuration and
`use case based driver <https://sphinx-collections.readthedocs.io/en/latest/drivers/index.html>`_.

.. image:: https://github.com/useblocks/sphinx-collections/raw/master/docs/_static/sphinx_collections_chart.png
   :align: center

A collection can be activated by default or its usage can be triggered by Sphinx tags.

Depending on the usage of a specific collection for a build, its content integration can be controlled by the
`if-collection:: directive <https://sphinx-collections.readthedocs.io/en/latest/directives.html#if-collection>`_ .



Following use cases are supported:

* `Create file with content from string <https://sphinx-collections.readthedocs.io/en/latest/drivers/string.html>`_
* `Create file with content from function call <https://sphinx-collections.readthedocs.io/en/latest/drivers/function.html>`_
* `Copy single file from local path <https://sphinx-collections.readthedocs.io/en/latest/drivers/copy_file.html>`_
* `Copy folder tree from local path <https://sphinx-collections.readthedocs.io/en/latest/drivers/copy_folder.html>`_
* `Create a symlink to a local target <https://sphinx-collections.readthedocs.io/en/latest/drivers/symlink.html>`_
* `Create a usage-report of collections <https://sphinx-collections.readthedocs.io/en/latest/drivers/report.html>`_
* `Clone git repository <https://sphinx-collections.readthedocs.io/en/latest/drivers/git.html>`_
* `Create multiple files based on jinja-template and specific data <https://sphinx-collections.readthedocs.io/en/latest/drivers/jinja.html>`_

``Sphinx-Collections`` cares about keeping your collection folders clean before and after each build.

Installation
------------
Install via pip: ``pip install sphinx-collection``.

Then add the extension to the ``conf.py`` file of the Sphinx project::

   extensions = [
       "sphinxcontrib.collections",
       # other extensions
   ]


Introduction
------------

``Sphinx-Collections`` gets completely configured by variables inside the ``conf.py`` file of your Sphinx project::

   collections = {
      'my_files': {
         'driver': 'copy_folder',
         'source': '../../extra_files/'
      }
   }

The driver ``copy_folder`` allows to copy local folders and their files into your Sphinx project.
There are other drivers available, which support different use cases and file locations.

By default all files get copied to ``_collections/`` + ``collection_name``, so in this example the complete path
inside your documentation folder would be ``_collections/my_files/``. The location can be set specific for each
collection by using ``target`` option.

Then you can reference the copied files by using a toctree::

   .. toctree::
      _collections/my_files/index

Please see the
`documentation of the needed Driver <https://sphinx-collections.readthedocs.io/en/latest/drivers/index.html>`_
to know which options are available and necessary.

Tag based collections
---------------------

Use Sphinx tags to collect and integrate only needed data::

    collections = {
      'my_files': {
         'driver': 'copy',
         'source': '../../extra_files/',
         'tags': ['user_manual'],  # gets active, if "user_manual" is set as tag
         'active': False,  # by default, collection shall not be executed
      }
   }

Then run ``sphinx-build`` with ``-t`` option::

   sphinx-build -b html -t user_manual . _build/html

Collection based content
------------------------

Use ``if-collection`` to add content to a page only, if a specified collections has been executed successfully.

.. code-block:: rst

    .. if-collection:: my_test, my_data

       My Test & Data chapter
       ----------------------

        .. toctree::

          /_collections/my_test/index
          /_collections/my_data/index

For more information take a look into the
`documentation of if-collection <https://sphinx-collections.readthedocs.io/en/latest/directives.html#if-collection>`_.

Motivation
----------

This sphinx extension is based on the needs of a software development team inside
a german automotive company.

The project team was searching for a practical way to support multiple sphinx-based documentations inside a
mono-repository and have the possibility to merge different documentations together or to add files based
on external data.

Sphinx-Collections is part of a software bundle, which was designed to support the development of
`ISO 26262 <https://en.wikipedia.org/wiki/ISO_26262>`_ compliant software.
Other tools are:
`sphinx-needs <http://sphinxcontrib-needs.readthedocs.io/en/latest/>`_,
`sphinx-test-reports <http://sphinx-test-reports.readthedocs.io/en/latest/>`_,
`tox-envreport <http://tox-envreport.readthedocs.io/en/latest/>`_.
