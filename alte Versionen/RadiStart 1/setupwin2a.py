from distutils.core import setup
import py2exe, os, sys

sys.argv.append('py2exe')

ICON='E:/UKSH/RadiStart/RadiStart.ico'
setup(
    name='RadiStart',
    version='0.8',
    author='Florian Becker',
    
    options={'py2exe':{'bundle_files':3, 'compressed':True}},
    windows=[{'script':'E:/UKSH/RadiStart/RadiStart.py','icon_resources':[(1,ICON)]}],
    zipfile=None
    )

