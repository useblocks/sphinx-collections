.. _directives:

Directives
==========

if_collection
-------------

Content is added to rst only, if named collection got executed correctly and is therefore available::

    .. if_collection:: my_test

       .. toctree::

          my_test/test1
          my_test/test2

Behaves like the ``only`` directive, but content gets removed already during read-in phase and is therefore not parsed
by Sphinx, if condition is not valid. This avoids a lot of trouble and warnings.