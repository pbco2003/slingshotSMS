from distutils.core import setup
import py2exe

setup(console=['agilesms.py'], data_files=['README', 'agilesms.cfg'])