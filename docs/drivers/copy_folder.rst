copy_folder
===========

Copies a folder tree from ``source`` into your documentation project::

    collections = {
        'my_files': {
            'driver': 'copy_folder',
            'source': '../../extra_files/',
            'target': 'my_data/'
            'ignore': ['*.dat', '.exe'],
        }
    }

Options
-------

ignore
~~~~~~

List of file matches, which shall get ignored from copy.

This variable is internally given to
`shutil.ignore_patterns <https://docs.python.org/3/library/shutil.html#shutil.ignore_patterns>`_.
So it must follow its syntax rules.