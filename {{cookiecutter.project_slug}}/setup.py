# See license.txt for license details.
# Copyright (c) {% now 'local', '%Y' %}, {{ cookiecutter.full_name }}

import os

from setuptools import setup, find_packages

base_dir = os.path.dirname(__file__)

setup(
    name='{{ cookiecutter.project_slug }}',
    version='{{ cookiecutter.project_version }}',
    author='{{ cookiecutter.full_name }}',
    author_email='{{ cookiecutter.email }}',
    license='MIT',
    description=(
        "{{ cookiecutter.project_short_description }}"
    ),
    long_description=open('README.rst').read(),
    url='https://github.com/{{ cookiecutter.github_path }}',
    classifiers=[
        'License :: OSI Approved :: MIT License',
{%- set major_versions = {} %}
{%- for version in cookiecutter.python_versions -%}
{%- set major_version = version[0] -%}
{%- if major_version not in major_versions -%}
        {%- set _ = major_versions.__setitem__(major_version, True) %}
        'Programming Language :: Python :: {{ major_version }}',
{%- endif %}
        'Programming Language :: Python :: {{ version }}',
{%- endfor %}
    ],
    packages=find_packages(exclude=["tests"]),
    zip_safe=False,
    include_package_data=True,
    extras_require=dict(
        test=[
            'pytest',
            'pytest-cov',
            'sybil',
            'testfixtures',
        ],
        build=['furo', 'sphinx', 'setuptools-git', 'twine', 'wheel']
    ),
)
