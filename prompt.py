import yaml
import builtins
from collections import OrderedDict

from helper import is_valid_file


class InvalidSchemaPath(Exception):
    """ """


class InvalidSchema(Exception):
    """ """


def interact(filepath: str):
    if not is_valid_file(filepath):
        raise InvalidSchemaPath('Schema path is not valid')

    with open(filepath) as f:
        context_vars = yaml.safe_load(f.read())

    if 'project_dir' not in context_vars:
        raise InvalidSchema('project_dir is missing in the yml file')

    if 'fields' not in context_vars:
        raise InvalidSchema('project_dir is missing in the yml file')

    rendered_context_vars = OrderedDict()
    rendered_context_vars['project_dir'] = context_vars['project_dir']
    try:
        for field in context_vars['fields']:
            while True:
                value = input(f'\n{field["help"]} ' +
                              (f'(Default - {field["default"]}): ' if 'default' in field else '') +
                              ('\nAllowed values: \n{}\n'.format('\n'.join(field['allowed']))
                               if 'allowed' in field else ''))
                if value:
                    # convert 'list' to list, 'str' to str
                    field_type = getattr(builtins, field['type'])

                    if not isinstance(value, field_type):
                        # Validate value datatype
                        print(f'Invalid type of value passed. Expected {field_type}, got {type(value)}!')
                    elif 'allowed' in field and value not in field['allowed']:
                        # Valudate list of choices
                        print(f'`{value}` not in allowed list')
                    else:
                        rendered_context_vars[field['name']] = value
                        break
                elif field['default']:
                    rendered_context_vars[field['name']] = field['default']
                    break
                else:
                    print(f'Cannot pass empty value!')
        return rendered_context_vars

    except Exception:
        print('Some error!')
        raise

if __name__ == '__main__':
    a = interact(filepath='/home/deepankar/.jina/templates/pod-template/schema.yml')
    import json
    print(json.dumps(a, indent=4))
