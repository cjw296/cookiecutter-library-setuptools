Cookiecutter for my standard library setup when using setuptools.

To use:

.. code-block:: bash

  cookiecutter gh:cjw296/cookiecutter-library-setuptools

If you're me, on my laptop, you want:

.. code-block:: bash

  ~/virtualenvs/cookiecutter/bin/cookiecutter cookiecutter-library-setuptools/

This sets up:

- Python package using a ``setup.py``
- Tests using pytest
- Docs using Sphinx
- CI (including releasing) using CircleCI and Carthorse
