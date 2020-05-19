**Complete documentation**: http://sphinx-collections.readthedocs.io/en/latest/

.. image:: https://github.com/useblocks/sphinx-collections/raw/master/docs/_static/sphinx_collections_logo.png
   :align: center

.. From here shared with index.rst of docs folder. #SHARED_CONTENT

Sphinx-Collections
==================

``Sphinx-Collections`` is a Sphinx extension to collect and generate additional files from different sources before
Sphinx starts the overall build.

All collected and generated files get registered to the Sphinx Env and are therefore available during a Sphinx build.

It was created to support the following use cases:

* Grab additional ``.rst`` or ``md`` files from outside the ``docs`` source folder.
* Merge multiple Sphinx projects into one project
* Generate ``.rst`` and ``.md`` files based on data in ``json`` files.

Internally ``Sphinx-Collections`` is based on a set of ``drivers``, which support different use cases.
Feel free to extend the list of available ``drivers`` by creating a PR in our github project.

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
There are other drivers available, which support different use cases and and files locations.

By default all files get copied to ``_collections/`` + ``collection_name``, so in this example the complete path
inside your documentation folder would be ``_collections/my_files/``. The location can be set specific for each
collection by using ``target`` option.

Then you can reference the copied files by using a toctree::

   .. toctree::
      _collections/my_files/index

Please see the documentation of the needed Driver to know which options are available and necessary.

Tag based collections
---------------------

Use Sphinx tags to collect and integrate only needed data::

    collections = {
      'my_files': {
         'driver': 'copy',
         'source': '../../extra_files/'
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
