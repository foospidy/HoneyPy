#!/usr/bin/env python
# HoneyPy Copyright (C) 2013-2017 foospidy
# GNU GENERAL PUBLIC LICENSE
# https://github.com/foospidy/HoneyPy/blob/master/LICENSE

import sys
import os
import subprocess
import socket
import ConfigParser
import argparse
import importlib
from twisted.internet import protocol
from twisted.internet import reactor
from twisted.internet import stdio
from twisted.python import log
from twisted.python.log import FileLogObserver
from twisted.python.logfile import DailyLogFile
from lib.honeypy_logtail import HoneyPyLogTail
from lib.honeypy_console import HoneyPyConsole

# prevent creation of compiled bytecode files
sys.dont_write_bytecode = True

# handle and process command line arguments
parser = argparse.ArgumentParser(description='Process command line arguments.')
parser.add_argument('-d', help='run in daemon mode (no console).', default=False, action="store_true")
parser.add_argument('-ipt', help='generate ipt-kit script in /tmp.', default=False, action="store_true")
args = parser.parse_args()

# get path for config files
honeypy_config_file = os.path.dirname(os.path.abspath(__file__)) + '/etc/honeypy.cfg'
service_config_file = os.path.dirname(os.path.abspath(__file__)) + '/etc/services.cfg'
log_path = os.path.dirname(os.path.abspath(__file__)) + '/log/'
log_file_name = 'honeypy.log'
ipt_file_name = '/tmp/honeypy-ipt.sh'

# setup log file and formatting
if not os.path.exists(os.path.dirname(log_path)):
    # if log directory does not exist, create it.
    os.makedirs(os.path.dirname(log_path))

log_file = DailyLogFile(log_file_name, log_path)
file_log_observer = FileLogObserver(log_file)
time_zone = subprocess.check_output(['date', '+%z'])
file_log_observer.timeFormat = "%Y-%m-%d %H:%M:%S,%f," + time_zone.rstrip()

# get version
version = file(os.path.dirname(os.path.abspath(__file__)) + '/VERSION').read().strip()

# start logging
log.startLoggingWithObserver(file_log_observer.emit, False)

# setup config parsers
honeypy_config = ConfigParser.ConfigParser()
service_config = ConfigParser.ConfigParser()

# read config files
honeypy_config.read(honeypy_config_file)
service_config.read(service_config_file)

#check if other service profiles are to be included
if honeypy_config.has_option('honeypy', 'service_profiles'):
    log.msg('Skipping etc/services.cfg')
    service_config = ConfigParser.ConfigParser()
    for service_profile in honeypy_config.get('honeypy', 'service_profiles').split(','):
        profile_cfg_file = os.path.dirname(os.path.abspath(__file__)) + '/etc/profiles/' + service_profile.strip()
        log.msg("Reading services from %s" % profile_cfg_file)
        profile_cfg = ConfigParser.ConfigParser()
        profile_cfg.read(profile_cfg_file)
        #add the services from this profile
        for section in profile_cfg.sections():
            if profile_cfg.get(section, 'enabled').lower() == 'yes':
                #if enabled and don't already exist
                if not service_config.has_section(section):
                    log.msg("Adding service : %s %s" % (section, profile_cfg.get(section, 'low_port')))
                    service_config.add_section(section)
                    #read the options and add then to the new service section
                    for option in profile_cfg.options(section):
                        service_config.set(section, option, profile_cfg.get(section, option))
                else:
                    log.msg("Skipping duplicate service : %s %s" % (section, service_config.get(section, 'low_port')))

if args.ipt:
    # generate ipt-kit script in /tmp and quit.
    ipt_file = open(ipt_file_name, 'w')
    ipt_file.write('# copy this file to your ipt-kit directory and execute.\n')

    for service in service_config.sections():
        if service_config.get(service, 'enabled') == 'Yes':
            [low_protocol, low_port] = service_config.get(service, 'low_port').split(':')
            [protocol, port] = service_config.get(service, 'port').split(':')

            if int(low_port) < 1024:
                ipt_file.write('./ipt_set_' + low_protocol + ' ' + low_port + ' ' + port + ' $1\n')

    # set file permission, close, and quit
    os.chmod(ipt_file_name, 0744)
    ipt_file.close()
    quit()

# tail log file when reactor runs
tailer = HoneyPyLogTail(log_path + log_file_name)
tailer.config = honeypy_config
tailer.config.set('honeypy', 'useragent', 'HoneyPy (' + version + ')')
tailer.start()

log.msg(tailer.config.get('honeypy', 'useragent') + " Started")
for section in tailer.config.sections():
    if section != 'honeypy' and tailer.config.get(section, 'enabled').lower() == 'yes':
        log.msg("Enabled Logger : %s" % (section))

# services object array
services = []
services.append([])
services.append([])

# start enabled services
display_low_port_message = True


def get_ip_address():
    # function to ensure we get external IP (rather than hostname) for udp connections.
    # http://stackoverflow.com/questions/24196932/how-can-i-get-the-ip-address-of-eth0-in-python/24196955
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ipaddress = s.getsockname()[0]
    s.shutdown(socket.SHUT_RDWR)
    s.close()
    return ipaddress

for service in service_config.sections():
    if service_config.get(service, 'enabled') == 'Yes':
        [low_protocol, low_port] = service_config.get(service, 'low_port').split(':')
        [protocol, port] = service_config.get(service, 'port').split(':')
        plugin_module = 'plugins.' + service_config.get(service, 'plugin')
        plugin = importlib.import_module(plugin_module)
        service_object = None

        if args.d is False:
            if int(low_port) < 1024:
                if display_low_port_message:
                    print 'Your service configuration suggests that you want to run on at least one low port!'
                    print 'To enable port redirection run the following ipt-kit (https://github.com/foospidy/ipt-kit) commands as root:'
                    print ''
                    display_low_port_message = False

        try:
            if protocol.lower() == 'tcp':
                # run tcp service
                service_object = reactor.listenTCP(int(port), plugin.pluginFactory(service))
            else:
                # run udp service
                service_object = reactor.listenUDP(int(port), plugin.pluginMain(service, get_ip_address(), port))

            if service_object:
                # stop services from listening immediately if not starting in daemon mode.
                if args.d is False:
                    service_object.stopListening()

                # save service objects to array, to be used by HoneyPy Console
                services[0].append(service)
                services[1].append(service_object)

        except Exception as e:
            print str(e) + '\n'

            if str(e).find('Permission denied') != -1:
                print 'If you are attempting to use a low port (below 1024), do not.'
                print 'Low ports require root privilege and you should not run HoneyPy as root.'
                print 'Run the service on a high port and use IP Tables to redirect the low port'
                print 'to a high port. This may help, https://github.com/foospidy/ipt-kit'

            if str(e).find('Address already in use') != -1:
                print 'A service (' + service + ') is configured to run on a port that is already'
                print 'in use by another process. Kill the other process or use a different port.'

            sys.exit()

# run HoneyPy Console if daemon mode not specified
if args.d is False:
    stdio.StandardIO(HoneyPyConsole(honeypy_config, services))

# start reactor
reactor.run()
