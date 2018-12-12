# PyPI Malware

## Info
PyPI is a well known Python packages repository. 
Everyone can upload modules to PyPI without any security checks or audits.

Legacy package format is based on distutils module and requires setup.py script.
This script is run on local machine once package is been installed.

## How to verify
```bash
pip freeze | grep "distrib\|djanga\|easyinstall\|junkeldat\|libpeshka\|mumpy\|mybiubiubiu\|nmap-python\|openvc\|python-ftp\|pythonkafka\|python-mongo\|python-mysql\|python-mysqldb\|python-openssl\|python-sqlite\|smb\|virtualnv"
```

## How to be secure
* use ["wheels"](https://pythonwheels.com/)
* always double check package name
* do not run pip as root/admin
* use pip [hash-checking mode](https://pip.pypa.io/en/stable/reference/pip_install/#hash-checking-mode)

## Malware packages
<table style="width: 700px;">
<tbody>
<tr>
<td style="width: 110px;"><strong>Package</strong></td>
<td style="width: 131px;"><strong>Versions</strong></td>
<td style="width: 27px;"><strong>Remote Host</strong></td>
<td style="width: 131px;"><strong>Info</strong></td>
</tr>
<tr>
<td style="width: 110px;"><a href="https://github.com/rsc-dev/pypi_malware/tree/master/malware/distrib">distrib</a></td>
<td style="width: 131px;">distrib-0.1</td>
<td style="width: 27px;">packageman.comlu.com</td>
<td style="width: 131px;">Sends hostname + OS environment variables to remote host.</td>
</tr>
<tr>
<td style="width: 110px;" rowspan="3"><a href="https://github.com/rsc-dev/pypi_malware/tree/master/malware/djanga">djanga</a></td>
<td style="width: 131px;">djanga-0.1</td>
<td style="width: 27px;" rowspan="3">145.249.104.71</td>
<td style="width: 131px;" rowspan="3">Linux malware. Downloads executable and adds it to .bashrc.</td>
</tr>
<tr>
<td style="width: 131px;">djanga-0.2</td>
</tr>
<tr>
<td style="width: 131px;">djanga-0.3</td>
</tr>
<tr>
<td style="width: 110px;" rowspan="6"><a href="https://github.com/rsc-dev/pypi_malware/tree/master/malware/easyinstall">easyinstall</a></td>
<td style="width: 131px;">easyinstall-37.0.0</td>
<td style="width: 27px;" rowspan="6">145.249.104.71</td>
<td style="width: 131px;" rowspan="6">Linux malware. Downloads executable and adds it to .bashrc.</td>
</tr>
<tr>
<td style="width: 131px;">easyinstall-39.0.0</td>
</tr>
<tr>
<td style="width: 131px;">easyinstall-39.1.0</td>
</tr>
<tr>
<td style="width: 131px;">easyinstall-40.0.0</td>
</tr>
<tr>
<td style="width: 131px;">easyinstall-41.0.0</td>
</tr>
<tr>
<td style="width: 131px;">easyinstall-42.0.0</td>
</tr>
<tr>
<td style="width: 110px;"><a href="https://github.com/rsc-dev/pypi_malware/tree/master/malware/junkeldat">junkeldat</a></td>
<td style="width: 131px;">junkeldat-1.0</td>
<td style="width: 27px;">www.dl01.pwnz.org</td>
<td style="width: 131px;">Seems broken.</td>
</tr>
<tr>
<td style="width: 110px;" rowspan="5"><a href="https://github.com/rsc-dev/pypi_malware/tree/master/malware/libpeshka">libpeshka</a></td>
<td style="width: 131px;">libpeshka-0.2</td>
<td style="width: 27px;" rowspan="5">145.249.104.71</td>
<td style="width: 131px;" rowspan="5">Linux malware. Downloads executable and adds it to .bashrc.</td>
</tr>
<tr>
<td style="width: 131px;">libpeshka-0.3</td>
</tr>
<tr>
<td style="width: 131px;">libpeshka-0.4</td>
</tr>
<tr>
<td style="width: 131px;">libpeshka-0.5</td>
</tr>
<tr>
<td style="width: 131px;">libpeshka-0.6</td>
</tr>
<tr>
<td style="width: 110px;"><a href="https://github.com/rsc-dev/pypi_malware/tree/master/malware/mumpy">mumpy</a></td>
<td style="width: 131px;">mumpy-0.1</td>
<td style="width: 27px;">packageman.comlu.com</td>
<td style="width: 131px;">Sends hostname + OS environment variables to remote host.</td>
</tr>
<tr>
<td style="width: 110px;" rowspan="6"><a href="https://github.com/rsc-dev/pypi_malware/tree/master/malware/mybiubiubiu">mybiubiubiu</a></td>
<td style="width: 131px;">mybiubiubiu-0.1.0</td>
<td style="width: 27px;" rowspan="6">http://snowty.cn</td>
<td style="width: 131px;" rowspan="6">Uploads some data (i.e. username, hostname, ip, etc.) to remote host.</td>
</tr>
<tr>
<td style="width: 131px;">mybiubiubiu-0.1.1</td>
</tr>
<tr>
<td style="width: 131px;">mybiubiubiu-0.1.2</td>
</tr>
<tr>
<td style="width: 131px;">mybiubiubiu-0.1.3</td>
</tr>
<tr>
<td style="width: 131px;">mybiubiubiu-0.1.4</td>
</tr>
<tr>
<td style="width: 131px;">mybiubiubiu-0.1.6</td>
</tr>
<tr>
<td style="width: 110px;"><a href="https://github.com/rsc-dev/pypi_malware/tree/master/malware/nmap-python">nmap-python</a></td>
<td style="width: 131px;">nmap-python-0.6.1</td>
<td style="width: 27px;">http://openvc.org</td>
<td style="width: 131px;">Uploads some data (i.e. username, hostname, ip, etc.) to remote host.</td>
</tr>
<tr>
<td style="width: 110px;"><a href="https://github.com/rsc-dev/pypi_malware/tree/master/malware/openvc">openvc</a></td>
<td style="width: 131px;">openvc-1.0.0</td>
<td style="width: 27px;">http://openvc.org</td>
<td style="width: 131px;">Uploads some data (i.e. username, hostname, ip, etc.) to remote host.</td>
</tr>
<tr>
<td style="width: 110px;"><a href="https://github.com/rsc-dev/pypi_malware/tree/master/malware/python-ftp">python-ftp</a></td>
<td style="width: 131px;">python-ftp-2.4</td>
<td style="width: 27px;">http://us.dslab.pw</td>
<td style="width: 131px;">Uploads username, hostname, ip to remote host.</td>
</tr>
<tr>
<td style="width: 110px;"><a href="https://github.com/rsc-dev/pypi_malware/tree/master/malware/pythonkafka">pythonkafka</a></td>
<td style="width: 131px;">pythonkafka-1.3.5</td>
<td style="width: 27px;">http://us.dslab.pw</td>
<td style="width: 131px;">Uploads username, hostname, ip to remote host.</td>
</tr>
<tr>
<td style="width: 110px;"><a href="https://github.com/rsc-dev/pypi_malware/tree/master/malware/python-mongo">python-mongo</a></td>
<td style="width: 131px;">python-mongo-0.2.0</td>
<td style="width: 27px;">http://us.dslab.pw</td>
<td style="width: 131px;">Uploads username, hostname, ip to remote host.</td>
</tr>
<tr>
<td style="width: 110px;"><a href="https://github.com/rsc-dev/pypi_malware/tree/master/malware/python-mysql">python-mysql</a></td>
<td style="width: 131px;">python-mysql-1.0.0</td>
<td style="width: 27px;">http://mysql.openvc.org</td>
<td style="width: 131px;">Uploads username, hostname, ip to remote host.</td>
</tr>
<tr>
<td style="width: 110px;"><a href="https://github.com/rsc-dev/pypi_malware/tree/master/malware/python-mysqldb">python-mysqldb</a></td>
<td style="width: 131px;">python-mysqldb-2.4</td>
<td style="width: 27px;">http://us.dslab.pw</td>
<td style="width: 131px;">Uploads username, hostname, ip to remote host.</td>
</tr>
<tr>
<td style="width: 110px;"><a href="https://github.com/rsc-dev/pypi_malware/tree/master/malware/python-openssl">python-openssl</a></td>
<td style="width: 131px;">python-openssl-0.1</td>
<td style="width: 27px;">http://openvc.org</td>
<td style="width: 131px;">Uploads username, hostname, ip to remote host.</td>
</tr>
<tr>
<td style="width: 110px;"><a href="https://github.com/rsc-dev/pypi_malware/tree/master/malware/python-sqlite">python-sqlite</a></td>
<td style="width: 131px;">python-sqlite-2.4</td>
<td style="width: 27px;">http://us.dslab.pw</td>
<td style="width: 131px;">Uploads username, hostname, ip to remote host.</td>
</tr>
<tr>
<td style="width: 110px;"><a href="https://github.com/rsc-dev/pypi_malware/tree/master/malware/smb">smb</a></td>
<td style="width: 131px;">smb-2.4</td>
<td style="width: 27px;">http://us.dslab.pw</td>
<td style="width: 131px;">Uploads username, hostname, ip to remote host.</td>
</tr>
<tr>
<td style="width: 110px;"><a href="https://github.com/rsc-dev/pypi_malware/tree/master/malware/virtualnv">virtualnv</a></td>
<td style="width: 131px;">virtualnv-0.1.1</td>
<td style="width: 27px;">packageman.comlu.com</td>
<td style="width: 131px;">Sends hostname + OS environment variables to remote host.</td>
</tr>
</tbody>
</table>