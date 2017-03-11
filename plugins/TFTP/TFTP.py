# HoneyPy Copyright (C) 2013-2016 foospidy
# https://github.com/foospidy/HoneyPy
# See LICENSE for details

from twisted.internet.protocol import DatagramProtocol
from twisted.python import log
import uuid

### START CUSTOM IMPORTS ###
import struct
############################

OPCODE_RRQ  = 1
OPCODE_WRQ  = 2
OPCODE_DATA = 3
OPCODE_ACK  = 4

class pluginMain(DatagramProtocol):
	
	def datagramReceived(self, data, (host, port)):
		#self.rx(host, port, data)
		
		### START CUSTOM CODE ####################################################################
		command_string = ''
		opcode         = self.getOpcode(data)

		if opcode == OPCODE_RRQ:
			mode            = self.getRRQMode(data)
			command_string = 'RRQ %s %s' % (self.getFileName(data), mode)
		
		if opcode == OPCODE_WRQ:
			mode            = self.getWRQMode(data)
			command_string  = 'WRQ %s %s' % (self.getFileName(data), mode)
		
		if opcode == OPCODE_DATA:
			command_string = 'DATA %s' % (str(data))
		
		if opcode == OPCODE_ACK:
			command_string = 'ACK %s' % (str(data))
		
		self.rx(host, port, '%s' % command_string)

		##########################################################################################

	### START CUSTOM FUNCTIONS ###################################################################
	def getOpcode(self, packet):
		opcode = struct.unpack("!H", packet[0:2])[0]
		return opcode
	
	def getRRQMode(self, packet):
		rrqmode = packet[packet[2:].index("\0") + 3:-1].lower()
		return rrqmode
	
	def getFileName(self, packet):
		return packet.split("\0")[1]
	
	def getWRQMode(self, packet):
		wrqmode = packet[packet[2:].index("\0") + 3:-1].lower()
		return wrqmode
	
	def resetFile(theFile):
		theFile.seek(0, 0)
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
