HoneyPy
=======

A low interaction honeypot. Coded in Python and intended to be a very basic honeypot that is easy to deploy. By default HoneyPy simply opens ports to listen on, and only logs connections and data sent to it. It only responds with a message specified in the service config file for each service. Custom "scripts" or service emulators can be created to listen on those ports to provide more interaction. See the secton on custom service emulation below for more information.

#### Usage
**You should not run HoneyPy as root!** It is recommended to use a dedicated account to run under. HoneyPy is developed and run on Debain. There's no reason why it should not work on other Linux/Unix flavors as long as all Python dependencies are installed.

Run in console mode: `python Honey.py`

In console mode type 'help' for a list of command options.

Run in deamon mode: `python Honey.py -d &`

#### Service Config Files
There are several configuration service.* files in the etc directory. The service config file is used to define what ports (services) you want to run on your honey pot. By default HoneyPy will use the service.cfg file. Each service defined in the file has an "enabled" option. This option can be set to Yes or No to determine which services run on start. You can also use one of the other service config files, or create your own. Initially the service.cfg file is the same as service.all.cfg. To use one of the other files simply copy the file over service.cfg. For example:

`cp services.windows.iis.cfg service.cfg`

If you want to revert back to the default service config file simply run

`cp service.all.cfg service.cfg`

#### Running Services on Low Ports
While you should not run HoneyPy with the root user, this means HoneyPy will not be able to listen on ports 1 through 1024. As a work around you can use implement port redirection with IPTables. If you're not familiar with using IPTables you can try using ipt-kit (https://github.com/foospidy/ipt-kit). You will need to run ipt-kit as root to modify IPTables. Once the redirection rules are in place you won't need to run HoneyPy as root for low ports.

As an example, if you want HoneyPy to listen for telnet connections on port 23, choose a port above 1024. Edit the HoneyPy service config file to have telnet run on a high port (e.g. 2300). Then use ipt-kit to redirect 23 to 2300, example commands:

if root user:

`\#./ipt\_set_tcp 23 2300`

or if using sudo:

`$sudo ./ipt\_set_tcp 23 2300`

#### Custom Service Emulation
HoneyPy now supports custom service emulators. Service emulators can make the honeypot look more like a real system in order to invoke more interaction and capture more attack data. The emulator is a Python module that is loaded on start. HonePy simply opens a socket and hands it off to the service emulator. There are example service emulators included in the lib directory. These will be improved, and more added, in the future. To enable an emulator add the file name to the script parameter in the service config file. Example:

`[ftp]`

`port     = 21`

`response = cookie!`
comment  = Possible ftp attacks 
enabled  = Yes
script   = honeypy\_ftp_proftpd.py
`

#### Twitter API Support
Post CONNECT events to Twitter. Requires python twitter library, https://github.com/sixohsix/twitter. 

To install on Debian:

`apt-get install python-pip`

`pip install twitter`

Also required is a Twitter account and setting up a Twitter app:
https://dev.twitter.com/apps/new

Example Twitter account, @HoneyPyLog - https://www.twitter.com/HoneyPyLog

