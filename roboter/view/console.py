import os
import string
import termcolor


def get_template_dir_path():
    template_dir_path = None
    if not template_dir_path:
        base_dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        template_dir_path = os.path.join(base_dir_path,"templates")
        return template_dir_path


def find_template_path(filename):
    dir_path = get_template_dir_path()
    file_path = os.path.join(dir_path, filename)
    if not os.path.exists(file_path):
        raise Except_Not_Found(f"Hey we cannot find the file{filename}")

    return file_path


class Except_Not_Found(Exception):
    pass


def get_template_path(filename, color = "red"):
    template_path = find_template_path(filename)
    with open(template_path, "r") as template:
        contents = template.read()
        contents = contents.strip(os.linesep)
        contents = f'{"=" * 60}\n{contents}\n{"=" * 60}'
        contents = termcolor.colored(contents, color)
        str_contents = string.Template(contents)
        return str_contents

