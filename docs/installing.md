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

__WARNING:__ Cloning the repository will pull any development changes that may be a work in progress. As a result you may experience bugs or breaks.

## Dependencies

Before you can run HoneyPy you must ensure you have all required Python module dependencies installed. For a list of the dependencies see the [requirements.txt](https://raw.githubusercontent.com/foospidy/HoneyPy/master/requirements.txt) file. It is recommended to install dependencies using [pip](https://pypi.python.org/pypi/pip).

To install dependencies with pip and the requirements.txt file run:

```bash
cd /opt/HoneyPy
sudo pip install -r reqirements.txt
```

## Running

There are several options in how you can launch and run HoneyPy.

### Console

You can run HoneyPy in console mode. From any terminal run:

 ```bash
 cd /opt/HoneyPy
 ./Honey.py
 ```

### Daemon

You can run HoneyPy as a daemon process. From any terminal run:

 `/opt/Honey.py -d &`

### On Boot
