# HoneyPy Copyright (C) 2013-2015 foospidy
# https://github.com/foospidy/HoneyPy
# See LICENSE for details

from twisted.internet import protocol, reactor, endpoints, defer
from twisted.python import log
import uuid

### START CUSTOM IMPORTS ###
from twisted.protocols.telnet import *
from clilib import *

############################

class TelnetUnix(Telnet): ### Set custom protocol class name
	localhost   = None
	remote_host = None
	session     = None
	
	### START CUSTOM VARIABLES ###############################################################
	username = None
	prompt = '$'
	
	##########################################################################################

	# handle events
	def connectionMade(self):
		self.connect()

		### START CUSTOM CODE ####################################################################
		Telnet.connectionMade(self)
		
		##########################################################################################

	def dataReceived(self, data):
		self.rx(data)
		
		### START CUSTOM CODE ####################################################################
		Telnet.dataReceived(self, data)
		
		##########################################################################################

	### START CUSTOM FUNCTIONS ###################################################################
	def welcomeMessage(self):
		return "Debian GNU/Linux 7\r\n"
	
	def loginPrompt(self):
		return "Login: "
	
	def telnet_Password(self, password):
		self.write(IAC+WONT+ECHO+"\r\n")

		try:
			successful_login = self.checkUserAndPass(password)
			
			if not successful_login:
				self.tx("\r\ninvalid login\r\npassword:")
				return 'Password' # return the mode
			else:
				self.loggedIn()
				
				self.username = self.username.strip()
				
				if 'root' == self.username:
					self.prompt = '#'
				
				self.tx(self.username + self.prompt + ' ')
				
				return 'Command' # return the mode
				
		except Exception, e:
			print 'Error performing telnet authentication: ' + e + '\r\n'
			return 'Done' # return the mode

	def checkUserAndPass(self, password):
		authenticated = False
		
		password_list = ('admin', 'password', 'root', '12345', '123456')
		
		if password in password_list:
			authenticated = True
		
		return authenticated
	
	def telnet_Command(self, cmd):
		
		# parse command
		commands = str(cmd).split(';')
		
		for c in commands:
			commandParts = str(c.strip()).split()
	
			if 0 == len(commandParts):
				if 'root' == self.username:
					self.prompt = '#'
				
				self.tx(self.username + self.prompt + ' ')
			else:
				command = commandParts[0].lower()
				args    = commandParts[1:]
	
				try:
					method = getattr(self, 'do_' + command)
				except AttributeError, e:
					self.tx('- bash: ' + command + ': command not found\r\n')
					self.tx(self.username + self.prompt + ' ')
				else:
					try:
						method(*args)
						self.tx('\r\n' + self.username + self.prompt + ' ')
					except Exception, e:
						self.tx('WARNING: System error, closing connection.\n')
						print str(e)
						self.transport.loseConnection()
		
		return 'Command'
		
	def do_exit(self, args=None):
		self.mode = 'Done'
		self.transport.loseConnection()
	
	def do_man(self, *args):
		command = ''

		if len(args) > 0:
			command = args[0]
		
		self.tx(man(command))
	
	def do_echo(self, *args):
		self.tx(echo(*args))
	
	def do_uname(self, *args):
		self.tx(uname(*args))
	
	def do_whoami(self, *args):
		self.tx(whoami(self.username, *args))
	
	def do_which(self, *args):
		command = ''
		
		if len(args) > 0:
			command = args[0]
		
		self.tx(which(command))
	
	def do_rm(self, *args):
		self.tx(rm())
	
	def do_sh(self, *args):
		self.tx(sh())
	
	def do_cd(self, *args):
		self.tx(cd())
	
	def do_busybox(self, *args):
		self.tx(busybox())
	
	def do_wget(self, *args):
		self.tx(wget())
	
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
	protocol = TelnetUnix ### Set protocol to custom protocol class name
	
	def __init__(self, name=None):
		self.name = name or 'HoneyPy'
