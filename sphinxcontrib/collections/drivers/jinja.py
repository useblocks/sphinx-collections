"""
jinja
=====

Creates one or multiple files based on a given Jinja template in ``source``.

``data`` must be a dictionary and its keys can be used as identifier in the template.

**Example for single data element**

*template file*

Path: ``templates/say_hello.rst.template``

.. code-block:: jinja

   Hey Hooo!

   It's {{name}} from {{city}}!

*conf.py file*

.. code-block:: python

   collections = [
       'jinja_test': {
           'driver': 'jinja',
           'source': 'templates/say_hello.rst.template',
           'target': 'my_jinja_test.rst',
           'data': {
               'name': 'Max',
               'city': 'Munich'
           },
           'active': True,
       },
   ]

The values inside ``{{..}}`` get replaced by the related value from the data dictionary.

If ``multiple_files`` is set to ``True``, ``data`` must be a list and the driver gets executed
for each element (dict) in this list.

To get also a new file for each element of the list, you can use Jinja syntax also in ``target`` and
``source``.

**Example for multiple data element**

*template file*

Path: ``templates/say_hello.rst.template``

.. code-block:: jinja

   Hey Hooo!

   It's {{name}} from {{city}}!

*conf.py file*

.. code-block:: python

   collections = [
       'jinja_test': {
           'driver': 'jinja',
           'source': 'templates/say_hello.rst.template',
           'target': 'my_jinja_test_for_{{name|lower}}.rst',
           'data': [
               {
                   'name': 'Max',
                   'city': 'Munich'
               },
               {
                   'name': 'Sandra',
                   'city': 'Barcelone'
               },
           ],
           'active': True,
       },
   ]

This example would create two files: ``my_jinja_test_for_max.rst`` and ``my_jinja_test_for_sandra.rst``


"""

import os

from jinja2 import Template

from sphinxcontrib.collections.drivers import Driver


class JinjaDriver(Driver):
    def run(self):
        data = self.config.get("data", {})
        multiple_files = bool(self.config.get("multiple_files", False))

        # We only deal with data for multi-files.
        # So if we only get one data set, we put it into a list.
        if not multiple_files:
            data = [data]

        self.info("Creating {} file/s from Jinja template...".format(len(data)))
        for datum in data:
            source = Template(self.config["source"]).render(**datum)
            target = Template(self.config["target"]).render(**datum)

            source = self.get_path(source)
            target = self.get_path(target)

            if not os.path.exists(source):
                self.error("Source {} does not exist".format(source))
                return

            try:
                template = Template(open(source).read())
                result = template.render(**datum)
            except Exception as e:
                self.error("Problems during creating of symlink.", e)

            try:
                with open(target, "w") as target_file:
                    target_file.write(result)
            except IOError as e:
                self.error("Problems during writing rendered template to target", e)

    def clean(self):
        data = self.config.get("data", {})
        multiple_files = bool(self.config.get("multiple_files", False))

        # We only deal with data for multi-files.
        # So if we only get one data set, we put it into a list.
        if not multiple_files:
            data = [data]

        self.info("Cleaning {} jinja Based file/s ...".format(len(data)))

        for datum in data:
            target = Template(self.config["target"]).render(**datum)
            target = self.get_path(target)

            try:
                os.remove(target)
                self.info("  File deleted: {}".format(target))
            except FileNotFoundError:
                pass  # Already cleaned? I'm okay with it.
            except IOError as e:
                self.error("Problems during cleaning for collection {}".format(self.config["name"]), e)
