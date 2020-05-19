.. _directives:

Directives
==========

if_collection
-------------

Content is added to rst only, if named collection got executed correctly and is therefore available:

.. code-block:: rst

    .. if-collection:: my_test, my_data

       .. toctree::

          /_collections/my_test/index
          /_collections/my_data/index

Takes one single argument, which is a comma-separated list of collection names.
If one of these collections was executed correctly the data from the content part is added and parsed.

In all other cases nothing is added to the page.

Behaves like Sphinx own
`only <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-only>`__
directive, but content gets removed already during read-in phase and is therefore not parsed
by Sphinx, if collection was not executed. This avoids a lot of trouble and warnings.


.. hint::

   If you use ``if-collection`` to add entries to a toctree or set any other value, which Sphinx stores in its
   internal cache (pickled environment), please use ``sphinx-build`` with option ``-E`` to avoid caching.
   Otherwise a tag or collection change may not get recognized by Sphinx, if related ``rst`` file got no updates and is
   therefore taken from cache.

There is a abbreviation available to save some characters: ``.. ifc::`` :

.. code-block:: rst

    .. ifc:: my_test

       Awesome!
