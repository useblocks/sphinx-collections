report
======

Creates a collection report in file specified by ``target``.

Please be sure to specify this report as one of the latest collections, otherwise other
collections have not been executed before this report gets generated.

.. code-block:: python

    collections = {
      'my_collection_report: {
         'driver': 'report',
         'target': 'reports/collections.rst'
         }
      }
   }


The following template is used to build the report:

.. literalinclude:: ../../sphinxcontrib/collections/drivers/report.rst.template

**Example**:

This is the report of the latest run for this documentation.

.. literalinclude:: /_collections/doc_collection_report.rst