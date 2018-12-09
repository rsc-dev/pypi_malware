# openssl-python

This tool is a command line interface to OpenSSL, written with Python3.
It permits encrypting/decrypting files, as well as generating RSA keys, encrypting private RSA keys, signing files using an RSA key, and also verifying signatures using RSA.  
  
## Dependencies
  
Before running this tool, the following dependency must be installed, as well as being on the path:

* openssl  
  
Usually, this dependency exists by default in most of the supported platforms(see below). In case it doesn't, try consulting the official [OpenSSL documentation](https://www.openssl.org/docs/); or consult your operating system' documentation on how to install new software. 
  
## Usage

To launch openssl-python tool, just download the source code, and run the following command:  
```
python3 main.py
```
Or alternatively, if python is in the path, run the following commands:
```
chmod +x main.py
./main.py
```
  

## Platform support

This tool was initially developed and tested on Linux systems, so it does also support Unix-like systems: BSDs, Mac OS...  
Windows support though is not guaranteed.
