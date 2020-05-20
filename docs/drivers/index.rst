.. _drivers:

Drivers
=======

Drivers represents the technical function, which gets configured by the configuration given by a collection.

Each collection must reference a single driver, which cares about:

* Initial clean up
* Configured execution
* Final clean up

``Sphinx-Collections`` already provides some major drivers, which support different use case.

.. toctree::
   :maxdepth: 1

   copy_folder
   copy_file
   string
   function
   report

Own drivers
-----------

You can specify own drivers directly inside your ``conf.py`` file.

Using own drivers instead of e.g. a pure function call has several advantages:

* Configuration handling.
* Correct and easy logging.
* Executed during correct Sphinx phases.
* Integrated clean-up.
* Report capabilities.

.. code-block::

    from sphinxcontrib.collections.drivers import Driver
    from sphinxcontrib.collections.api import register_driver


    class myDriver(Driver):
        def run(self):
            self.info('Run for source {}'.format(self.config['source']))

        def clean(self):
            self.info('Clean')

    register_driver('my_driver', myDriver)

    collections = {
        'my_river_test': {
            'driver': 'my_driver',
            'source': '../tests/dummy/',
            'active': True,
        },

If you have created an awesome driver, please consider to provide it to ``Sphinx-Collections`` by creating
a PR on our `github project <https://github.com/useblocks/sphinx-collections>`_ .
This would help our little Sphinx community a lot. Thanks!

Driver class
~~~~~~~~~~~~

.. autoclass:: sphinxcontrib.collections.drivers.Driver
   :members:
   :undoc-members:
   :private-members:
   :special-members: __init__
