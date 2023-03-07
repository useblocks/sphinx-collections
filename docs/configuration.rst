.. _configuration:

Configuration
=============

.. _conf_collections:

collections
-----------

Takes a dictionary, which configures the :ref:`collections`.

.. code-block:: rst

    collections = {
      'my_files': {
         'driver': 'copy',
         'source': '../../extra_files/'
      }
    }

See :ref:`collections` for details.


**Default**: ``{}``

.. _conf_collections_target:

collections_target
------------------

Defines the default storage location for all collections.

If a relative path is set, this path is relative to the documentation folder (the one which contains your ``conf.py``).

Can be set individually for each collection by using :ref:`collections_target`.

**Default**: ``_collections``

.. _conf_collections_clean:

collections_clean
-----------------

If ``True`` all configured target locations get wiped out at the beginning.

The related driver of the collection specifies if cleaning is needed and how to perform it.

If you use nested collections, e.g ``_collections/collection_A/collection_B`` the outer clean routine of
a collection (here ``collection_A``) deletes also the content of other collections (here ``collection_B``).

This can be overwritten for each collection be configuring :ref:`collections_clean`.

**Default**: ``True``

.. _conf_collections_keep:

.. _conf_collections_final_clean:

collections_final_clean
-----------------------

If this option is set to ``True``, all collections start their clean-up
routine after a Sphinx build is done.  Normally It doesn't matter if
the build was a success or failed.

Works similarly to :ref:`conf_collections_clean`, but at the end of the build instead before.

Can be overwritten for each collection be setting :ref:`collections_final_clean`.

This final clean up is normally active to keep your working tree clean and get no unnecessary files into git or any
other solution.

**Default**: ``True``
