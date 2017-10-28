# Installing HoneyPy

## 1. Download HoneyPy

__NOTE:__ You can run HoneyPy from any directory on your file system. For the purposes of this documentaiton `/opt/HoneyPy` will be referenced.

Download the latest release from [https://github.com/foospidy/HoneyPy/releases/latest](https://github.com/foospidy/HoneyPy/releases/latest).

Example script:

```
#!/usr/bin/env bash

cd /opt
latest=`curl https://raw.githubusercontent.com/foospidy/HoneyPy/master/VERSION`
curl -L -o HoneyPy.tar.gz https://github.com/foospidy/HoneyPy/archive/${latest}.tar.gz
tar -xzf HoneyPy.tar.gz
mv HoneyPy-${latest} HoneyPy
```

Or you can clone the repository from Github with from [https://github.com/foospidy/HoneyPy.git](https://github.com/foospidy/HoneyPy.git).

Example script:

```
#!/usr/bin/env bash

cd /opt
git clone https://github.com/foospidy/HoneyPy.git
```

__WARNING:__ Cloning the repository will pull any development changes that may be a work in progress. This could result you may experience bugs or breaks.
