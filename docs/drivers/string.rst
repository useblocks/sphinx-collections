string
======

Copies a string defined in ``source`` into a file specified by ``target``.

.. code-block:: python

    collections = {
      'my_files: {
         'driver': 'string',
         'source': 'Awesome, this is nice',
         'target': 'my_data/my_file.txt'
         }
      }
   }

You can also use more complex strings by assigning them to a variable.

.. code-block:: python

    my_string = """
    Headline
    ========

    Ohh **awesome**!

    Multiline!

    .. codeblock:: rst

       Works also
       ----------
    """

    collections = {
      'my_files: {
         'driver': 'string',
         'source': my_string,
         'target': 'my_data/my_file.txt'
         }
      }
   }

