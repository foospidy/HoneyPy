# HoneyPy Copyright (C) 2013-2015 foospidy
# https://github.com/foospidy/HoneyPy
# See LICENSE for details

from twisted.internet import protocol, reactor, endpoints
from twisted.python import log
import uuid

### START CUSTOM IMPORTS ###
import time

############################

class SmtpExim(protocol.Protocol): ### Set custom protocol class name
	localhost   = None
	remote_host = None
	session     = None

	### START CUSTOM VARIABLES ###############################################################
	state = 'COMMAND'
	##########################################################################################
	
	# handle events
	def connectionMade(self):
		self.connect()

		### START CUSTOM CODE ####################################################################
		self.tx('220 localhost ESMTP Exim 4.80 ' + time.strftime('%a, %d %b %H:%M:%S %z') + '\n');
		

		##########################################################################################

	def dataReceived(self, data):
		self.rx(data)

		### START CUSTOM CODE ####################################################################
		
		if 'COMMAND' == self.state:
			# parse command
			commandParts = str(data).split()

			if 0 == len(commandParts):
				self.tx('')
			else:
				command      = commandParts[0].lower()
				args         = commandParts[1:]

				try:
					method = getattr(self, 'do_' + command)
				except AttributeError, e:
					self.tx('500 unrecognized command\n')
				else:
					try:
						method(*args)
					except Exception, e:
						self.tx('500 Too many unrecognized commands\n')
						self.transport.loseConnection()
		else:
			self.rx(data)
			if '.' == str(data).strip():
				self.state = 'COMMAND'
				# todo: dynamically generate id
				self.tx('250 OK id=1ZaadR-0004Vi-1D\n')

		##########################################################################################

	### START CUSTOM FUNCTIONS ###################################################################
	def do_help(self):
		self.tx('214-Commands supported:\n214 AUTH HELO EHLO MAIL RCPT DATA NOOP QUIT RSET HELP\n')

	def do_ehlo(self, domain=None):
		if domain is None:
			self.tx('501 Syntactically invalid EHLO argument(s)\n')
		else:
			self.tx('250 localhost Hello ' + domain + ' [::1]\n250-SIZE 52428800\n250-8BITMIME\n250-PIPELINING\n250 HELP\n')

	def do_helo(self, domain=None):
		if domain is None:
			self.tx('501 Syntactically invalid HELO argument(s)\n')
		else:
			self.tx('250 localhost Hello ' + domain + ' [::1]\n')

	def do_mail(self, arg=None, sender=None):
		# todo: validate sender format (e.g. email address)
		if arg is None:
			self.tx('500 unrecognized command\n')
		elif 'from:' != arg:
			self.tx('500 unrecognized command\n')
		elif sender is None:
			self.tx('501 MAIL must have an address operand\n')
		else:
			self.tx('250 OK\n')

	def do_rcpt(self, arg=None, recipient=None):
		# todo: validate recipeint format (e.g. email address)
		if arg is None:
			self.tx('500 unrecognized command\n')
		elif 'to:' != arg:
			self.tx('500 unrecognized command\n')
		elif recipient is None:
			self.tx('501 RCPT must have an address operand\n')
		else:
			self.tx('250 Accepted\n')

	def do_data(self):
		self.state = 'DATA'
		self.tx('354 Enter message, ending with "." on a line by itself\n')
		
	def do_rset(self):
		self.tx('250 Reset OK\n')

	def do_auth(self):
		self.tx('503 AUTH command used when not advertised\n')

	def do_noop(self):
		self.tx('250 OK\n')

	def do_quit(self):
		self.tx('221 localhost closing connection\n')
		self.transport.loseConnection()
		
		
	##############################################################################################

	def connect(self):
		self.local_host  = self.transport.getHost()
		self.remote_host = self.transport.getPeer()
		self.session     = uuid.uuid1()
		log.msg('%s %s CONNECT %s %s %s %s %s' % (self.session, self.remote_host.type, self.local_host.host, self.local_host.port, self.factory.name, self.remote_host.host, self.remote_host.port))

	def tx(self, data):
		log.msg('%s %s TX %s %s %s %s %s %s' % (self.session, self.remote_host.type, self.local_host.host, self.local_host.port, self.factory.name, self.remote_host.host, self.remote_host.port, data.encode("hex")))
		self.transport.write(data)

	def rx(self, data):
		log.msg('%s %s RX %s %s %s %s %s %s' % (self.session, self.remote_host.type, self.local_host.host, self.local_host.port, self.factory.name, self.remote_host.host, self.remote_host.port, data.encode("hex")))

class pluginFactory(protocol.Factory):
	protocol = SmtpExim ### Set protocol to custom protocol class name
	
	def __init__(self, name=None):
		self.name = name or 'HoneyPy'
