import sys, os
from cx_Freeze import setup,Executable

includefiles = []
includes = []
excludes = ['Tkinter']
packages = []

base=None
if sys.platform=="win32":
    base="Win32GUI"
else:
    base="Win64GUI"
    
setup(
    name = 'Radistart2',
    version = '2.01',
    description = 'Radistart2 mit cx_freeze',
    author = 'S1l3nz',
    author_email = 's1l3nzcodes@googlemail.com.com',
    options = {'build_exe': {'excludes':excludes,'packages':packages,'include_files':includefiles}}, 
    executables = [Executable('Radistart2.py', base=base)]
)
