copy_file
=========

Copies a single file from ``source`` to ``project``. Both should should have a valid file name in it.

.. code-block:: python

    collections = {
      'my_files': {
         'driver': 'copy_file',
         'source': '../extra_files/my_file.txt',
         'target': 'my_data/new_data.txt'
      }
    }

Clean up behavior
-----------------
During clean up the target file gets deleted.
