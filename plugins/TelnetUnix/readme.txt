#### Description
A telnet service implemented with the Twisted telnet protocol.

#### Dependencies
This plugin requires clilib.
https://github.com/foospidy/clilib

#### Install on Ubuntu
apt-get install python-setuptools
git clone https://github.com/foospidy/clilib.git
cd clilib
python setup.py bdist_egg
easy_install -Z dist/clilib-0.0.0-py2.7.egg
