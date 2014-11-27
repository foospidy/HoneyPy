HoneyPy
=======

A low interaction honeypot. Coded in Python and intended to be a very basic honeypot that is easy to deploy. More features will be added on in time.

#### Usage

Run in console mode: python Honey.py

In console mode type 'help' for a list of command options.

Run in deamon mode: python Honey.py -d &

#### Service Config Files
There are several configuration service.* files in the etc directory. The service config file is used to define what ports (services) you want to run on your honey pot. By default HoneyPy will use the service.cfg file. Each service defined in the file has an "enabled" option. This option can be set to Yes or No to determine which services run on start. You can also use one of the other service config files, or create your own. Initially the service.cfg file is the same as service.all.cfg. To use one of the other files simply copy the file over service.cfg. For example:

cp services.windows.iis.cfg service.cfg

If you want to revert back to the default service config file simply run

cp service.all.cfg service.cfg

#### Twitter API Support
Post CONNECT events to Twitter. Requires python twitter library, https://github.com/sixohsix/twitter. 

To install on Debian:

apt-get install python-pip

pip install twitter

Also required is a Twitter account and setting up a Twitter app:
https://dev.twitter.com/apps/new

Example Twitter account, @HoneyPyLog - https://www.twitter.com/HoneyPyLog

