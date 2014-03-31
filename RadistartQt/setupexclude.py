from distutils.core import setup
import py2exe, os, sys, sip
import PyQt4
from PyQt4 import *

sys.argv.append('py2exe')

ICON='E:/RadistartQt/RadiStart.ico'
setup(
    name='RadiStart',
    version='0.05',
    author='Florian Becker',
    
    options={'py2exe':{'bundle_files':3,
                       'compressed':True,
                       'excludes':["config"],
                       'includes':["sip", "PyQt4", "PyQt4.QtNetwork"]}},

    windows=[{'script':'E:/RadistartQt/Radistart.py','icon_resources':[(1,ICON)]}],
    zipfile=None
    )

