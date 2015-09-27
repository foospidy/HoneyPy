# HoneyPy Copyright (C) 2013-2015 foospidy
# https://github.com/foospidy/HoneyPy
# See LICENSE for details

from twisted.internet.protocol import DatagramProtocol
from twisted.python import log
import uuid

### START CUSTOM IMPORTS ###
from dnslib import *
import random
import socket
import struct
############################

class pluginMain(DatagramProtocol):
	
	def datagramReceived(self, data, (host, port)):
		self.rx(host, port, data)
		
		### START CUSTOM CODE ####################################################################

		request = DNSRecord.parse(data)
		id      = request.header.id
		qname   = request.q.qname
		qtype   = request.q.qtype

		IP           = self.get_random_ip()
		BIND_VERSION = '8.2.2-P5'
		C_NAME        = 'taco.burrito'

		reply = DNSRecord(DNSHeader(id=id, qr=1, aa=1, ra=1), q=request.q)
		
		if self.is_version_request(qname):
			reply.add_answer(RR(qname, QTYPE.TXT, rdata=TXT(BIND_VERSION)))
		elif QTYPE.A == qtype:
			reply.add_answer(RR(qname, qtype, rdata=A(IP)))
		elif QTYPE.MX == qtype:
			reply.add_answer(RR(qname, qtype, rdata=MX(IP)))
		elif QTYPE.CNAME == qtype:
			reply.add_answer(RR(qname, QTYPE.CNAME, rdata=CNAME(C_NAME)))			
		else:
			reply.add_answer(RR(qname, QTYPE.A, rdata=A(IP)))
			reply.add_answer(RR(qname, QTYPE.MX, rdata=MX(IP)))
			reply.add_answer(RR(qname, QTYPE.TXT, rdata=TXT(IP)))

		self.tx(host, port, reply.pack())

		##########################################################################################

	### START CUSTOM FUNCTIONS ###################################################################
	def is_version_request(self, qname):
		if 'versionbind' == str(qname).replace('.', '').lower():
			return True
		else:
			return False
	
	def get_random_ip(self):
		ip = '0.0.0.0'
		
		while('0.0.0.0' == ip or '255.255.255.255' == ip):
			# http://stackoverflow.com/questions/21014618/python-randomly-generated-ip-address-of-the-string
			ip = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
		
		return ip
		
	##############################################################################################
	
	def tx(self, host, port, data):
		log.msg('%s UDP TX %s %s %s %s %s %s' % (self.session, self.host, self.port, self.name, host, port, str(data).encode("hex")))
		self.transport.write(data, (host, port))

	def rx(self, host, port, data):
		self.session = uuid.uuid1()
		log.msg('%s UDP RX %s %s %s %s %s %s' % (self.session, self.host, self.port, self.name, host, port, data.encode("hex")))

	def __init__(self, name=None, host=None, port=None):
		self.name    = name or 'HoneyPy'
		self.host    = host or '???'
		self.port    = port or '???'
		self.session = None
