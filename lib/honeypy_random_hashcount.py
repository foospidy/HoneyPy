# Copyright (c) 2014, phiLLip maDDux II (foospidy)
# GNU GENERAL PUBLIC LICENSE
# https://github.com/foospidy/HoneyPy/blob/master/LICENSE

import socket
import threading
### START CUSTOM IMPORT
import time
import os
import md5
### END CUSTOM IMPORT

class MyMainHoney(threading.Thread):
	def __init__(self, logger, host, port, service, remote_host, remote_port, client_socket):
		threading.Thread.__init__(self)
		self.logger        = logger
		self.host          = host
		self.port          = port
		self.service       = service
		self.remote_host   = remote_host
		self.remote_port   = remote_port
		self.client_socket = client_socket

	def tx(self, data):
		self.client_socket.send(data)
		self.logger.info('TX %s %s [%s] %s %s %s' % (self.host, self.port, self.service, self.remote_host, self.remote_port, data.encode("hex")))

	def rx(self):
		data = self.client_socket.recv(65535)
		self.logger.info('RX %s %s [%s] %s %s %s' % (self.host, self.port, self.service, self.remote_host, self.remote_port, data.encode("hex")))
		return data

	def run(self):
		try:
			self.rx()
			### START CUSTOM PROTOCOL ###########################################################################################################
			self.tx('ACCEPT_CONN: ' + str(self.remote_host) + ':' + str(self.remote_port) + '\n')
			count = 0

			while True:
				count = count + 1
				self.tx(md5sum(count) + ':' + str(os.urandom(99)) + '\n')
				self.rx()
				time.sleep(1)

			### END CUSTOM PROTOCOL #############################################################################################################
		except Exception as e:
			self.logger.debug('%s %s %s [%s] %s %s' % (str(e), self.host, self.port, self.service, self.remote_host, self.remote_port))
			print 'WARNING: ' + str(e)
			self.client_socket.close()

		self.client_socket.close()

	### START CUSTOM FUNCTIONS ##################################################################################################################
	def md5sum(data):
		m = md5.new()
		m.update(str(data))
		return m.hexdigest()
	
	### END CUSTOM FUNCTIONS ####################################################################################################################
