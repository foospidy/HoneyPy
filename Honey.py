#!/usr/bin/python
# HoneyPy Copyright (C) 2013-2015 foospidy
# GNU GENERAL PUBLIC LICENSE
# https://github.com/foospidy/HoneyPy/blob/master/LICENSE

import sys
import os
import subprocess
import socket
import threading
import ConfigParser
import argparse
import importlib
import lib.followtail
from lib.honeypy_console import HoneyPyConsole
from lib.honeypy_log_triage import triage, triageConfig
from twisted.internet import protocol, reactor, endpoints, stdio
from twisted.protocols import basic
from twisted.python import log
from twisted.python.log import ILogObserver, FileLogObserver
from twisted.python.logfile import DailyLogFile

# prevent creation of compiled bytecode files
sys.dont_write_bytecode = True

# handle and process command line arguments
parser = argparse.ArgumentParser(description='Process command line arguments.')
parser.add_argument('-d', help='run in daemon mode (no console).', default=False, action="store_true")
args = parser.parse_args()

# get path for config files
honeypy_config_file = os.path.dirname(os.path.abspath(__file__)) + '/etc/honeypy.cfg'
service_config_file = os.path.dirname(os.path.abspath(__file__)) + '/etc/services.cfg'
log_path            = os.path.dirname(os.path.abspath(__file__)) + '/log/'
log_file_name       = 'honeypy.log'

# setup config parsers
honeypy_config  = ConfigParser.ConfigParser()
service_config  = ConfigParser.ConfigParser()

# read config files
honeypy_config.read(honeypy_config_file)
service_config.read(service_config_file)

# setup log file and formatting
if not os.path.exists(os.path.dirname(log_path)):
	# if log directory does not exist, create it.
	os.makedirs(os.path.dirname(log_path))

log_file                     = DailyLogFile(log_file_name, log_path)
file_log_observer            = FileLogObserver(log_file)
time_zone                    = subprocess.check_output(['date', '+%z'])
file_log_observer.timeFormat = "%Y-%m-%d %H:%M:%S,%f," + time_zone.rstrip()

# start logging
log.startLoggingWithObserver(file_log_observer.emit, False)

if 'Yes' == honeypy_config.get('twitter', 'enabled') or 'Yes' == honeypy_config.get('honeydb', 'enabled'):
	# tail log file when reactor runs
	triageConfig(honeypy_config)
	tailer = lib.followtail.FollowTail(log_path + log_file_name)
	tailer.lineReceived = triage
	tailer.start()

# services object array
services = []
services.append([])
services.append([])

# start enabled services
display_low_port_message = True

for service in service_config.sections():
	if 'Yes' == service_config.get(service, 'enabled'):
		[low_protocol, low_port] = service_config.get(service, 'low_port').split(':')
		[protocol, port]         = service_config.get(service, 'port').split(':')
		plugin_module            = 'plugins.' + service_config.get(service, 'plugin')
		plugin                   = importlib.import_module(plugin_module)
		service_object           = None

		if int(low_port) < 1024:
			if display_low_port_message:
				print('Your service configuration suggests that you want to run on at least one low port!')
				print('To enable port redirection run the following ipt-kit (https://github.com/foospidy/ipt-kit) commands as root:')
				print('')
				display_low_port_message = False
				
			print('./ipt_set_' + low_protocol + ' ' + low_port + ' ' + port	)

		try:
			if 'tcp' == protocol.lower():
				# run tcp service
				service_object = reactor.listenTCP(int(port), plugin.pluginFactory(service))
			else:
				# run udp service
				service_object = reactor.listenUDP(int(port), plugin.pluginMain(service, socket.gethostname(), port))

			if service_object:
				# stop services from listening immediately if not starting in daemon mode.
				if False == args.d:
					service_object.stopListening()

				# save service objects to array, to be used by HoneyPy Console
				services[0].append(service)
				services[1].append(service_object)

		except Exception as e:
			print(str(e) + '\n')
			
			if -1 != str(e).find('Permission denied'):
				print('If you are attempting to use a low port (below 1024), do not.')
				print('Low ports require root privilege and you should not run HoneyPy as root.')
				print('Run the service on a high port and use IP Tables to redirect the low port')
				print('to a high port. This may help, https://github.com/foospidy/ipt-kit')

			if -1 != str(e).find('Address already in use'):
				print('A service (' + service + ') is configured to run on a port that is already')
				print('in use by another process. Kill the other process or use a different port.')

			sys.exit()

# run HoneyPy Console if daemon mode not specified
if False == args.d:
	stdio.StandardIO(HoneyPyConsole(honeypy_config, services))

# start reactor
reactor.run()
