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



PYTHON_BIN = os.environ.get('PYTHON_BIN', '/bin/')


def pyarmor_converter(dir_list, working_dir):
    for fd in dir_list:
        path = os.path.join(working_dir, fd)
        if fd.endswith(".py") and os.path.isfile(path):
            path = os.path.join(working_dir, fd)
            pyarmor = os.path.join(PYTHON_BIN, 'pyarmor')
            os.system(pyarmor + ' obfuscate --restrict=0 ' + path)
        elif os.path.isdir(path):
            os.chdir(path)
            pyarmor_converter([d for d in os.listdir(path) if d not in exclude_file_dir], path)


def pyarmor_converter(dir_list, working_dir):
    for fd in dir_list:
        path = os.path.join(working_dir, fd)
        if fd.endswith("dist") and os.path.isdir(path):
            for f in os.listdir(path):
                if f.endswith(".py"):
                    src_file_path = os.path.join(path, f)
                    dest_file_path = os.path.join(working_dir, f)
                    os.rename(src_file_path, dest_file_path)
            os.rmdir(path)
        elif fd.endswith(".py") and os.path.isfile(path):
            os.remove(path)
        elif os.path.isdir(path):
            os.chdir(path)
            pyarmor_converter([d for d in os.listdir(path) if d not in exclude_file_dir], path)
            
            
pyarmor_converter([d for d in os.listdir('.') if d not in exclude_file_dir], os.getcwd())



