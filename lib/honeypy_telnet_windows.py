# Copyright (c) 2014, phiLLip maDDux II (foospidy)
# GNU GENERAL PUBLIC LICENSE
# https://github.com/foospidy/HoneyPy/blob/master/LICENSE

import socket
import threading
### START CUSTOM IMPORT
import time
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
			### START CUSTOM PROTOCOL ###########################################################################################################
			time.sleep(3)
			self.tx('Welcome to Microsoft Telnet Service\n\n')
			count = 0

			while count < 3:
				uname = ''
				while uname.rstrip() == '':
					self.tx('login: ')
					uname = self.rx()

				self.tx('password: ') 
				pword = self.rx()
				self.tx('\n')

				count = count + 1
			### END CUSTOM PROTOCOL #############################################################################################################
		except Exception as e:
			self.logger.debug('%s %s %s [%s] %s %s' % (str(e), self.host, self.port, self.service, self.remote_host, self.remote_port))
			print 'WARNING: ' + str(e)
			self.client_socket.close()

		self.client_socket.close()

	### START CUSTOM FUNCTIONS ##################################################################################################################
	### END CUSTOM FUNCTIONS ####################################################################################################################
