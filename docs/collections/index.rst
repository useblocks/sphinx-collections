.. _collections:

Collections
===========

Collections are defined by setting :ref:`conf_collections` in ``conf.py``::

    collections = {
          '<COLLECTION_NAME>': {
             'driver': '<DRIVER>',
             'source': 'source path',
             '<COLLECTION_OPTION>': 'any value'
          }
       }

``<COLLECTION_NAME>`` must be a string, which can also be used as folder name.
So try to avoid special characters or other hashable objects.

``driver`` must always be set and match a registered :ref:`Driver <drivers>`.

Also ``source`` must always be specified. Its content is validated and used by the driver.

``<COLLECTION_OPTION>`` should also be a string, which matches one of the options below.
If it does not match, it gets ignored.

Collection Options
------------------
Most of the below options have a default value.
Therefore setting them inside your configuration is not needed, if you are happy with the related default value.

However, options which are needed by drivers normally don't have a default value.
So please take a look into the related :ref:`driver <drivers>` configuration to see what is needed and supported.

driver
~~~~~~

Specifies the driver to use. Must be a string.

If not set or driver is unknown, an exception gets thrown.

For a complete list of drivers, please see :ref:`drivers`.

**Mandatory**: Yes

.. code-block:: python

    collections = {
        'my_collection': {
            'driver': 'copy_folder',
            'source': 'source path',
        }
    }

source
~~~~~~
String of the ``source`` to use.

Depending on the used driver, this can be a folder, file, a git repository or whatever.

**Mandatory**: Yes

.. code-block:: python

    collections = {
        'my_collection': {
            'driver': 'copy_folder',
            'source': 'source path',
        }
    }

.. _collections_target:

target
~~~~~~

Target path, where to store the new files.
Depending on the :ref:`driver <drivers>` this must be a folder or a single file.

Can be an absolute path or a relative path, which starts from the folder set by
:ref:`conf_collections_target`.

If not set, the collection name is used as target name.

**Example**:

If :ref:`conf_collections_target` has default value ``_collections`` and collection is named ``my_first_collection``,
then target is set to ``_collections/my_first_collection`` inside your documentation
project.

.. hint::

   ``target`` must always be somewhere inside your documentation folder
   (where your ``conf.py`` is stored). Targets outside of your documentation
   are not supported.

**Default**: collection name

.. code-block:: python

    collections = {
        'my_collection': {
            'driver': 'copy_folder',
            'source': 'source path',
            'target': 'custom_folder/folder_x/'
        }
    }

.. _collections_active:

active
~~~~~~
``active`` can be set to ``True`` or ``False``.
If set to ``False``, the collection gets completely ignored during documentation build.

**Default**: ``True``

.. code-block:: python

    collections = {
        'my_collection': {
            'driver': 'copy_folder',
            'source': 'source path',
            'active': False
        }
    }

safe
~~~~
Takes a boolean value and if it is set to ``True`` any problem will raise an exception and stops the build.

**Default**: ``True``

.. code-block:: python

    collections = {
        'my_collection': {
            'driver': 'copy_folder',
            'safe': False,
        }
    }

.. _collections_clean:

clean
~~~~~

If set to ``False``, no clean-up is taking place before collections get executed.

Default value can be changed for all collections by setting :ref:`conf_collections_clean`

**Default**: ``True``

.. code-block:: rst

    collections = {
        'my_collection': {
            'driver': 'copy_folder',
            'source': 'source path',
            'clean': False
        }
    }

.. _collections_final_clean:

final_clean
~~~~~~~~~~~

If set to ``True``, a final clean up at the end of a Sphinx build is executed.

Often used to keep your working tree clean and have collected files only during build in related folders.

Default value can be changed for all collections by setting :ref:`conf_collections_final_clean`.

**Default**: ``True``

.. code-block:: rst

    collections = {
        'my_collection': {
            'driver': 'copy_folder',
            'source': 'source path',
            'final_clean': False
        }
    }

.. _collections_tags:

tags
~~~~
List of tags, which trigger an activation of the collection.
Should be used together with :ref:`collections_active` set to ``False``, otherwise the collection gets always
executed.

.. code-block:: python

    collections = {
        'my_collection': {
            'driver': 'copy_folder',
            'source': 'source path',
            'active': False,
            'tags': ['my_collection', 'dummy']
        }
    }

Use ``-t tag`` option of ``sphinx-build`` command to trigger related collections.

.. code-block:: text

   sphinx-build -b html -t dummy . _build/html

Driver Options
--------------

Options for drivers are also stored directly with the configuration for collections.

Please take a look into the specific :ref:`Driver <drivers>` to get information
about its additional configuration possibilities.
