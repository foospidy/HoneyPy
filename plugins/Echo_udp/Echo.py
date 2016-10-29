# HoneyPy Copyright (C) 2013-2016 foospidy
# https://github.com/foospidy/HoneyPy
# See LICENSE for details

from twisted.internet.protocol import DatagramProtocol
from twisted.python import log
import uuid

### START CUSTOM IMPORTS ###

############################

class pluginMain(DatagramProtocol):
	
	def datagramReceived(self, data, (host, port)):
		self.rx(host, port, data)
		
		### START CUSTOM CODE ####################################################################
		self.tx(host, port, data)
	
		##########################################################################################

	### START CUSTOM FUNCTIONS ###################################################################

	##############################################################################################
	
	def tx(self, host, port, data):
		log.msg('%s UDP TX %s %s %s %s %s %s' % (self.session, self.host, self.port, self.name, host, port, data.encode("hex")))
		self.transport.write(data, (host, port))

	def rx(self, host, port, data):
		self.session = uuid.uuid1()
		log.msg('%s UDP RX %s %s %s %s %s %s' % (self.session, self.host, self.port, self.name, host, port, data.encode("hex")))

	def __init__(self, name=None, host=None, port=None):
		self.name    = name or 'HoneyPy'
		self.host    = host or '???'
		self.port    = port or '???'
		self.session = None
