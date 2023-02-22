import os.path
import os


exclude_file_dir = set([
    'venv',
    '.gitignore',
    'db.sqlite3',
    'doc.txt',
    'README.md',
    'LICENSE',
    'py_code',
    '.idea',
    '.git',
    'static',
    'media',
    'wsgi.py',
    'manage.py',
])


# export PYTHON_BIN='/home/shoumitro/Documents/FR/test/pyc_converter/venv/bin/'
# export SOURCEDEFENDER_PASSWORD="1111"
# export SOURCEDEFENDER_SALT="2222"
# python defender_converter.py

os.environ.setdefault("SOURCEDEFENDER_SALT", "2222")
os.environ.setdefault("SOURCEDEFENDER_PASSWORD", "1111")

PYTHON_BIN = os.environ.get('PYTHON_BIN', '/bin/')
# PYTHON_BIN = os.environ.get('PYTHON_BIN', '/home/shoumitro/Documents/FR/test/pyc_converter/venv/bin/')
# os.environ.setdefault("PYTHON_BIN", "/usr/bin/")


def source_defender_converter(dir_list, working_dir):
    for fd in dir_list:
        path = os.path.join(working_dir, fd)
        if fd.endswith(".py") and os.path.isfile(path):
            path = os.path.join(working_dir, fd)
            sourcedefender = os.path.join(PYTHON_BIN, 'sourcedefender')
            os.system(sourcedefender + ' encrypt --remove ' + path)
        elif os.path.isdir(path):
            os.chdir(path)
            source_defender_converter([d for d in os.listdir(path) if d not in exclude_file_dir], path)


source_defender_converter([d for d in os.listdir('.') if d not in exclude_file_dir], os.getcwd())



