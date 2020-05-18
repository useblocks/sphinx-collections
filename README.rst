**Complete documentation**: http://sphinx-collections.readthedocs.io/en/latest/

.. image:: docs/_static/sphinx_collections_logo.png
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
* Generate ``.rst`` and ``.md`` files based on data on ``json`` files.

Internally ``Sphinx-Collections`` is based on a set of ``drivers``, which support different use cases.
Feel free to extend the list of available ``drivers`` by creating a PR in our github project.

Introduction
------------

``Sphinx-Collections`` is completely configured by variables inside the ``conf.py`` file of your Sphinx project::

   collections = {
      'my_files': {
         'driver': 'copy',
         'source': '../../extra_files/'
      }
   }

The driver ``copy`` allows to copy local files into your Sphinx project.
There are other drivers available, which support different use cases and and files locations.

By default all files get copied to ``_collections/`` + ``collection_name``, so in this example the complete path
inside your documentation folder would be ``_collections/my_files/``. The location can be set specific for each
collection by using ``target`` option.

Then you can reference the copied files by using a toctree::

   .. toctree::
      _collections/my_files/index

Please see the documentation of the needed Driver to know which options are available and necessary.
