function
========

Executes a function referenced by ``source`` and writes its return value into a file specified by ``target``.

.. code-block:: python

    def my_own_data(config):
        string = 'This data gets written into {}'.format(config['target'])

        return string

    collections = {
      'my_files': {
         'driver': 'function',
         'source': my_own_data,
         'target': 'my_data/my_file.txt'
         'write_result': True
         }
    }

The specified function gets 1 argument during the call: A dictionary which contains the complete configuration of the
collection.

If return value is not None, the returned data is written to the file specified by ``target``.

Options
-------

write_result
~~~~~~~~~~~~

If ``write_result`` is False, no data is written by the driver.
But this could be done by the function itself.

**Default**: ``True``

Clean up behavior
-----------------
The target folder/file gets deleted.
