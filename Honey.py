#!/usr/bin/python							# This is server.py file

# Copyright (c) 2013, phiLLip maDDux II (foospidy)
# GNU GENERAL PUBLIC LICENSE
# https://github.com/foospidy/HoneyPy/blob/master/LICENSE

import socket
import threading
import ConfigParser
import os
import time
import re
import sys
import getopt
import urllib2
import imp

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

# Setup log directory if it doesn't exist
if not os.path.exists(os.path.dirname(logfile)):
	os.makedirs(os.path.dirname(logfile))

def logger(file, txt):
	"""
	Log messages to log file in standard format
	"""
	f = open(file, 'a')
	f.write(time.asctime(time.localtime(time.time())) + ' ' + txt + '\n')
	f.close()


def honey(service, log):
	"""
	release the honey!
	start the specified service and capture data to log file
	TODO: implement scriptable service emulation.
	"""
	global servicescfg

	scriping = False
	port     = servicescfg.get(service, 'port')
	response = servicescfg.get(service, 'response')
	script   = servicescfg.get(service, 'script')

	if script.strip() != '':
		if not os.path.exists(script):
			print '%s : what you stank? Dere aint no scrip fill fool!' % (service)
		else:
			foo = imp.load_source('HoneyPyMod', script)
			scriping = True

	# Create a socket object
	s    = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# the SO_REUSEADDR flag tells the kernel to reuse a local socket in TIME_WAIT state, without waiting for its natural timeout to expire.
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	# Get local machine name
	host = socket.gethostname()

	try:
		# Bind to the port
		s.bind(('', int(port)))
	except socket.error as msg:
		logger(log, 'Error starting %s:%s, %s' % (service, port, msg))
	except:
		logger(log, 'Error something for %s:%s' % (service, port))
	else:
		# Now wait for client connection.
		s.listen(5)

		while True:
			# Establish connection with client.
			c, addr = s.accept()
			logger(log, '%s %s %s connect!' % (service, port, addr))

			# disable scripting for now, to be implemented in the future
			scripting = False;

			if scriping:
				while True:
					try:
						c.send(foo.nextmsg())
						data = c.recv(1024)
						if not data: break
						logger(log, '%s %s %s %s' % (service, port, addr, data.encode("hex")))
						foo.receive(data)

					except socket.error as msg:
						logger(log, '%s %s %s %s' % (service, port, addr, str(msg)))
						break
			else:
				# accept connections and log data to file
				while True:
					try:
						c.send(response)
						data = c.recv(1024)
						if not data: break
						logger(log, '%s %s %s %s' % (service, port, addr, data.encode("hex")))

					except socket.error as msg:
						logger(log, '%s %s %s %s' % (service, port, addr, str(msg)))
						break

			# Close the connection
			c.close()


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
		safe_input = (input[:20]) if len(input) > 20 else input
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
		elif 'updatesvc' == safe_input:
			try:
				url  = 'http://www.foospidy.com/var/HoneyPy/services.cfg'
				f    = urllib2.urlopen(url)
				data = f.read()
				with open(svcfile, "wb") as svccfg:
					svccfg.write(data)
			except urllib2.URLError:
				print 'Error retreiving services.cfg'
				print 'Try downloading directly from ' + url

		elif 'help' == safe_input:
			print 'start     - start services as defined in honeypy.cfg.'
			print 'count     - display count of current running threads.'
			print 'threads   - display list of all current running thread names.'
			print 'updatesvc - update the service.cfg file.'
			print 'help      - display this help info.'
			print 'quit      - stop all current running threads and quit.'
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

	count = 0
	for s in servicescfg.sections():
		count = count + 1
		logger(logfile, 'Starting %s on port %s' % (s, servicescfg.get(s, 'port')))

		t        = threading.Thread(target=honey, args=(s, logfile), name=s)
		t.deamon = True
		t.start()


def configure():
	"""
	do what the honeypy config file says
	"""
	global honeypycfg, logfile

	for s in honeypycfg.sections():
		if 'honeypyout' == s:
                        logger(logfile, 'Starting %s writing to %s' % (s, honeypycfg.get(s, 'html')))
                        t = threading.Thread(target=honeyout, args=(s, logfile, honeypycfg.get(s, 'html'), honeypycfg.get(s, 'refresh')), name=s)
			t.deamon = True
			t.start()


configure()
argue(sys.argv[1:])
