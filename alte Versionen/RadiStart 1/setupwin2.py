from distutils.core import setup
import py2exe, os, sys

sys.argv.append('py2exe')

ICON='E:/RadiStart/RadiStart.ico'
setup(
    name='RadiStart',
    version='0.05',
    author='Florian Becker',
    
    options={'py2exe':{'bundle_files':3, 'compressed':True}},
    windows=[{'script':'E:/RadiStart/RadiStart.py','icon_resources':[(1,ICON)]}],
    zipfile=None
    )

