Copy
====

Copies a folder tree from ``source`` into your documentation project::

    collections = {
      'my_files: {
         'driver': 'copy',
         'source': '../../extra_files/',
         'target': 'my_data/'
         'ignore': ['*.dat', '.exe'],
         }
      }
   }

