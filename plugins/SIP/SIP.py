# HoneyPy Copyright (C) 2013-2017 foospidy
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
                sipheaders = {'Via':'', 'From':'', 'To':'', 'CallID':'', 'Cseq':'', 'UserAgent':'', 'Contact':'', 'Expires':'', 'Allow':'', 'Lenght':'', 'Authorization':''}
                sip=data.split("\r\n")
                for header in sip:
                        if "Via:" in header:
                                sipheaders['Via']=header
                        elif "From:" in header:
                                sipheaders['From']=header
                        elif "To:" in header:
                                sipheaders['To']=header
                        elif "Call-ID:" in header:
                                sipheaders['CallID']=header
                        elif "CSeq:" in header:
                                sipheaders['CSeq']=header
                        elif "User-Agent:" in header:
                                sipheaders['UserAgent']=header
                        elif "Contact:" in header:
                                sipheaders['Contact']=header
                        elif "Expires:" in header:
                                sipheaders['Expires']=header
                        elif "Allow:" in header:
                                sipheaders['Allow']=header
                        elif "Content-Lenght:" in header:
                                sipheaders['Lenght']=header
                        elif "Authorization:" in header:
                                sipheaders['Authorization']=header

                if "REGISTER" in sip[0]:
			if sipheaders['Authorization'] != "":
                              OK=self.okmessage(sipheaders,sip)
			      self.tx(host, port, OK)
                        else:
                              Unauthorized=self.unauthorizedmessage(sipheaders)
			      self.tx(host, port, Unauthorized)
                if "INVITE" in sip[0]:
                        if sipheaders['Authorization'] != "":
                              Try=self.trymessage(sipheaders)
                              self.tx(host, port, Try)
                              Ringing=self.ringingmessage(sipheaders)
                              self.tx(host, port, Ringing)
                        else:
                              Proxyauth=self.proxyauthenticationrequiredmessage(sipheaders)
                              self.tx(host, port, Proxyauth)
                if "BYE" in sip[0]:
                        OK=self.okmessage(sipheaders,sip)
                        self.tx(host, port, OK)
                if "ACK" in sip[0]:
                        pass
                if "CANCEL" in sip[0]:
                        CANCEL=self.cancelingmessage(sipheaders)
                        self.tx(host, port, CANCEL)
                else:
                        Notsupported=self.notsupportedmessage(sipheaders)
			self.tx(host, port, Notsupported)
	
		##########################################################################################

	### START CUSTOM FUNCTIONS ###################################################################

        def unauthorizedmessage (self, sipheaders):
            Unauthorized="SIP/2.0 401 Unauthorized\r\n"
            Unauthorized+=sipheaders['Via']+"\r\n"
            Unauthorized+=sipheaders['From']+"\r\n"
            Unauthorized+=sipheaders['To']+"\r\n"
            Unauthorized+=sipheaders['CallID']+"\r\n"
            Unauthorized+="CSeq: 1 REGISTER\r\n"
            Unauthorized+='WWW-Authenticate: Digest realm="sipplugin.com", nonce="ea9c8e88gf84f1tec4342ae6cbe5a359"\r\n'
            Unauthorized+="Server: OpenSER\r\n"
            Unauthorized+="Content-Length: 0\r\n\r\n"

            return Unauthorized;

        def okmessage (self, sipheaders, sip):
            OK="SIP/2.0 200 OK\r\n"
            OK+=sipheaders['Via']+"\r\n"
            OK+=sipheaders['From']+"\r\n"
            OK+=sipheaders['To'] + "\r\n"
            OK+=sipheaders['CallID']+"\r\n"
            if "BYE" in sip[0]:
                    OK+="CSeq: 2 BYE\r\n"
            else:
                    OK+="CSeq: 2 REGISTER\r\n"
            OK+=sipheaders['Contact']+"\r\n"
            OK+="Server: OpenSER\r\n"
	    OK+="Content-Length: 0\r\n\r\n"

            return OK;

        def ringingmessage (self, sipheaders):
            Ringing="SIP/2.0 180 Ringing\r\n"
            Ringing+=sipheaders['Via']+"\r\n"
            Ringing+=sipheaders['From']+"\r\n"
            Ringing+=sipheaders['To'] + "\r\n"
            Ringing+=sipheaders['CallID']+"\r\n"
            Ringing+="CSeq: 2 INVITE\r\n"
            Ringing+=sipheaders['Contact']+"\r\n"
            Ringing+="Allow: INVITE,ACK,BYE,CANCEL,REGISTER\r\n"
            Ringing+="Content-Length: 0\r\n\r\n"

            return Ringing;

        def notsupportedmessage (self, sipheaders):
            Notsupported="SIP/2.0 489 Event Package Not Supported\r\n"
            Notsupported+=sipheaders['Via']+"\r\n"
            Notsupported+=sipheaders['From']+"\r\n"
            Notsupported+=sipheaders['To'] + "\r\n"
            Notsupported+=sipheaders['CallID']+"\r\n"
            Notsupported+="Allow: INVITE,ACK,BYE,CANCEL,REGISTER\r\n"
            Notsupported+="Content-Length: 0\r\n\r\n"    
            
            return Notsupported;
 
        def proxyauthenticationrequiredmessage (self, sipheaders):
            Proxyauth="SIP/2.0 407 Proxy Authentication Required\r\n"
            Proxyauth+=sipheaders['Via']+"\r\n"
            Proxyauth+=sipheaders['From']+"\r\n"
            Proxyauth+=sipheaders['To'] + "\r\n"
            Proxyauth+=sipheaders['CallID']+"\r\n"
            Proxyauth+="CSeq: 1 INVITE\r\n"           
            Proxyauth+='Proxy-Authenticate: Digest realm="sipplugin.com", nonce="587993360c7c45282001e7b9552638d9509ed85f"\r\n'
            Proxyauth+="Server: OpenSER\r\n"
            Proxyauth+="Content-Length: 0\r\n\r\n"

            return Proxyauth;
 
        def trymessage (self, sipheaders):
            Try="SIP/2.0 100 Giving a try\r\n"
            Try+=sipheaders['Via']+"\r\n"
            Try+=sipheaders['From']+"\r\n"
            Try+=sipheaders['To'] + "\r\n"
            Try+=sipheaders['CallID']+"\r\n"
            Try+="CSeq: 2 INVITE\r\n"
            Try+="Server: OpenSER\r\n"
            Try+="Content-Length: 0\r\n\r\n"

            return Try;
 
        def cancelingmessage (self, sipheaders):
            Canceling="SIP/2.0 200 canceling\r\n"
            Canceling+=sipheaders['Via']+"\r\n"
            Canceling+=sipheaders['From']+"\r\n"
            Canceling+=sipheaders['To'] + "\r\n"
            Canceling+=sipheaders['CallID']+"\r\n"
            Canceling+="CSeq: 2 CANCEL\r\n"
            Canceling+="Server: OpenSER\r\n"
            Canceling+="Content-Length: 0\r\n\r\n"

            return Canceling;

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
