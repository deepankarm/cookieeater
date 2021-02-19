import os

from git import clone
from prompt import interact
from render import render_all
from helper import schema_path

template = 'https://github.com/deepankarm/pod-template.git'


if __name__ == '__main__':
    try:
        repo_dir = clone(url=template)
        schema = schema_path(repo_dir=repo_dir)
        user_context = interact(filepath=schema)
        if not user_context:
            print('Something wrong')
        render_all(context=user_context,
                   project_directory=os.path.join(repo_dir, user_context['project_dir']))
    except KeyboardInterrupt:
        print('\nUser interrupted. Nothing to do. Bye!')
