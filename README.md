HoneyPy
=======

A low interaction honeypot. Coded in Python and intended to be a very basic honeypot that is easy to deploy. More features will be added on in time.

Usage:

Run in console mode: python Honey.py

In console mode type 'help' for a list of command options.

Run in deamon mode: python Honey.py -d &

#### StatsD Support
Send CONNECT, RX, and ERROR events to StatsD. More on StatsD, https://github.com/etsy/statsd

#### Twitter API Support
Post CONNECT events to Twitter. Requires python twitter library, https://github.com/sixohsix/twitter. 

To install on Debian:
apt-get install python-pip
pip install twitter

Also required is a Twitter account and setting up a Twitter app:
https://dev.twitter.com/apps/new

Example Twitter account, @HoneyPyLog - https://www.twitter.com/HoneyPyLog

