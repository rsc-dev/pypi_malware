#!/usr/bin/env python3

import sys
import os

__author__ = "Youssef Seddik"
__version__ = '0.1'
__license__ = 'GNU GPLv3'

def menu():
    """
    A simple menu to choose operations from.
    """
    print("     ======OpenSSL Python Script======     ")
    print("|  1)  Encrypt a File                     |")
    print("|  2)  Decrypt a File                     |")
    print("|  3)  Generate an RSA key                |")
    print("|  4)  Encrypt an RSA private key         |")
    print("|  5)  Sign a file using an RSA key       |")
    print("|  6)  Verify signature using RSA key     |")
    print("|  99) Exit                               |")
    print("|_________________________________________|")

def main():
    """
    Overall, this is a simple command line interface to OpenSSL.
    """
    while True:
        menu()
        a = int(input(">_ "))
        if a == 1:
            flin = str(input("Enter input file name: "))
            try:
                tst = open(flin, 'r')
            except IOError as er:
                print(er)
                break
                sys.exit()
            finally:
                flout = str(input("Enter output file name: "))
                cmd = "openssl enc -e -aes-256-cbc -in " + flin  + " -out "\
                + flout
                os.system(cmd)
                print()
                print("Operation done successfully!")
                print()
        elif a == 2:
            flin = str(input("Enter input file name: "))
            try:
                tst = open(flin, 'r')
            except IOError as er:
                print(er)
                sys.exit()
            finally:
                flout = str(input("Enter output file name: "))
                cmd = "openssl enc -d -aes-256-cbc -in " + flin  + " -out "\
                + flout
                os.system(cmd)
                print()
                print("Operation done successfully!")
                print()
        elif a == 3:
            size = int(input("Choose the key size [1024/2048/4096] bits: "))
            if size == 1024 or size == 2048 or size == 4096:
                out1 = str(input("Enter the output filename\
 for the private key: "))
                out2 = str(input("Enter the output filename for\
 the public key: "))
            else:
                print("Invalid Size!")
            cmd = "openssl genrsa -out " + out1 + " " + str(size)
            os.system(cmd)
            cmd = "openssl rsa -in " + out1 + " -pubout -out " + out2
            os.system(cmd)
            print()
            print("Operation done successfully!")
            print()
        elif a == 4:
            flin = str(input("Enter the private key file name: "))
            try:
                tst = open(flin, 'r')
            except IOError as er:
                print(er)
                break
                sys.exit()
            finally:
                cipher = str(input("Choose which cipher to use[des/des3]: "))
                if cipher == "des" or cipher == "des3":
                    flout = str(input("Enter the output filename: "))
                    cmd = "openssl rsa -in " + flin + " -" + cipher + " -out "\
                    + flout
                    os.system(cmd)
                    print()
                    print("Operation done successfully!")
                    print()
        elif a == 5:
            keyin = str(input("Enter the RSA private key filename: "))
            flin = str(input("Enter the file name to sign: "))
            try:
                tst1 = open(keyin, 'r')
                tst2 = open(flin, 'r')
            except IOError as er:
                print(er)
                break
                sys.exit()
            finally:
                flout = str(input("Enter the output filename: "))
                cmd = "openssl dgst -out " + flout + " -sign " + keyin + " "\
                + flin
                os.system(cmd)
                print()
                print("Operation done successfully!")
                print()
        elif a == 6:
            keyin = str(input("Enter the RSA public key filename: "))
            sigin = str(input("Enter the signature filename: "))
            try:
                tst1 = open(keyin, 'r')
                tst2 = open(sigin, 'r')
            except IOError as er:
                print(er)
                break
                sys.exit()
            finally:
                flout = str(input("Enter the output filename to write\
 the imprint to it: "))
                cmd = "openssl rsautl -verify -in " + sigin\
                + " -pubin -inkey " + keyin + " -out " + flout
                os.system(cmd)
                print()
                print("Operation done successfully!")
                print()
        elif a == 99:
            print("Bye")
            break
            sys.exit()
        else:
            print("Please enter a valid choice.")

