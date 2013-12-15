#!/usr/bin/python							# This is server.py file

# Copyright (c) 2013, phiLLip maDDux II (foospidy)
# GNU GENERAL PUBLIC LICENSE
# https://github.com/foospidy/HoneyPy/blob/master/LICENSE

import socket
import threading
import ConfigParser
import logging
import os
import time
import re
import sys
import getopt
import urllib2
import imp
import hashlib

# get absolute paths for config and log files.
cfgfile = os.path.dirname(os.path.abspath(__file__)) + '/etc/honeypy.cfg'
svcfile = os.path.dirname(os.path.abspath(__file__)) + '/etc/services.cfg'
logfile = os.path.dirname(os.path.abspath(__file__)) + '/log/honeypy.log'

# setup config parsers.
honeypycfg  = ConfigParser.ConfigParser()
servicescfg = ConfigParser.ConfigParser()

# read config files.
honeypycfg.read(cfgfile)
servicescfg.read(svcfile)

# Setup log directory if it doesn't exist, and setup logging
if not os.path.exists(os.path.dirname(logfile)):
	os.makedirs(os.path.dirname(logfile))

# ISO 8601 time format
logging.basicConfig(filename=logfile, level=logging.DEBUG, format='%(asctime)sZ %(levelname)s %(message)s')
# use UTC/GMT
logging.Formatter.converter = time.gmtime

# setup twitter if enabled
if 'Yes' == honeypycfg.get('twitter', 'enabled'):
	from twitter import *

# setup statsd if enabled
if 'Yes' == honeypycfg.get('statsd', 'enabled'):
	from lib.thirdparty.statsd import StatsdClient


def honey(service, log):
	"""
	release the honey!
	start the specified service and capture data to log file
	TODO: implement scriptable service emulation.
	"""
	global servicescfg, honeypycfg

	scriping = False
	port     = servicescfg.get(service, 'port')
	response = servicescfg.get(service, 'response')
	script   = servicescfg.get(service, 'script')

	twitter  = honeypycfg.get('twitter', 'enabled')

	statsd   = honeypycfg.get('statsd', 'enabled')
	statsd_h = honeypycfg.get('statsd', 'host')
	statsd_p = honeypycfg.get('statsd', 'port')

	if script.strip() != '':
		if not os.path.exists(script):
			print '%s : what you stank? Dere aint no scrip fill fool!' % (service)
		else:
			foo = imp.load_source('HoneyPyMod', script)
			scriping = True

	try:
		# Create a socket object
		s    = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		# the SO_REUSEADDR flag tells the kernel to reuse a local socket in TIME_WAIT state, without waiting for its natural timeout to expire.
		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

		# Get local machine name
		host = socket.gethostname()

		# Bind to the port
		s.bind(('', int(port)))
	except socket.error as msg:
		logging.debug('Error starting %s:%s, %s' % (service, port, msg))
	except:
		logging.debug(log, 'Error something for %s:%s' % (service, port))
	else:
		# Now wait for client connection.
		s.listen(5)

		while True:
			# Establish connection with client.
			c, addr = s.accept()
			logging.info('CONNECT %s %s [%s] %s %s' % (host, port, service, addr[0], addr[1]))

			if('Yes' == twitter):
				honeytweet(service, addr[0])

			if('Yes' == statsd):
				StatsdClient.send({"HoneyPy." + host + ".connect":"1|c"}, (statsd_h, int(statsd_p)))

			# disable scripting for now, to be implemented in the future
			scripting = False;

			if scriping:
				while True:
					try:
						c.send(foo.nextmsg())
						data = c.recv(1024)
						if not data: break
						logging.info('%s %s %s %s' % (service, port, addr, data.encode("hex")))
						foo.receive(data)

					except socket.error as msg:
						logging.info('%s %s %s %s' % (service, port, addr, str(msg)))
						break
			else:
				# accept connections and log data to file
				while True:
					try:
						c.send(response)
						data = c.recv(1024)
						if not data: break
						logging.info('RX %s %s [%s] %s %s %s' % (host, port, service, addr[0], addr[1], data.encode("hex")))
						if('Yes' == statsd):
							StatsdClient.send({"HoneyPy." + host + ".rx":"1|c"}, (statsd_h, int(statsd_p)))

					except socket.error as msg:
						# typically "[Errno 104] Connection reset by peer", want to capture this as info
						logging.info('ERROR %s %s [%s] %s %s %s' % (host, port, service, addr[0], addr[1], str(msg)))
						if('Yes' == statsd):
							StatsdClient.send({"HoneyPy." + host + ".error":"1|c"}, (statsd_h, int(statsd_p)))
						break

			# Close the connection
			c.close()

def honeytweet(service, clientip):
	global servicescfg, honeypycfg

	ck = honeypycfg.get('twitter', 'consumerkey')
	cs = honeypycfg.get('twitter', 'consumersecret')
	ot = honeypycfg.get('twitter', 'oauthtoken')
	os = honeypycfg.get('twitter', 'oauthsecret')

	t = Twitter(auth=OAuth(ot, os, ck, cs))
	nodename = honeypycfg.get('twitter', 'nodename')
	comment = servicescfg.get(service, 'comment')
	try:
		t.statuses.update(status=nodename + ': ' + comment + ' from ' + clientip)
	except:
		logging.debug('Error posting to Twitter');


def honeyout(s, log, html, refresh):
	"""
	Generate html output at the specified refresh rate.
	"""
	while True:
		# Setup html directory if it doesn't exist
		if not os.path.exists(os.path.dirname(html)):
			os.makedirs(os.path.dirname(html))

		inputfile  = open(log)
		outputfile = open(html, 'w')

		outputfile.writelines('<pre>')

		for line in inputfile:
       		 	if not re.match("^.*(.192.168.*).*$", line):
       		        	match = re.search(r'\(\'.*,', line)
               		 	if match:
	                        	ip = re.sub(r'[\(\'\,]', '', match.group())
     		                   	newline = re.sub(ip, '<a href="http://who.is/whois-ip/ip-address/' + ip + '" target="_new">' + ip + '</a>', line)
    		                    	outputfile.writelines(newline)

		outputfile.writelines('</pre>')

		inputfile.close()
		outputfile.close()
		time.sleep(int(refresh))


def console():
	"""
	Run interactive console.
	"""
	global svcfile

	banner = 'ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBfX18gICAgICAgCiAgL1wgIC9cX19fICBfIF9fICAgX19fIF8gICBfICAvIF8gXF8gICBfIAogLyAvXy8gLyBfIFx8ICdfIFwgLyBfIFwgfCB8IHwvIC9fKS8gfCB8IHwKLyBfXyAgLyAoXykgfCB8IHwgfCAgX18vIHxffCAvIF9fXy98IHxffCB8ClwvIC9fLyBcX19fL3xffCB8X3xcX19ffFxfXywgXC8gICAgIFxfXywgfAogICAgICAgICAgICAgICAgICAgICAgICB8X19fLyAgICAgICB8X19fLyAKCg=='
	version = 'WyBIb25leVB5IHYwLjEgQ29weXJpZ2h0IChjKSAyMDEzLiBmb29zcGlkeSBd'

	print banner.decode("base64"),
	print version.decode("base64") + "\n"

	# console loop
	safe_input = '';
	while 'quit' != safe_input:
        	input      = raw_input('honey>');
		safe_input = (input[:20]) if len(input) > 20 else input.strip()
		input      = '' # clear untrusted variable

        	if 'start' == safe_input:
			print 'starting...'
			startservices()
			print '%d service(s) running' % (threading.activeCount())
		elif 'count' == safe_input:
			print '%d service(s) running' % (threading.activeCount())
		elif 'threads' == safe_input:
			for t in threading.enumerate():
				#print t
				print t.name
		elif 'update-services' == safe_input:
			try:
				url  = 'http://www.foospidy.com/var/HoneyPy/services.cfg'
				f    = urllib2.urlopen(url)
				data = f.read()
				with open(svcfile, "wb") as svccfg:
					svccfg.write(data)

				print 'service.cfg file updated, restart HoneyPy to take effect.'
			except urllib2.URLError:
				print 'Error retreiving services.cfg'
				print 'Try downloading directly from ' + url
		elif 'test-statsd' == safe_input:
			if 'Yes' == honeypycfg.get('statsd', 'enabled'):
				statsd_h = honeypycfg.get('statsd', 'host')
				statsd_p = honeypycfg.get('statsd', 'port')
				StatsdClient.send({"HoneyPy." + socket.gethostname() + ".test":"1|c"}, (statsd_h, int(statsd_p)))
				print 'statsd test sent to %s on port %s' % (statsd_h, statsd_p)
			else:
				print 'statsd not enabled.'
		elif 'help' == safe_input:
			print 'start           - start services as defined in honeypy.cfg.'
			print 'count           - display count of current running threads.'
			print 'threads         - display list of all current running thread names.'
			print 'update-services - update the service.cfg file.'
			print 'test-statsd     - if statsd is enabled send a test counter to configured host.'
			print 'help            - display this help info.'
			print 'quit            - stop all current running threads and quit.'
		elif 'banner' == safe_input:
			print banner.decode("base64")

	os._exit(0)


def argue(argv):
	"""
	Handle command line arguements.
	"""
	try:
		opts, args = getopt.getopt(argv,"hvd")
	except getopt.GetoptError:
		print 'python HoneyPy.py'
		os._exit(2)

	consolemode = True

	for opt, arg in opts:
		if opt == '-h':
			print 'python HoneyPy.py'
			os._exit(0)
		elif '-v' == opt:
			print 'HoneyPy v0.0'
			os._exit(0)
		elif '-d' == opt:
			# run in deamon mode.
			consolemode = False
			startservices()

	if consolemode:
		console()


def startservices():
	"""
	start all services specified in the config file
	"""
	global servicescfg, logfile

	max   = 450 
	count = 0

	for s in servicescfg.sections():
		count = count + 1

		if count <= max:
			logging.info('Starting [%s] on port %s' % (s, servicescfg.get(s, 'port')))
			try:
				t        = threading.Thread(target=honey, args=(s, logfile), name=s)
				t.deamon = True
				t.start()
			except:
				logging.debug('Error starting thread for [%s]. Is this a 32-bit system? If so, known issue, hope to fix soon.' % (s))
		else:
			logging.info('Skipping [%s] on port %s; max service count exceeded.' % (s, servicescfg.get(s, 'port')))


def configure():
	"""
	do what the honeypy config file says
	"""
	global honeypycfg, logfile

	for s in honeypycfg.sections():
		if 'honeypyout' == s:
                        logging.info('Starting %s writing to %s' % (s, honeypycfg.get(s, 'html')))
                        t = threading.Thread(target=honeyout, args=(s, logfile, honeypycfg.get(s, 'html'), honeypycfg.get(s, 'refresh')), name=s)
			t.deamon = True
			t.start()


configure()
argue(sys.argv[1:])
