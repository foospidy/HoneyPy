# HoneyPy Copyright (C) 2013-2016 foospidy
# https://github.com/foospidy/HoneyPy
# See LICENSE for details

from twisted.internet.protocol import DatagramProtocol
from twisted.python import log
import uuid

### START CUSTOM IMPORTS ###
import struct
import os
############################

OPCODE_RRQ  = 1
OPCODE_WRQ  = 2
OPCODE_DATA = 3
OPCODE_ACK  = 4
OPCODE_ERR  = 5

ASCII_FILE = 'file.txt'
OCTET_FILE = 'file.bin'

MAX_UPLOAD_SIZE = 3906 * 512 # 3906 * 512 = 2MB

class pluginMain(DatagramProtocol):
	get_file     = None
	block_number = 1
	put_file     = None
	put_block_number = 0
	data         = None

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
			block_number = self.getDataBlockNumber(data)
			command_string = 'DATA %s %s' % (block_number, str(data))
		
		if opcode == OPCODE_ACK:
			command_string = 'ACK %s' % (str(data))
		
		self.rx(host, port, '%s' % command_string)

		if opcode == OPCODE_RRQ:
			path = os.path.dirname(os.path.realpath(__file__)) + '/'

			if 'netascii' == mode:
				path += ASCII_FILE
			else:
				path += OCTET_FILE
			
			self.get_file     = open(path, "r")
			self.block_number = 1

			self.resetFile(self.get_file)
			self.transmit(self.get_file, host, port)
		
		if opcode == OPCODE_WRQ:
			packet = struct.pack("!hh", OPCODE_ACK, self.put_block_number)
			self.tx(host, port, packet)

		
		if opcode == OPCODE_DATA:
			self.put_block_number += 1

			if (self.put_block_number * 512) > MAX_UPLOAD_SIZE:
				error_message = "Disk full or allocation exceeded.\000"
				packet = struct.pack("!hh%ds" % len(error_message), OPCODE_ERR, 3, error_message)
			else:
				packet = struct.pack("!hh", OPCODE_ACK, self.put_block_number)
			
			self.tx(host, port, packet)
		
		if opcode == OPCODE_ACK:
			block_number = struct.unpack("!H", data[2:4])[0]
			self.ack(block_number)
			self.transmit(self.get_file, host, port)

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
	
	def getDataBlockNumber(self, packet):
		block_number = struct.unpack("!H", packet[2:4])[0]
		return block_number
	
	def getWRQMode(self, packet):
		wrqmode = packet[packet[2:].index("\0") + 3:-1].lower()
		return wrqmode
	
	def resetFile(self, theFile):
		theFile.seek(0, 0)
	
	def transmit(self, theFile, host, port):
		self.data = theFile.read(512)
		packet    = struct.pack("!HH%ds" % len(self.data), OPCODE_DATA, self.block_number, self.data)
		#transmit_string = '%s DATA %s %s' % (len(data), self.block_number, str(data))
		#print transmit_string

		self.tx(host, port, packet)
	
	def ack(self, block_number):
		if block_number == self.block_number:
		    if len(self.data) < 512:
				# EOF, transmission complete
		        return True
		    else:
		        self.data = self.get_file.read(512)
		        self.block_number += 1
		
		#else - if unknown block number then possible tampering
	
	##############################################################################################
	
	def tx(self, host, port, data):
		log.msg('%s UDP TX %s %s %s %s %s %s' % (self.session, self.host, self.port, self.name, host, port, data.encode("hex")))
		self.transport.write(data, (host, int(port)))

	def rx(self, host, port, data):
		self.session = uuid.uuid1()
		log.msg('%s UDP RX %s %s %s %s %s %s' % (self.session, self.host, self.port, self.name, host, port, data.encode("hex")))

	def __init__(self, name=None, host=None, port=None):
		self.name    = name or 'HoneyPy'
		self.host    = host or '???'
		self.port    = port or '???'
		self.session = None
