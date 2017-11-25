HoneyPy
=======

[![Build Status](https://travis-ci.org/foospidy/HoneyPy.svg?branch=master)](https://travis-ci.org/foospidy/HoneyPy)

A low interaction honeypot with the capability to be more of a medium interaction honeypot. HoneyPy is written in Python and is intended to be easy to: deploy, extend funtionality with plugins, and apply custom configurations. The level of interaction is determined by the functionality of a plugin. Plugins can be created to emulate UDP or TCP based services to provide more interaction. All activity is logged to a file by default, but posting honeypot activity to Twitter or a web service endpoint can be configured as well. Examples:  

Live HoneyPy data posted to 
- Twitter: https://twitter.com/HoneyPyLog
- Web service endpoint and displayed via the HoneyDB web site: https://riskdiscovery.com/honeydb

note: HoneyPy has primarily been tested and run on Debian with Python 2.7.9.

**Pull requests are welcome!** If you would like to create new plugins or improve existing plugins, please do. 

### Documentation

The main documentation can be found at the [HoneyPy Docs](https://honeypy.readthedocs.io/en/latest/) site.
