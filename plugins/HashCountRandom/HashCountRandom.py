# HoneyPy Copyright (C) 2013-2016 foospidy
# https://github.com/foospidy/HoneyPy
# See LICENSE for details

from twisted.internet import protocol, reactor, endpoints
from twisted.python import log
import uuid

### START CUSTOM IMPORTS ###
import os
import md5
############################

class HashCountRandom(protocol.Protocol): ### Set custom protocol class name
	localhost   = None
	remote_host = None
	session     = None

	### START CUSTOM VARIABLES ###############################################################
	
	##########################################################################################

	# handle events
	def connectionMade(self):
		self.connect()

		### START CUSTOM CODE ####################################################################
		self.count = 0		
		self.tx('ACCEPT_CONN: ' + str(self.remote_host.host) + '\n')
		
		##########################################################################################

	def dataReceived(self, data):
		self.rx(data)

		### START CUSTOM CODE ####################################################################
		# custom code
		self.count = self.count + 1
		self.tx(self.md5sum(self.count) + ':' + str(os.urandom(99)) + '\n')
		
		##########################################################################################

	### START CUSTOM FUNCTIONS ###################################################################
	def md5sum(self, data):
		m = md5.new()
		m.update(str(data))
		return m.hexdigest()

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
	protocol = HashCountRandom ### Set protocol to custom protocol class name
	
	def __init__(self, name=None):
		self.name = name or 'HoneyPy'
