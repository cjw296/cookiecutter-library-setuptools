
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

|CircleCI|_  |Docs|_

.. |CircleCI| image:: https://circleci.com/gh/{{ cookiecutter.github_path }}/tree/master.svg?style=shield
.. _CircleCI: https://circleci.com/gh/{{ cookiecutter.github_path }}/tree/master

.. |Docs| image:: https://readthedocs.org/projects/{{ cookiecutter.project_slug }}/badge/?version=latest
.. _Docs: http://{{ cookiecutter.project_slug }}.readthedocs.org/en/latest/

{{ cookiecutter.project_short_description }}
