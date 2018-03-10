# Quickstart

__WARNING:__ Only do this if you know what you are doing! All the dangerous traps - like running
a honeypot as root or installing packages globally - are explained in the upcoming sections.

First you need a local copy of the repository:

```shell
git clone https://github.com/foospidy/HoneyPy.git
git checkout tags/<insert_latest_release_tag> -b latest
```

Install and run:

```shell
pipenv install && pipenv run ./HoneyPy
```

Check out the config files and stick to `.cfg`-syntax when changing them:

```shell
cd etc/
vim *.cfg
```
