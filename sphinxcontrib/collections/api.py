from sphinxcontrib.collections.collections import DRIVERS
from sphinxcontrib.collections.drivers import Driver


def register_driver(name, driver_class):
    if not issubclass(driver_class, Driver):
        raise SphinxCollectionsApiError("Given driver class must be a subclass of the main Driver class.")

    try:
        DRIVERS[name] = driver_class
    except KeyError:
        raise SphinxCollectionsApiError(f"Driver with name {name} already exists.")


class SphinxCollectionsApiError(BaseException):
    pass
