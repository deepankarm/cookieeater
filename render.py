import os
from typing import Dict
from jinja2 import Environment, FileSystemLoader

from helper import copydir, rename, render_string, render_file_content


def render_all(context: Dict, project_directory: str):
    env = Environment(loader=FileSystemLoader(project_directory))

    # Render project root
    rendered_project_name = render_string(environment=env, name=project_directory, context=context)
    copydir(src=project_directory, dst=os.path.basename(rendered_project_name))

    for filename in env.list_templates():
        # Render filename
        rendered_filename = render_string(environment=env, name=filename, context=context)
        original_path = os.path.join(os.curdir, os.path.basename(rendered_project_name), filename)

        if filename != rendered_filename:
            new_path = os.path.join(os.curdir, os.path.basename(rendered_project_name), rendered_filename)
            rename(original_path, new_path)
        else:
            new_path = original_path

        # Render file content
        rendered_content = render_file_content(environment=env, name=filename, context=context)
        with open(new_path, 'w+') as f:
            f.writelines(rendered_content)
