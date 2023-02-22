# pip install -U --force-reinstall Cython

import pyximport
pyximport.install(pyimport=True,language_level=3)

#import pyximportcpp;
#pyximportcpp.install()

import my_module
