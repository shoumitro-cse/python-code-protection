[shoumitro@shoumitro-pc code_protection]$ python
Python 3.10.8 (main, Nov  1 2022, 14:18:21) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
>>> import pyximport; #pyximport is a part of cython.
>>> pyximport.install()
(None, <pyximport.pyximport.PyxImporter object at 0x7f6807354850>)
>>> 
>>> import mymodule
/home/shoumitro/.local/lib/python3.10/site-packages/Cython/Compiler/Main.py:369: FutureWarning: Cython directive 'language_level' not set, using 2 for now (Py2). This will change in a later release! File: /home/shoumitro/Documents/FR/test/pyc_converter/code_protection/mymodule.pyx
  tree = Parsing.p_module(s, pxd, full_module_name)
('cython fun calling', 12)
('cython fun calling', 12)
756.0
('cython fun calling', 12)
0.0
>>> 
>>> 
>>> pyximport.install(pyimport=True,language_level=3)
(<pyximport.pyximport.PyImporter object at 0x7f680484f760>, None)
>>> 
>>> 
>>> import mymodule
>>> 
>>> exit()

