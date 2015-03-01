HoneyPy
=======

The latest updates significantly change how HoneyPy works, this readme is obsolete, it will be updated soon.

A low interaction honeypot with the capability to be more of a medium interaction honeypot. Coded in Python and intended to be a very basic honeypot that is easy to deploy. HoneyPy is now based on plugins, and the level of interaction is based on what plugins are configured to run. The default plugins are low interaction and all activity is logged. Plugins can be enhanced or created to emulate services to provide more interaction. 

#### Usage
**You should not run HoneyPy as root!** It is recommended to use a dedicated account to run under. HoneyPy is developed and run on Debain. There's no reason why it should not work on other Linux/Unix flavors as long as all Python dependencies are installed.

##### Console Mode
Run in console mode: `python Honey.py`

In console mode services do not automatically start, use the `start` command. Type the `help` command for a list of command options. Example of the console screen:

```
                                ___       
  /\  /\___  _ __   ___ _   _  / _ \_   _ 
 / /_/ / _ \| '_ \ / _ \ | | |/ /_)/ | | |
/ __  / (_) | | | |  __/ |_| / ___/| |_| |
\/ /_/ \___/|_| |_|\___|\__, \/     \__, |
                        |___/       |___/ 


[HoneyPy v0.1.0 Copyright (c) 2013-2015. foospidy]

HoneyPy Console. For help type 'help'.
HoneyPy>start
8 service(s) started!
HoneyPy>
```

##### Deamon Mode

In deamon mode all configured services will automatically start and listen for connections.

Run in deamon mode: `python Honey.py -d &`

#### Service Config Files
In the `etc` directory there is a `service.cfg` file, this is the file HoneyPy uses to launch services. There are several example service configuration files located in the `etc/examples` directory. The service config file is used to define service names, ports, and plugins to run on your honeypot. Each service defined in the file has an "enabled" option. This option can be set to Yes or No to determine which services run on start. You can also use one of the example config files, or create your own. To use one of the other files simply copy the file over service.cfg. For example:

`cp examples/services.windows_iis.example service.cfg`

If you want to revert back to the default service config file simply run

`cp examples/service.default.example service.cfg`

#### Running Services on Low Ports
While you should not run HoneyPy with the root user, this means HoneyPy will not be able to listen on ports 1 through 1024. As a work around you can use implement port redirection with IPTables. If you're not familiar with using IPTables you can try using ipt-kit (https://github.com/foospidy/ipt-kit). You will need to run ipt-kit as root to modify IPTables. Once the redirection rules are in place you won't need to run HoneyPy as root for low ports.

As an example, if you want HoneyPy to listen for telnet connections on port 23, choose a port above 1024. Edit the HoneyPy service config file to have telnet run on a high port (e.g. 2300). Then use ipt-kit to redirect 23 to 2300, example commands:

if root user:

`#./ipt_set_tcp 23 2300`

or if using sudo:

`$sudo ./ipt_set_tcp 23 2300`

#### Custom Service Emulation
HoneyPy now uses the concept of plugins for custom service emulators. Service emulators can make the honeypot look more like a real system in order to invoke more interaction and capture more attack data. The emulator is a Python module that is loaded on start. HonePy simply opens a socket and hands it off to the service emulator. There are example service emulators included in the plugins directory. These will be improved, and more added, in the future. Example:

```
[Echo]
plugin      = Echo
port        = tcp:10007
description = Echo back data received via tcp.
enabled     = Yes
```

#### Creating Custom Service Emulators
Hopefully creating new plugins is now easy. HoneyPy takes care of sending/receiving data and logging, all you have to do is write the custom protocol/logic. The service emulators in the plugins directory can be used as templates to create new emulators.

Example:
https://github.com/foospidy/HoneyPy/blob/master/plugins/HashCountRandom/HashCountRandom.py

There are three sections to edit: custom import, custom protocol, and custom functions. To keep the template well organized, you should only make modifciaitons in the designated sections, note the comments that denote each section.

Example of custom import. Import the Python modules you need:
```
### START CUSTOM IMPORT
import time
import os
import md5
### END CUSTOM IMPORT
```

Next, use the custom protocol section to write your logic. use the `self.tx()` function to transfer (send) data to the socket, and use the `self.rx()` function to receive data from the socket.

```
### START CUSTOM PROTOCOL ###########################################################
self.tx('ACCEPT_CONN: ' + str(self.remote_host) + ':' + str(self.remote_port) + '\n')
count = 0

while True:
	count = count + 1
	self.tx(self.md5sum(count) + ':' + str(os.urandom(99)) + '\n')
	self.rx()
	time.sleep(1)

### END CUSTOM PROTOCOL #############################################################
```

Add custom functions as needed at the bottom. All functions must have the first parameter be `self`. When you call custom functions from the custom protocol section you must prefix them with `self.`, for example: `self.md5sum('test')`

```
### START CUSTOM FUNCTIONS ##########################################################
def md5sum(self, data):
	m = md5.new()
	m.update(str(data))
	return m.hexdigest()

### END CUSTOM FUNCTIONS ############################################################
```

#### Dependencies

##### Twisted
HoneyPy is now completely dependent on the Twisted. Learn more about Twisted here https://twistedmatrix.com.

To Install on Debian:

`apt-get install python-twisted`

##### Twitter API Support
Post CONNECT events to Twitter. Requires python twitter library, https://github.com/sixohsix/twitter. 

To install on Debian:

`apt-get install python-pip`

`pip install twitter`

Also required is a Twitter account and setting up a Twitter app:
https://dev.twitter.com/apps/new

Example Twitter account, @HoneyPyLog - https://www.twitter.com/HoneyPyLog
