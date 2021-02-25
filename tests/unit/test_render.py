import pytest
import os

from collections import OrderedDict
from render import render_all

pod_user_context = OrderedDict([('project_dir', "{{executor_name.replace(' ', '_').replace('-', '_')}}"),
                      ('executor_name', 'FirstExecutor'),
                      ('kind', 'Encoder'),
                      ('description', 'First encoder'),
                      ('keywords', ['jina']),
                      ('pip_requirements', ['jina']),
                      ('base_image', 'jinaai/jina'),
                      ('author_name', 'Jina AI Dev-Team (dev-team@jina.ai)'),
                      ('author_url', 'https://jina.ai'),
                      ('author_vendor', 'Jina AI Limited'),
                      ('docs_url', 'https://github.com/jina-ai/jina-hub'),
                      ('version', '0.0.1'),
                      ('license', 'apache-2.0')])

app_user_context = OrderedDict([('project_dir', "{{project_name.replace(' ', '_').replace('-', '_')}}"),
                      ('project_name', 'NeuralProject'),
                      ('jina_version', '0.8.2'),
                      ('author_name', 'Jina AI Dev-Team (dev-team@jina.ai)'),
                      ('project_short_description', 'neural project'),
                      ('task_type', 'cv'),
                      ('index_type', 'files'),
                      ('public_port', 65481),
                      ('parallel', 2),
                      ('shards', 2),
                      ('version', '0.0.1')])

def test_render_pod_template():
    repo_dir = '/Users/rutujasurve/Documents/jina-ai/cookieeater/tests/unit/test_pod_template'
    rendered_files = render_all(context=pod_user_context,
               project_directory=os.path.join(repo_dir, pod_user_context['project_dir']))

    expected_files = ['Dockerfile', 'README.md', '__init__.py', 'config.yml', 'manifest.yml', 'requirements.txt', 'tests/__init__.py', "tests/test_{{executor_name.lower().replace(' ','_').replace('-','_')}}.py"]

    assert expected_files == rendered_files


def test_render_app_template():
    repo_dir = '/Users/rutujasurve/Documents/jina-ai/cookieeater/tests/unit/test_app_template'
    rendered_files = render_all(context=app_user_context,
               project_directory=os.path.join(repo_dir, app_user_context['project_dir']))

    expected_files = ['Dockerfile', 'README.md', '__init__.py', 'config.yml', 'manifest.yml', 'requirements.txt', 'tests/__init__.py', "tests/test_{{executor_name.lower().replace(' ','_').replace('-','_')}}.py", 'Dockerfile', 'README.md', '__init__.py', 'app.py', 'flows/index.yml', 'flows/query.yml', 'pods/craft.yml', 'pods/doc.yml', 'pods/encode.yml', 'requirements.txt', 'tests/__init__.py', "tests/test_{{project_name.lower().replace(' ','_').replace('-','_')}}.py"]

    assert expected_files == rendered_files
