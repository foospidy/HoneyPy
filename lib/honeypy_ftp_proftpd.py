# Copyright (c) 2014, phiLLip maDDux II (foospidy)
# GNU GENERAL PUBLIC LICENSE
# https://github.com/foospidy/HoneyPy/blob/master/LICENSE

import socket
import threading
### START CUSTOM IMPORT
import time
import random
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
		self.rx()
		try:
			### START CUSTOM PROTOCOL ###########################################################################################################
			command            = ['foo'] # initialize first element of array with something
			max_login_attempt  = 10
			success_count      = random.randint(3, max_login_attempt)
			count              = 0
			loggedin           = False
			user               = ''
			password           = ''
			
			time.sleep(2)
			self.tx('220 ProFTPD 1.2.4 Server (ProFTPD) [::ffff:' + self.host + ']\n')
			
			while 'quit' != command[0]:
				command = str(self.rx()).rstrip().lower().split()
				
				if 0 == len(command):
					self.tx('500 Invalid command: try being more creative\n')
					command = ['foo']
	
				elif 'user' == command[0]:
					if len(command) < 2:
						self.tx('500 USER: command requires a parameter\n')
					else:
						user = command[1]
						self.tx('331 Password required for ' + command[1] + '\n')

				elif 'pass' == command[0]:
					if len(command) < 2:
						self.tx('530 Login incorrect.\n')
					else:
						if '' == user:
							self.txt('503 Login with USER first\n')
						else:
							if 'password' == command[1]:
								self.tx('230 User ' + user + ' logged in\n')
							else:
								self.tx('530 Login incorrect.\n')

				elif 'syst' == command[0]:
					self.tx('215 UNIX Type: L8')
				
				elif 'help' == command[0]:
					self.tx('help not availible\n')
					
				else:
					self.tx('500 ' + command[0] + ' not understood\n')
			
			self.tx('221 Goodbye.\n')

			### END CUSTOM PROTOCOL #############################################################################################################
		except Exception as e:
			self.logger.debug('%s %s %s [%s] %s %s' % (str(e), self.host, self.port, self.service, self.remote_host, self.remote_port))
			print 'WARNING: ' + str(e)
			self.client_socket.close()

		self.client_socket.close()

	### START CUSTOM FUNCTIONS ##################################################################################################################
