.. _drivers:

Drivers
=======

Drivers represent the tasks which get configured by a collection's configuration.

Each collection must reference a single driver, which cares about:

* Initial clean up
* Configured execution
* Final clean up

``Sphinx-Collections`` already provides some major drivers, which support different use cases.

.. toctree::
   :glob:
   :maxdepth: 1

   *

Custom drivers
--------------

You can create your own drivers directly inside your ``conf.py`` file.

Creating your own drivers has several advantages:

* Configuration handling.
* Correct and easy logging.
* Ensure execution during correct Sphinx phases.
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
        'my_driver_test': {
            'driver': 'my_driver',
            'source': '../tests/dummy/',
            'active': True,
        },
    }

If you have created an awesome driver, please consider contributing it to ``Sphinx-Collections`` by creating
a PR on our `github project <https://github.com/useblocks/sphinx-collections>`_ .
This would help our little Sphinx community a lot. Thanks!

Driver class
~~~~~~~~~~~~

.. autoclass:: sphinxcontrib.collections.drivers.Driver
   :members:
   :undoc-members:
   :private-members:
   :special-members: __init__
