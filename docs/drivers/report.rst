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

.. hint::

   The ``executed`` option in the report for the current report-collection is always ``False``, as this
   options gets changed **after** the report was successfully generated.


The following template is used to build the report:

.. literalinclude:: ../../sphinxcontrib/collections/drivers/report.rst.template

.. if-collection:: report

   Example Report
   --------------

   This is the report of the latest run for this documentation.

   .. include:: /_collections/doc_collection_report.rst

Clean up behavior
-----------------
During clean up the target folders, which contains the report, gets deleted.