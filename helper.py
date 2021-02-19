import os
from typing import Dict, Union
from shutil import rmtree, move, which
from distutils.dir_util import copy_tree

if False:
    from jinja2 import Environment, Template


def mkdir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)


def rmdir(dir):
    rmtree(dir)


def copydir(src, dst):
    copy_tree(src=src, dst=dst)


def rename(src, dst):
    move(src, dst)


def is_valid_file(path):
    return os.path.isfile(path)


def is_valid_dir(path):
    return os.path.isdir(path)


def default_clone_dir():
    return os.path.join(os.path.expanduser('~'), '.jina', 'templates')


def is_git_installed():
    return which('git')


def schema_path(repo_dir):
    return os.path.join(repo_dir, 'schema.yml')


def render_string(environment: 'Environment', name: str, context: Dict):
    return environment.from_string(name).render(**context)


def render_file_content(environment: 'Environment', name: Union['Template', str], context: Dict):
    return environment.get_template(name).render(**context)
