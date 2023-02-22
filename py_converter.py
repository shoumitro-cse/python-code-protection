import os.path
import os

# run converter
# /home/shoumitro/Documents/FR/social_backend/venv/bin/python py_converter.py

# for uncompile. it's only works for python version <= 3.8. 
# pip install uncompyle6
# uncompyle6 manage.pyc > manage.py
# As of this writing, no existing version of uncompyle6 works for Python 3.9 or 3.10 or later(and your bytecode is built for 3.10 or later).

exclude_file_dir = set([
    'venv',
    '.gitignore',
    'db.sqlite3',
    'doc.txt',
    'py_converter.py',
    'README.md',
    'LICENSE',
    'py_code',
    '.idea',
    '.git',
    'static',
    'media',
])

PYTHON_BIN = os.environ.get('PYTHON_BIN', '/bin/')
# PYTHON_BIN = os.environ.get('PYTHON_BIN', '/home/shoumitro/Documents/FR/test/pyc_converter/venv/bin/')
# os.environ.setdefault("PYTHON_BIN", "/usr/bin/")


def pyc_converter(dir_list, working_dir):
    for fd in dir_list:
        path = os.path.join(working_dir, fd)
        if fd.endswith(".pyc") and os.path.isfile(path):
            new_path = os.path.join(working_dir, fd[:-1])
            os.system(PYTHON_BIN + 'uncompyle6 ' + path + ' > ' + new_path)
            os.remove(path)
        elif os.path.isdir(path):
            os.chdir(path)
            pyc_converter([d for d in os.listdir(path) if d not in exclude_file_dir], path)


pyc_converter([d for d in os.listdir('.') if d not in exclude_file_dir], os.getcwd())
