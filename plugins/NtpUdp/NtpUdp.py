# HoneyPy Copyright (C) 2013-2016 foospidy
# https://github.com/foospidy/HoneyPy
# See LICENSE for details

from twisted.internet.protocol import DatagramProtocol
from twisted.python import log
import uuid

### START CUSTOM IMPORTS ###
from ntpserver import *

############################

class pluginMain(DatagramProtocol):
	
	def datagramReceived(self, data, (host, port)):
		self.rx(host, port, data)
		
		### START CUSTOM CODE ####################################################################
		
		recvTimestamp = system_to_ntp_time(time.time())		
		recvPacket = NTPPacket()
		recvPacket.from_data(data)
		timeStamp_high,timeStamp_low = recvPacket.GetTxTimeStamp()
		sendPacket = NTPPacket(version=3,mode=4)
		sendPacket.stratum = 2
		sendPacket.poll = 10
		sendPacket.ref_timestamp = recvTimestamp-5
		sendPacket.SetOriginTimeStamp(timeStamp_high,timeStamp_low)
		sendPacket.recv_timestamp = recvTimestamp
		sendPacket.tx_timestamp = system_to_ntp_time(time.time())
		
		self.tx(host, port, sendPacket.to_data())
	
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
