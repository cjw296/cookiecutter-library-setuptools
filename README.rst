Cookiecutter for my standard library setup when using setuptools.

To use:

.. code-block:: bash

  cookiecutter gh:cjw296/cookiecutter-library-setuptools

If you're me, on my laptop, you want:

.. code-block:: bash

  cd ~/vcs/git
  ~/virtualenvs/cookiecutter/bin/cookiecutter cookiecutter-library-setuptools/

This sets up:

- Python package using a ``setup.py``
- Tests using pytest
- Docs using Sphinx
- CI (including releasing) using CircleCI and Carthorse
- A skeleton ``.idea`` for PyCharm. (You'll still need to add the interpreter in the virtualenv by hand)
