# HoneyPy Copyright (C) 2013-2015 foospidy
# https://github.com/foospidy/HoneyPy
# See LICENSE for details

from twisted.internet import protocol, reactor, endpoints, defer
from twisted.python import log
import uuid

### START CUSTOM IMPORTS ###

############################

class TelnetDebian7(protocol.Protocol): ### Set custom protocol class name
	localhost   = None
	remote_host = None
	session     = None
	
	### START CUSTOM VARIABLES ###############################################################
	state = 'NO_UNAME'
	uname = None
	pword = None
	
	##########################################################################################

	# handle events
	def connectionMade(self):
		self.connect()

		### START CUSTOM CODE ####################################################################
		self.tx('Debian GNU/Linux 7\r\n')
		self.tx('Login: ')
		
		##########################################################################################

	def dataReceived(self, data):
		self.rx(data)

		### START CUSTOM CODE ####################################################################
		if 'NO_UNAME' == self.state:
			self.uname = data.rstrip()
			self.state = 'NO_PWORD'
			self.tx('Password: ')
		elif 'NO_PWORD' == self.state:
			self.pword = data.rstrip()
			if 'Pa$$word' == self.pword:
				self.tx('WARNING: System error, closing connection.\n')
				self.transport.loseConnection()
			else:
				self.state = 'NO_UNAME'
				self.tx('Login incorrect\n')
				self.tx('Login: ')

		##########################################################################################

	### START CUSTOM FUNCTIONS ###################################################################

			
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
	protocol = TelnetDebian7 ### Set protocol to custom protocol class name
	
	def __init__(self, name=None):
		self.name = name or 'HoneyPy'
