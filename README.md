# HoneyPy 🍯

[![Build Status](https://travis-ci.org/foospidy/HoneyPy.svg?branch=master)](https://travis-ci.org/foospidy/HoneyPy)
[![Documentation Status](https://readthedocs.org/projects/honeypy/badge/?version=latest)](http://honeypy.readthedocs.io/en/latest/?badge=latest)

A low interaction honeypot with the capability to be more of a medium interaction honeypot.

**Project status:**

* No longer in active development.
* Repository will remain for anyone wanting to use or contribute to HoneyPy.
* I recommend using the honeydb-agent instead: https://honeydb-agent-docs.readthedocs.io/

**Description**

HoneyPy is written in Python2 and is intended to be easy to:
* install and deploy
* extend with plugins and loggers
* run with custom configurations

Feel free to follow the [QuickStart Guide](https://honeypy.readthedocs.io/en/latest/quickstart) to dive in directly.
The main documentation can be found at the [HoneyPy Docs](https://honeypy.readthedocs.io/en/latest/) site.

Live HoneyPy data gets posted to:
* Twitter: https://twitter.com/HoneyPyLog
* Web service endpoint and displayed via the HoneyDB web site: https://riskdiscovery.com/honeydb

**Leave an issue or feature request!** Use the GitHub issue tracker to tell us whats on your mind.

**Pull requests are welcome!** If you would like to create new plugins or improve existing ones, please do.

__NOTE:__ HoneyPy has primarily been tested and run on Debian and Ubuntu using Python 2.7.9.


## Overview

HoneyPy comes with a lot of plugins included. The level of interaction is determined by the functionality of the used
plugin. Plugins can be created to emulate UDP or TCP based services to provide more interaction. All activity is logged
to a file by default, but posting honeypot activity to Twitter or a web service endpoint can be configured as well.

**Examples**:
* Plugins:
    * ElasticSearch
    * SIP
    * etc.

* Loggers:
    * HoneyDB
    * Twitter
    * etc.
