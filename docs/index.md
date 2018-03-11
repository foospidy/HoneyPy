# Welcome to HoneyPy Docs!

[![Build Status](https://travis-ci.org/foospidy/HoneyPy.svg?branch=master)](https://travis-ci.org/foospidy/HoneyPy)
[![Documentation Status](https://readthedocs.org/projects/honeypy/badge/?version=latest)](http://honeypy.readthedocs.io/en/latest/?badge=latest)


**A low interaction honeypot with the capability to be more of a medium interaction honeypot.**

HoneyPy is written in Python2 and is intended to be easy to:
* install and deploy
* extend with plugins and loggers
* run with custom configurations

HoneyPy comes with a lot of plugins included. The level of interaction is determined by the functionality of the used
plugin. Plugins can be created to emulate UDP or TCP based services to provide more interaction. All activity is logged
to a file by default, but posting honeypot activity to Twitter or a web service endpoint can be configured as well.


Feel free to follow the [QuickStart Guide](https://honeypy.readthedocs.io/en/latest/quickstart) to dive in directly.

__NOTE:__ HoneyPy has primarily been tested and run on Debian and Ubuntu using Python 2.7.9.
