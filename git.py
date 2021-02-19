import os
import subprocess

from helper import mkdir, rmdir, is_valid_dir, default_clone_dir, is_git_installed


class InvalidRepo(Exception):
    """ """

class GitNotInstalled(Exception):
    """ """


def clone(url: str, jina_dir: str = default_clone_dir()):
    if not is_git_installed():
        raise GitNotInstalled('You don\'t have git installed. Are you even a developer?')

    repo_name = url.split('/')[-1]
    repo_dir = os.path.join(jina_dir, repo_name.rstrip('.git'))
    print(f'Directory to be created: {jina_dir}')
    mkdir(jina_dir)

    if is_valid_dir(repo_dir):
        while True:
            delete = input(f'You\'ve used {repo_name.rstrip(".git")} before, do you want to download it again? (yes|no): ')
            if delete == 'yes':
                rmdir(repo_dir)
                break
            elif delete == 'no':
                return repo_dir
            else:
                print('Invalid option! Please choose from (yes|no)')

    try:
        subprocess.check_output(
            ['git', 'clone', url],
            cwd=jina_dir,
            stderr=subprocess.STDOUT
        )
    except Exception as ex:
        rmdir(jina_dir)
        if 'not found' in ex.stdout.decode():
            raise InvalidRepo('Invalid repo!')
        raise

    return repo_dir


if __name__ == '__main__':
    template = 'https://github.com/deepankarm/pod-template.git'
    print(clone(url=template))
