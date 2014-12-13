# Copyright (c) 2014, phiLLip maDDux II (foospidy)
# GNU GENERAL PUBLIC LICENSE
# https://github.com/foospidy/HoneyPy/blob/master/LICENSE

import socket
import threading
import datetime
import lib.honeydb
### START CUSTOM IMPORT
import time
import random
### END CUSTOM IMPORT

class MyMainHoney(threading.Thread):
	def __init__(self, logger, honeydb, host, port, service, remote_host, remote_port, client_socket):
		threading.Thread.__init__(self)
		self.logger        = logger
		self.honeydb       = honeydb
		self.host          = host
		self.port          = port
		self.service       = service
		self.remote_host   = remote_host
		self.remote_port   = remote_port
		self.client_socket = client_socket

	def tx(self, data):
		self.client_socket.send(data)
		self.logger.info('TX %s %s [%s] %s %s %s' % (self.host, self.port, self.service, self.remote_host, self.remote_port, data.encode("hex")))

		if('Yes' == self.honeydb['enabled']):
			t =  datetime.datetime.now()
			lib.honeydb.logger(self.honeydb['url'], self.honeydb['secret'], t.strftime("%Y-%m-%d"), t.strftime("%H:%M:%S"), t.strftime("%Y-%m-%d") + " " + t.strftime("%H:%M:%S"), t.microsecond, 'TX', self.host, self.port, "[" + self.service + "]", self.remote_host, self.remote_port, data.encode("hex"))

	def rx(self):
		data = self.client_socket.recv(65535)
		self.logger.info('RX %s %s [%s] %s %s %s' % (self.host, self.port, self.service, self.remote_host, self.remote_port, data.encode("hex")))
		return data

	def run(self):
		#self.rx()
		try:
			### START CUSTOM PROTOCOL ###########################################################################################################
			command            = ['foo'] # initialize first element of array with something
			max_login_attempt  = 10
			success_count      = random.randint(3, max_login_attempt)
			count              = 0
			loggedin           = False
			user               = ''
			password           = ''
			pwd                = '/'
			
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
								# initialize some variables
								if 'root' == user:
									pwd = '/root'
								else:
									pwd = '/home/' + user

								self.tx('230 User ' + user + ' logged in\n')
							else:
								self.tx('530 Login incorrect.\n')

				elif 'pwd' == command[0] or 'xpwd' == command[0]:
					self.tx(pwd + '\n')

				elif 'cwd' == command[0] or 'xcwd' == command[0]:
					if len(command) < 2:
						self.tx('501 Invalid number of arguments\n')
					else:
						self.tx('550 ' + command[1] + ': No such file or directory\n')
					
					#todo 257 "' + command[1] + '" - Directory successfully created

				elif 'mkd' == command[0] or 'xmkd' == command[0]:
					if len(command) < 2:
						self.txt('501 Invalid number of arguments\n')
					else:
						self.tx(550 ' + command[1] + ': Permission denied')

				elif 'port' == command[0]:
					if len(command) < 2:
						self.tx('501 Invalid number of arguments\n')
					else:
						self.tx('501 Illegal PORT command\n')
				
				elif 'cdup' == command[0]:
					self.tx('550 ' + command[1] + ': No such file or directory\n')

				elif 'pasv' == command[0]:
					self.tx('Passive mode on.\n')
				
				elif 'abor' == command[0]:
					self.tx('226 Abort successful\n')
				
				elif 'allo' == command[0]:
					self.tx('214 Syntax: ALLO is not implemented (ignored)\n')
				
				elif 'syst' == command[0]:
					self.tx('215 UNIX Type: L8')

				elif 'help' == command[0]:
					self.tx('help not availible\n')

				elif 'quit' == command[0]:
					break;
				
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
	### END CUSTOM FUNCTIONS ####################################################################################################################
