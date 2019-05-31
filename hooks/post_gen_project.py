#!/usr/bin/env python
from ast import literal_eval
from subprocess import check_call


def shell(command):
    check_call(command, shell=True)


def make_venv(venv, python_version):
    venv_path = '{{ cookiecutter.virtualenv_root }}/{{ cookiecutter.project_slug }}_'+python_version.replace('.', '')
    shell(venv+' '+venv_path)
    pip = venv_path+'/bin/pip'
    shell(pip+' install -U pip')
    shell(pip+' install -e .[test,build]')


if __name__ == '__main__':

    shell('git init')
    shell('git add .')
    shell('git commit -m "initial boilerplate"')
    shell('git remote add origin git@github.com:{{ cookiecutter.github_path }}.git')

    virtualenv_root = "{{ cookiecutter.virtualenv_root }}"
    if virtualenv_root:
        python_versions = literal_eval("{{ cookiecutter.python_versions }}")
        if '2.7' in python_versions:
            make_venv('~/virtualenvs/virtualenv/bin/virtualenv', '2.7')
        make_venv('python{{ cookiecutter.python_versions[-1] }} -m venv', '{{ cookiecutter.python_versions[-1] }}')
