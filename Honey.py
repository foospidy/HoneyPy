#!/usr/bin/python

# Copyright (c) 2013, phiLLip maDDux II (foospidy)
# GNU GENERAL PUBLIC LICENSE
# https://github.com/foospidy/HoneyPy/blob/master/LICENSE

import socket
import threading
import ConfigParser
import logging
import logging.handlers
import os
import fnmatch
import time
import datetime
import re
import sys
import getopt
import urllib
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

# root logger
logger = logging.getLogger("")
logger.setLevel(logging.DEBUG)

# logging format
os.environ['TZ'] = 'Europe/London'
time.tzset()
logging.Formatter.conferter = time.gmtime	# using UTC/GMT
format                      = logging.Formatter(fmt='%(asctime)s %(levelname)s %(message)s')
#, datefmt='%Y-%m-%d %H:%M:%S %z')

# honey logger
honeyloghandler = logging.handlers.TimedRotatingFileHandler(logfile, 'midnight', 1)
honeylogger     = logging.getLogger('honey')

honeylogger.setLevel(logging.DEBUG)
honeyloghandler.setFormatter(format)
honeylogger.addHandler(honeyloghandler)

# setup twitter if enabled
if 'Yes' == honeypycfg.get('twitter', 'enabled'):
	from twitter import *
	twitterlogfile    = os.path.dirname(os.path.abspath(__file__)) + '/log/twitter.log'
	twitterloghandler = logging.handlers.TimedRotatingFileHandler(twitterlogfile, 'midnight', 1)
	twitterlogger     = logging.getLogger('twitter')

	twitterlogger.setLevel(logging.DEBUG)
	twitterloghandler.setFormatter(format)
	twitterlogger.addHandler(twitterloghandler)
	twitterlogger.info('Twitter enabled.')

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
	honeydb  = honeypycfg.get('honeydb', 'enabled')

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
		honeylogger.debug('Error starting %s:%s, %s' % (service, port, msg))
	except:
		honeylogger.debug(log, 'Error something for %s:%s' % (service, port))
	else:
		# Now wait for client connection.
		s.listen(5)

		while True:
			# Establish connection with client.
			c, addr = s.accept()
			honeylogger.info('CONNECT %s %s [%s] %s %s' % (host, port, service, addr[0], addr[1]))

			if('Yes' == twitter):
				honeytweet(service, addr[0])

			if('Yes' == statsd):
				StatsdClient.send({"HoneyPy." + host + ".connect":"1|c"}, (statsd_h, int(statsd_p)))

			if('Yes' == honeydb):
				t =  datetime.datetime.now()
				honeydb_logger(t.strftime("%Y-%m-%d"), t.strftime("%H:%M:%S"), t.strftime("%Y-%m-%d") + " " + t.strftime("%H:%M:%S"), t.microsecond, 'CONNECT', host, port, "[" + service + "]", addr[0], addr[1], '')

			# disable scripting for now, to be implemented in the future
			scripting = False;

			if scriping:
				while True:
					try:
						c.send(foo.nextmsg())
						data = c.recv(1024)
						if not data: break
						honeylogger.info('%s %s %s %s' % (service, port, addr, data.encode("hex")))
						foo.receive(data)

					except socket.error as msg:
						honeylogger.info('%s %s %s %s' % (service, port, addr, str(msg)))
						break
			else:
				# accept connections and log data to file
				while True:
					try:
						c.send(response)
						data = c.recv(1024)
						if not data: break
						honeylogger.info('RX %s %s [%s] %s %s %s' % (host, port, service, addr[0], addr[1], data.encode("hex")))
						if('Yes' == statsd):
							StatsdClient.send({"HoneyPy." + host + ".rx":"1|c"}, (statsd_h, int(statsd_p)))

						if('Yes' == honeydb):
							honeydb_logger(t.strftime("%Y-%m-%d"), t.strftime("%H:%M:%S"), t.strftime("%Y-%m-%d") + " " + t.strftime("%H:%M:%S"), t.microsecond, 'RX', host, port, "[" + service + "]", addr[0], addr[1], data.encode("hex"))

					except socket.error as msg:
						# typically "[Errno 104] Connection reset by peer", want to capture this as info
						honeylogger.info('ERROR %s %s [%s] %s %s %s' % (host, port, service, addr[0], addr[1], str(msg)))
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

	t        = Twitter(auth=OAuth(ot, os, ck, cs))
	nodename = honeypycfg.get('twitter', 'nodename')
	comment  = servicescfg.get(service, 'comment')
	try:
		t.statuses.update(status=nodename + ': #' + service + ' '  + comment + ' from ' + clientip + ' https://foospidy.com/opt/honeydb/view-ip/' + clientip)
	except Exception, err:
		twitterlogger.debug('Error posting to Twitter: %s' % err)


def honeyout(htmldir, refresh):
	"""
	Generate html output at the specified refresh rate.
	"""
	htmldir = os.path.dirname(os.path.abspath(__file__)) + '/' + htmldir

	while True:
		# Setup html directory if it doesn't exist
		if not os.path.exists(htmldir):
			os.makedirs(htmldir)

		menu = '<a href="honeypy.log.html">honeypy.log</a><br>'
		for filename in os.listdir(os.path.dirname(os.path.abspath(__file__)) + '/log'):
			if fnmatch.fnmatch(filename, "honeypy.log.*"):
				menu += '<a href="' +  filename + '.html">' + filename + '</a><br>'
			

		for filename in os.listdir(os.path.dirname(os.path.abspath(__file__)) + '/log'):
			if fnmatch.fnmatch(filename, "honeypy.log*"):
				inputfile  = open(os.path.dirname(os.path.abspath(__file__)) + '/log/' + filename)
				outputfile = open(os.path.dirname(os.path.abspath(__file__)) + '/html/' + filename + '.html', 'w')

				outputfile.writelines('<html><head><title>HoneyPy - Logs</title></head>')
				outputfile.writelines('<table><tr><td colspan=2><h3>HoneyPy Log</h3></td></tr><tr><td valign=top>' + menu + '</td><td valign=top>')
				outputfile.writelines('<pre>')

				for line in inputfile:
					words = line.split()
					if re.match("CONNECT|RX", words[3]):
						newline = words[0] + ' ' + words[1] + ' ' + words[3] + ' ' + words[5] + ' ' + words[6] + ' <a href="http://who.is/whois-ip/ip-address/' + words[7] + '" target="_new">' + words[7] + '</a> ' + words[8] + ' '
						if 10 == len(words):
							newline += '<a href="http://www.foospidy.com/opt/honeydb2/whois-data/' + words[7] + '/' + words[9] + '" target="_new">' + words[9] + '</a>'
						newline += "\n"
    			               		outputfile.writelines(newline)

				outputfile.writelines('</pre>')
				outputfile.writelines('</td></tr></table></html>')

				inputfile.close()
				outputfile.close()

		time.sleep(int(refresh))

def honeypysql():
        """
        Generate sql files from log data
        """
	global honeypycfg

	h      = hashlib.md5()
	sqldir = os.path.dirname(os.path.abspath(__file__)) + '/' + honeypycfg.get('honeypysql', 'sqldir')

        while True:
                # Setup sql directory if it doesn't exist
                if not os.path.exists(sqldir):
                        os.makedirs(sqldir)

                for filename in os.listdir(os.path.dirname(os.path.abspath(__file__)) + '/log'):
                        if fnmatch.fnmatch(filename, "honeypy.log*"):
                                inputfile  = open(os.path.dirname(os.path.abspath(__file__)) + '/log/' + filename)
                                outputfile = open(sqldir + '/' + filename + '.sql', 'w')

				# create table if not exist
                                outputfile.writelines('')

                                for line in inputfile:
                                        words = line.split()
                                        if re.match("CONNECT|RX", words[3]):
                                                newline = "INSERT INTO honeypy (date, time, date_time, millisecond, event, local_host, local_port, service, remote_host, remote_port"

						if 10 == len(words):
							newline += ", data, bytes, data_hash"

						timeparts = words[1].split(',')
						newline += ") VALUES ('" + words[0] + "', '" + timeparts[0] + "', '" + words[0] + " " + timeparts[0] + "', " + timeparts[1] + ", '" + words[3] + "', 'localhost', '" + words[5] + "', '" + words[6] + "', '" + words[7] + "', '" + words[8] + "'"

                                                if 10 == len(words):
							h.update(words[9])
                                                        newline += ", '" + words[9] + "', " + str(len(words[9])) + ", '" + h.hexdigest() + "'"
                                                newline += ");\n"
                                                outputfile.writelines(newline)


                                inputfile.close()
                                outputfile.close()

                time.sleep(int(honeypycfg.get('honeypysql', 'refresh')))

def honeydb_logger(date, time, date_time, millisecond, event, local_host, local_port, service, remote_host, remote_port, data):
	# post events to honedb logger
	global honeypycfg

	u = honeypycfg.get('honeydb', 'url')
        s = honeypycfg.get('honeydb', 'secret')
	h = hashlib.md5()

	h.update(data)

	# applying [:-3] to time to truncate microsecond
	d = urllib.urlencode([('date', date), ('time', time), ('date_time', date_time), ('millisecond', str(millisecond)[:-3]), ('s', s), ('event', event), ('local_host', local_host), ('local_port', local_port), ('service', service), ('remote_host', remote_host), ('remote_port', remote_port), ('data', data), ('bytes', str(len(data))), ('data_hash', h.hexdigest())])

	try:
		req      = urllib2.Request(u, d, {'User-Agent':'HoneyPy'})
		response = urllib2.urlopen(req)
		page     = response.read()

		honeylogger.info('Post event to honeydb, response: %s' % (page))
	except urllib2.URLError, e:
		honeylogger.debug('Error posting to honeydb: %s %s' % (str(e.code), str(e.reason)))

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
				url  = 'https://raw.githubusercontent.com/foospidy/HoneyPy/master/etc/services.cfg'
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
		elif 'display-log' == safe_input:
			with open(logfile) as file:
				for line in file:
					print line
		elif 'help' == safe_input:
			print 'start           - start services as defined in honeypy.cfg.'
			print 'count           - display count of current running threads.'
			print 'threads         - display list of all current running thread names.'
			print 'update-services - update the service.cfg file.'
			print 'test-statsd     - if statsd is enabled send a test counter to configured host.'
			print 'display-log     - displays the contents of honeypy.log.'
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
	global servicescfg, logfile, honeylogger

	max   = 450 
	count = 0

	for s in servicescfg.sections():
		count = count + 1

		if count <= max:
			honeylogger.info('Starting [%s] on port %s' % (s, servicescfg.get(s, 'port')))
			try:
				t        = threading.Thread(target=honey, args=(s, logfile), name=s)
				t.deamon = True
				t.start()
			except:
				honeylogger.debug('Error starting thread for [%s]. Is this a 32-bit system? If so, known issue, hope to fix soon.' % (s))
		else:
			honeylogger.info('Skipping [%s] on port %s; max service count exceeded.' % (s, servicescfg.get(s, 'port')))


def configure():
	"""
	do what the honeypy config file says
	"""
	global honeypycfg

	for s in honeypycfg.sections():
		if 'honeypyout' == s:
			if 'Yes' == honeypycfg.get(s, 'enabled'):
                        	honeylogger.info('Starting %s writing to %s' % (s, honeypycfg.get(s, 'htmldir')))
                        	t = threading.Thread(target=honeyout, args=(honeypycfg.get(s, 'htmldir'), honeypycfg.get(s, 'refresh')), name=s)
				t.deamon = True
				t.start()

		if 'honeypysql' == s:
			if  'Yes' == honeypycfg.get(s, 'enabled'):
				honeylogger.info('Starting %s writing to %s' % (s, honeypycfg.get(s, 'sqldir')))
				t = threading.Thread(target=honeypysql, args=(), name=s)
                        	t.deamon = True
                        	t.start()


configure()
argue(sys.argv[1:])
