from distutils.core import setup
import py2exe, os, sys, sip
import PyQt4
from PyQt4 import *

sys.argv.append('py2exe')

ICON='E:/Radistart_Dev/RadistartQt/RadiStart.ico'
setup(
    name='RadiStart',
    version='2.01',
    author='Florian Becker',
    
    options={'py2exe':{'bundle_files':3,
                       'compressed':True,
                       'includes':["sip", "PyQt4", "PyQt4.QtNetwork"]}},

    windows=[{'script':'E:/Radistart_Dev/RadistartQt/radistart2.py','icon_resources':[(1,ICON)]}],
    zipfile=None
    )

