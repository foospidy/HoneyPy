# Installing HoneyPy

## System Requirements

- Linux
- Python 2.7

## Downloading

__NOTE:__ You can run HoneyPy from any directory on your file system. For the purposes of this documentaiton `/opt/HoneyPy` will be referenced.

Download the latest release from [https://github.com/foospidy/HoneyPy/releases/latest](https://github.com/foospidy/HoneyPy/releases/latest).

Example script:

```bash
#!/usr/bin/env bash

cd /opt
latest=`curl https://raw.githubusercontent.com/foospidy/HoneyPy/master/VERSION`
curl -L -o HoneyPy.tar.gz https://github.com/foospidy/HoneyPy/archive/${latest}.tar.gz
tar -xzf HoneyPy.tar.gz
mv HoneyPy-${latest} HoneyPy
```

Or you can clone the repository from Github with from [https://github.com/foospidy/HoneyPy.git](https://github.com/foospidy/HoneyPy.git).

Example script:

```bash
#!/usr/bin/env bash

cd /opt
git clone https://github.com/foospidy/HoneyPy.git
```

__WARNING:__ Cloning the repository will pull any development changes that may be a work in progress. As a result you may experience bugs or breaks. Current build status [![Build Status](https://travis-ci.org/foospidy/HoneyPy.svg?branch=master)](https://travis-ci.org/foospidy/HoneyPy)

## Dependencies

Before you can run HoneyPy you must ensure you have all required Python module dependencies installed. For a list of the dependencies see the [requirements.txt](https://raw.githubusercontent.com/foospidy/HoneyPy/master/requirements.txt) file. It is recommended to install dependencies using [pip](https://pypi.python.org/pypi/pip).

__NOTE:__ Installing dependencies on your base system will require root access. Recommended alternatives to install dependencies and run HoneyPy are [Virtualenv](https://virtualenv.pypa.io/) or [pipenv](https://github.com/pypa/pipenv) as described below. Both create isolated Python environments, which may be beneficial if you are running other Python scripts and their dependencies on the same system. However, if you are using a dedicated system, or even a container, to run HoneyPy, then Virtualenv/pipenv may not be necessary.


To install dependencies globally with pip and the requirements.txt file run:

```bash
cd /opt/HoneyPy
sudo pip install -r requirements.txt
```

To install dependencies using Virtualenv run:
```bash
cd /opt/HoneyPy
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

To install dependencies using pipenv run:
```bash
cd /opt/HoneyPy
pipenv install
pipenv shell
```

__NOTE:__ Please keep in mind that you have to activate the Virtualenv/pipenv before using HoneyPy.

## Running

There are several options for how you can launch and run HoneyPy, [console](#console) mode, [daemon](#daemon) mode, and [on boot](#on-boot) (also daemon mode).

__WARNING:__ It is highly recommended to __NOT__ run HoneyPy as root. It is recommended to create a dedicated user account for running HoneyPy.

### Console

You can run HoneyPy in console mode. From any terminal run:

```bash
cd /opt/HoneyPy
./Honey.py
```

__NOTE:__ You can leverage the [screen](https://www.gnu.org/software/screen/manual/screen.html#Overview) utility to run HoneyPy in console mode. Using screen will keep HoneyPy running even if you lose your terminal connection.

Example creating a screen session for HoneyPy:

```bash
screen -S MyHoneyPyConsole
```

Example recovering the HoneyPy screen session:

```bash
screen -r MyHoneyPyConsole
```

### Daemon

You can run HoneyPy as a daemon process. From any terminal run:

```bash
/opt/Honey.py -d &
```

### On Boot

Configuring your system to launch HoneyPy on system boot will depend on what version of Linux you are using. Most likely you will need a startup script. HoneyPy comes with an example startup script, `honeypyd`, which has been tested on Debian (Jessie). You can find this script in the `/opt/HoneyPy/etc/` directory. View the top section of the stript for instructions. To view this script on Github, [click here](https://raw.githubusercontent.com/foospidy/HoneyPy/master/etc/honeypyd).
