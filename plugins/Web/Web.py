# HoneyPy Copyright (C) 2013-2017 foospidy
# https://github.com/foospidy/HoneyPy
# See LICENSE for details

from twisted.internet import protocol, reactor, endpoints
from twisted.python import log
import uuid

### START CUSTOM IMPORTS ###
from BaseHTTPServer import BaseHTTPRequestHandler
from StringIO import StringIO
import base64
############################

class Web(protocol.Protocol): ### Set custom protocol class name
	localhost   = None
	remote_host = None
	session     = None

	### START CUSTOM VARIABLES ###############################################################
	
	##########################################################################################
	
	# handle events
	def connectionMade(self):
		self.connect()

		### START CUSTOM CODE ####################################################################
		
		##########################################################################################

	def dataReceived(self, data):
		self.rx(data)

		### START CUSTOM CODE ####################################################################
		request         = HTTPRequest(data)
		response_header = 'HTTP/1.1 200 OK\nServer: Apache/2.4.10 (Debian)\nConnection: close\nContent-Type: text/html\n\n'
		response_body   = 'OK!\n'

		if None != request.path:
			if '/robots.txt' == request.path:
				response_header = 'HTTP/1.1 200 OK\nServer: Apache/2.4.10 (Debian)\nConnection: close\nContent-Type: text/plain\n\n'
				response_body   = 'User-agent: *\nDisallow: /customers\nDisallow: /users.txt\n'
				response        = '{}{}'.format(response_header, response_body)

			elif '/wp-login.php' == request.path:
				# todo: /wp-admin/setup-config.php
				wp_login_page = 'CjwhRE9DVFlQRSBodG1sPgoJPCEtLVtpZiBJRSA4XT4KCQk8aHRtbCB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCIgY2xhc3M9ImllOCIgbGFuZz0iZW4iPgoJPCFbZW5kaWZdLS0+Cgk8IS0tW2lmICEoSUUgOCkgXT48IS0tPgoJCTxodG1sIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIiBsYW5nPSJlbiI+Cgk8IS0tPCFbZW5kaWZdLS0+Cgk8aGVhZD4KCTxtZXRhIGh0dHAtZXF1aXY9IkNvbnRlbnQtVHlwZSIgY29udGVudD0idGV4dC9odG1sOyBjaGFyc2V0PVVURi04IiAvPgoJPHRpdGxlPldvcmRQcmVzcy5jb20gJmxzYXF1bzsgTG9nIEluPC90aXRsZT4KCTxsaW5rIHJlbD0nc3R5bGVzaGVldCcgaHJlZj0naHR0cHM6Ly9zMi53cC5jb20vd3AtYWRtaW4vY3NzL3dwY29tLmNzcz9tPTE0NjExNTc5MTBoJiMwMzg7dmVyc2lvbj00LjcuMycgdHlwZT0ndGV4dC9jc3MnIC8+CjxsaW5rIHJlbD0nZG5zLXByZWZldGNoJyBocmVmPScvL3MwLndwLmNvbScgLz4KPHNjcmlwdCB0eXBlPSJ0ZXh0L2phdmFzY3JpcHQiPgppZiAoIHdpbmRvdy50b3AgIT09IHdpbmRvdy5zZWxmICkgewoJaWYgKCB3aW5kb3cudG9wLmxvY2F0aW9uLmhvc3RuYW1lICE9PSB3aW5kb3cuc2VsZi5sb2NhdGlvbi5ob3N0bmFtZSB8fCB3aW5kb3cudG9wLmxvY2F0aW9uLnByb3RvY29sICE9PSB3aW5kb3cudG9wLmxvY2F0aW9uLnByb3RvY29sICkgewoJCXdpbmRvdy50b3AubG9jYXRpb24uaHJlZiA9IHdpbmRvdy5zZWxmLmxvY2F0aW9uLmhyZWY7Cgl9Cn0KPC9zY3JpcHQ+CjxzY3JpcHQgdHlwZT0ndGV4dC9qYXZhc2NyaXB0JyBzcmM9J2h0dHBzOi8vczEud3AuY29tL19zdGF0aWMvPz8tZUp6VEx5L1F6Y3hMemlsTlNTM1d6d0tpd3RMVW9rb29wWmRWcktPUFQ0RnVibVo2VVdKSnFsNXVaaDVRc1gydXJhR0ptWm1wa2JHbHVVVVdBQ1dxSUxrPSc+PC9zY3JpcHQ+CjxsaW5rIHJlbD0nc3R5bGVzaGVldCcgaWQ9J2FsbC1jc3MtMC0xJyBocmVmPSdodHRwczovL3MyLndwLmNvbS9fc3RhdGljLz8/LWVKelRMeS9RemN4THppbE5TUzNXVHk0dTFrOUpMTTdJVE03UEs5Ykx6Y3pUQTRybzZLTXJTU290S1VGWGtKZ0M1SUZsMC9LTGNuSEo1UmdhNU9HU3lrL1BSSkxMMU0vTEx3RzdBODdBb3FtOElEay9GeVJ1bjJ0cmFHSmhZV0ZvWVdacW1BVUFzQmRNY3c9PScgdHlwZT0ndGV4dC9jc3MnIG1lZGlhPSdhbGwnIC8+CjxsaW5rIHJlbD0iY2Fub25pY2FsIiBocmVmPSJodHRwczovL3dvcmRwcmVzcy5jb20vd3AtbG9naW4ucGhwIj4KCTxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+CgkJYm9keSwgZm9ybSAuaW5wdXQgewoJCQlmb250LWZhbWlseTogIk9wZW4gU2FucyIsICJIZWx2ZXRpY2EgTmV1ZSIsICJBcmlhbCIsIHNhbnM7CgkJfQoKCQlib2R5LmxvZ2luLnJlY292ZXItcGFzc3dvcmQsCgkJYm9keS5sb2dpbi5yZWNvdmVyLXBhc3N3b3JkLXN1Y2Nlc3MgewoJCQloZWlnaHQ6IGF1dG87CgkJCW1pbi1oZWlnaHQ6IDEwMCU7CgkJfQoKCQkKCQkjcmVjb3ZlcnkgewoJCQlwYWRkaW5nLWJvdHRvbTogMjRweDsKCQl9CgoJCS5yZWNvdmVyLXBhc3N3b3JkICNsb2dpbl9lcnJvciB7CgkJCXdpZHRoOiBhdXRvOwoJCX0KCgkJI2xvZ2luX2Vycm9yIHVsIHsKCQkJbGlzdC1zdHlsZTogc3F1YXJlIG91dHNpZGUgbm9uZTsKCQkJbWFyZ2luLWxlZnQ6IDE1cHg7CgkJfQoKCQkjbG9naW5fZXJyb3Igb2wgewoJCQkJCW1hcmdpbi1sZWZ0OiAyNXB4OwoJCQkJfQoKCQkubWVzc2FnZSBvbCB7CgkJCQkJbWFyZ2luOiAxMHB4IDBweCAxMHB4IDIwcHg7CgkJCQl9CgoJCSNsb2dpbl9lcnJvciBoMiwgI3JlY292ZXJ5IGgyIHsKCQkJcGFkZGluZy1ib3R0b206IDEwcHg7CgkJfQoKCQkjbG9naW5fZXJyb3IgaDMgewoJCQlwYWRkaW5nLWJvdHRvbTogNXB4OwoJCX0KCgkJI2xvZ2luX2Vycm9yIGgzIHsKCQkJbWFyZ2luLXRvcDogMTBweDsKCQl9CgoJCS5yZWNvdmVyLXBhc3N3b3JkICNyZWNvdmVyeSBoMiB7CgkJCW1hcmdpbi1ib3R0b206IDVweDsKCQl9CgkJLnJlY292ZXItcGFzc3dvcmQtc3VjY2VzcyAjcmVjb3ZlcnkgaDIgewoJCQltYXJnaW4tYm90dG9tOiAuNWVtOwoJCX0KCgkJLnJlY292ZXItcGFzc3dvcmQgI3JlY292ZXJ5IHAgewoJCQlsaW5lLWhlaWdodDogMS42OwoJCQlwYWRkaW5nLWJvdHRvbTogMTBweDsKCQkJYm9yZGVyLXRvcDogbm9uZTsKCQl9CgkJLnJlY292ZXItcGFzc3dvcmQtc3VjY2VzcyAjcmVjb3ZlcnkgcCB7CgkJCWxpbmUtaGVpZ2h0OiAxLjY7CgkJCXBhZGRpbmctYm90dG9tOiAxZW07CgkJfQoKCQkucmVjb3Zlcnktc3RhZ2UgewoJCQltYXJnaW46IDE0cHggMHB4IDI3cHggMHB4OwoJCX0KCQkubG9naW4gLnJlY292ZXJ5LXN0YWdlIGlucHV0W3R5cGU9InRleHQiXSB7CgkJCW1hcmdpbi1ib3R0b206IDVweDsKCQl9CgoJCS5yZWNvdmVyeS1vd25lcnNoaXAtbWVzc2FnZSB7CgkJCWJhY2tncm91bmQtY29sb3I6ICNmZmY7CgkJCS13ZWJraXQtYm94LXNoYWRvdzogMCAxcHggMnB4IHJnYmEoMCwwLDAsMC4xKTsKCQkJYm94LXNoYWRvdzogMCAxcHggMnB4IHJnYmEoMCwwLDAsMC4xKTsKCQkJcGFkZGluZzogN3B4IDE1cHggMCAxNXB4OwoJCQltYXJnaW46IDFlbSAwOwoJCQliYWNrZ3JvdW5kOiAjZmZmZmUwOwoJCX0KCgkJLnJlY292ZXJ5LWVycm9yLW1lc3NhZ2UgewoJCQlkaXNwbGF5OiBub25lOwoJCQliYWNrZ3JvdW5kLWNvbG9yOiAjZjE4MzFlOwoJCQktd2Via2l0LWJveC1zaGFkb3c6IDAgMXB4IDJweCByZ2JhKDAsMCwwLDAuMSk7CgkJCWJveC1zaGFkb3c6IDAgMXB4IDJweCByZ2JhKDAsMCwwLDAuMSk7CgkJCXBhZGRpbmc6IDdweCAxNXB4IDAgMTVweDsKCQkJbWFyZ2luOiAxZW0gMDsKCQkJYmFja2dyb3VuZDogI2YxODMxZTsKCQl9CgoJCS5yZWNvdmVyLXBhc3N3b3JkICNyZWNvdmVyeSB0ZXh0YXJlYSB7CgkJCXdpZHRoOiAxMDAlOwoJCQlib3gtc2l6aW5nOiBib3JkZXItYm94OwoJCQktbW96LWJveC1zaXppbmc6Ym9yZGVyLWJveDsKCQkJLXdlYmtpdC1ib3gtc2l6aW5nOmJvcmRlci1ib3g7CgkJCS1tcy1ib3gtc2l6aW5nOmJvcmRlci1ib3g7CgkJfQoKCQkucmVjb3Zlci1wYXNzd29yZCAjcmVjb3ZlcnkgLnJlY292ZXJ5LW93bmVyc2hpcC10aXRsZSB7CgkJCXBvc2l0aW9uOiByZWxhdGl2ZTsKCQkJcGFkZGluZy1ib3R0b206IDA7CgkJfQoKCQkucmVjb3Zlcnktb3duZXJzaGlwLWhlbHAgewoJCQlmbG9hdDogcmlnaHQ7CgkJCWZvbnQtc2l6ZTogMTFweDsKCQkJbWFyZ2luLXRvcDogLTEwcHg7CgkJCW1hcmdpbi1ib3R0b206IDVweDsKCQl9CgoJCS5yZWNvdmVyeS1vd25lcnNoaXAgewoJCQljbGVhcjogYm90aDsKCQl9CgoJCS5yZWNvdmVyeS1vd25lcnNoaXAtaGVscCB7CgkJCW1hcmdpbjogM3B4IDAgMCAwOwoJCX0KCgkJLnJlY292ZXJ5LW93bmVyc2hpcC1oZWxwLXRleHQgewoJCQlkaXNwbGF5OiBub25lOwoJCQlwb3NpdGlvbjogYWJzb2x1dGU7CgkJCQl0b3A6IDI1cHg7CgkJCQlyaWdodDogMDsKCQkJei1pbmRleDogMTAwOwoJCQlib3JkZXI6IDFweCBzb2xpZCAjZTZkYjU1OwoJCQliYWNrZ3JvdW5kLWNvbG9yOiBsaWdodHllbGxvdzsKCQkJd2lkdGg6IDI1MHB4OwoJCQlwYWRkaW5nOiA4cHg7CgkJCWJveC1zaGFkb3c6IDAgNHB4IDEwcHggLTFweCByZ2JhKDIwMCwgMjAwLCAyMDAsIDAuNyk7CgkJfQoKCQkuYWNjb3VudC1yZWNvdmVyeS1saW5rIHsKCQkJbWFyZ2luLWJvdHRvbTogMTZweDsKCQl9CgoJCS5sb2dpbiAjbm9zbXMgewoJCQlmb250LXNpemU6IDEzcHg7CgkJCXBhZGRpbmc6IDAgMjRweCAwOwoJCQltYXJnaW46IDE2cHggMCAwIDA7CgkJfQoJPC9zdHlsZT4KCQkJPHN0eWxlIHR5cGU9InRleHQvY3NzIj4KCQkJLnR3b3N0ZXAtbG9naW4tZGV0YWlscyBzdHJvbmcgewoJCQkJd2hpdGUtc3BhY2U6IG5vd3JhcDsKCQkJfQoJCTwvc3R5bGU+CgkJPG1ldGEgbmFtZT0idmlld3BvcnQiIGNvbnRlbnQ9IndpZHRoPWRldmljZS13aWR0aCIgLz4KCTxtZXRhIG5hbWU9ImFwcGxlLWl0dW5lcy1hcHAiIGNvbnRlbnQ9ImFwcC1pZD0zMzU3MDM4ODAiIC8+CQk8L2hlYWQ+Cgk8Ym9keSBjbGFzcz0ibG9naW4gbG9naW4tYWN0aW9uLWxvZ2luIHdwLWNvcmUtdWkgIGxvY2FsZS1lbiI+CgkJPGRpdiBpZD0ibG9naW4iPgoJCTxoMT48YSBocmVmPSJodHRwczovL3dvcmRwcmVzcy5jb20vIiB0aXRsZT0iV29yZFByZXNzLmNvbSIgdGFiaW5kZXg9Ii0xIj5Xb3JkUHJlc3MuY29tPC9hPjwvaDE+CgkKPGZvcm0gbmFtZT0ibG9naW5mb3JtIiBpZD0ibG9naW5mb3JtIiBhY3Rpb249Imh0dHBzOi8vd29yZHByZXNzLmNvbS93cC1sb2dpbi5waHAiIG1ldGhvZD0icG9zdCI+Cgk8cD4KCQk8bGFiZWwgZm9yPSJ1c2VyX2xvZ2luIj5Vc2VybmFtZSBvciBFbWFpbCBBZGRyZXNzPGJyIC8+CgkJPGlucHV0IHR5cGU9InRleHQiIG5hbWU9ImxvZyIgaWQ9InVzZXJfbG9naW4iIGNsYXNzPSJpbnB1dCIgdmFsdWU9IiIgc2l6ZT0iMjAiIC8+PC9sYWJlbD4KCTwvcD4KCTxwPgoJCTxsYWJlbCBmb3I9InVzZXJfcGFzcyI+UGFzc3dvcmQ8YnIgLz4KCQk8aW5wdXQgdHlwZT0icGFzc3dvcmQiIG5hbWU9InB3ZCIgaWQ9InVzZXJfcGFzcyIgY2xhc3M9ImlucHV0IiB2YWx1ZT0iIiBzaXplPSIyMCIgLz48L2xhYmVsPgoJPC9wPgoJCTxwIGNsYXNzPSJmb3JnZXRtZW5vdCI+PGxhYmVsIGZvcj0icmVtZW1iZXJtZSI+PGlucHV0IG5hbWU9InJlbWVtYmVybWUiIHR5cGU9ImNoZWNrYm94IiBpZD0icmVtZW1iZXJtZSIgdmFsdWU9ImZvcmV2ZXIiICBjaGVja2VkPSdjaGVja2VkJyAvPiBTdGF5IHNpZ25lZCBpbjwvbGFiZWw+PC9wPgoJPHAgY2xhc3M9InN1Ym1pdCI+CgkJPGlucHV0IHR5cGU9InN1Ym1pdCIgbmFtZT0id3Atc3VibWl0IiBpZD0id3Atc3VibWl0IiBjbGFzcz0iYnV0dG9uIGJ1dHRvbi1wcmltYXJ5IGJ1dHRvbi1sYXJnZSIgdmFsdWU9IkxvZyBJbiIgLz4KCQk8aW5wdXQgdHlwZT0iaGlkZGVuIiBuYW1lPSJyZWRpcmVjdF90byIgdmFsdWU9Imh0dHBzOi8vd29yZHByZXNzLmNvbS8iIC8+CgkJPGlucHV0IHR5cGU9ImhpZGRlbiIgbmFtZT0idGVzdGNvb2tpZSIgdmFsdWU9IjEiIC8+Cgk8L3A+CjwvZm9ybT4KCjxwIGlkPSJuYXYiPgo8YSBjbGFzcz0iY2xpY2stcmVnaXN0ZXIiIGhyZWY9Imh0dHBzOi8vd29yZHByZXNzLmNvbS9zdGFydD9yZWY9d3Bsb2dpbiI+UmVnaXN0ZXI8L2E+IHwgCTxhIGhyZWY9Imh0dHBzOi8vd29yZHByZXNzLmNvbS93cC1sb2dpbi5waHA/YWN0aW9uPWxvc3RwYXNzd29yZCI+TG9zdCB5b3VyIHBhc3N3b3JkPzwvYT4KPC9wPgoKPHNjcmlwdCB0eXBlPSJ0ZXh0L2phdmFzY3JpcHQiPgpmdW5jdGlvbiB3cF9hdHRlbXB0X2ZvY3VzKCl7CnNldFRpbWVvdXQoIGZ1bmN0aW9uKCl7IHRyeXsKZCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCd1c2VyX2xvZ2luJyk7CmQuZm9jdXMoKTsKZC5zZWxlY3QoKTsKfSBjYXRjaChlKXt9Cn0sIDIwMCk7Cn0KCndwX2F0dGVtcHRfZm9jdXMoKTsKaWYodHlwZW9mIHdwT25sb2FkPT0nZnVuY3Rpb24nKXdwT25sb2FkKCk7Cjwvc2NyaXB0PgoKCTxwIGlkPSJiYWNrdG9ibG9nIj48YSBocmVmPSJodHRwOi8vd29yZHByZXNzLmNvbS8iPiZsYXJyOyBCYWNrIHRvIFdvcmRQcmVzcy5jb208L2E+PC9wPgoJCgk8L2Rpdj4KCgkKCTxzY3JpcHQgdHlwZT0idGV4dC9qYXZhc2NyaXB0Ij4KLy8gPCFbQ0RBVEFbCihmdW5jdGlvbigpIHsKdHJ5ewogIGlmICggd2luZG93LmV4dGVybmFsICYmJ21zSXNTaXRlTW9kZScgaW4gd2luZG93LmV4dGVybmFsKSB7CiAgICBpZiAod2luZG93LmV4dGVybmFsLm1zSXNTaXRlTW9kZSgpKSB7CiAgICAgIHZhciBqbCA9IGRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoJ3NjcmlwdCcpOwogICAgICBqbC50eXBlPSd0ZXh0L2phdmFzY3JpcHQnOwogICAgICBqbC5hc3luYz10cnVlOwogICAgICBqbC5zcmM9Jy93cC1jb250ZW50L3BsdWdpbnMvaWUtc2l0ZW1vZGUvY3VzdG9tLWp1bXBsaXN0LnBocCc7CiAgICAgIHZhciBzID0gZG9jdW1lbnQuZ2V0RWxlbWVudHNCeVRhZ05hbWUoJ3NjcmlwdCcpWzBdOwogICAgICBzLnBhcmVudE5vZGUuaW5zZXJ0QmVmb3JlKGpsLCBzKTsKICAgIH0KICB9Cn1jYXRjaChlKXt9Cn0pKCk7Ci8vIF1dPgo8L3NjcmlwdD48c2NyaXB0IHNyYz0iaHR0cHM6Ly9zMS53cC5jb20vd3AtY29udGVudC9qcy9ib29tZXJhbmctYThjLm1pbi5qcz92PTAuNCI+PC9zY3JpcHQ+CjxzY3JpcHQ+CkJPT01SLmluaXQoIHsKCWJlYWNvbl91cmw6ICJodHRwczovL3BpeGVsLndwLmNvbS9ib29tLmdpZiIsCgliZWFjb25fdHlwZTogIkdFVCIsCglsb2c6IG51bGwsCglhOGNfY2xpY2tzOiB7CgkJJ2J1dHRvbi1wcmltYXJ5JzogewoJCQlzdGF0OiAnd3Bjb20ubG9naW4ubG9nX2luX2NsaWNrJywKCQkJaW5jbHVkZV9wYWdlX2xvYWQ6IHRydWUKCQl9LAoJCSdjbGljay1yZWdpc3Rlcic6IHsKCQkJc3RhdDogJ3dwY29tLmxvZ2luLnJlZ2lzdGVyX2NsaWNrJywKCQkJaW5jbHVkZV9wYWdlX2xvYWQ6IHRydWUKCQl9LAoJCSdjbGljay1iYWNrdG9ibG9nJzogewoJCQlzdGF0OiAnd3Bjb20ubG9naW4uYmFja3RvYmxvZ19jbGljaycsCgkJCWluY2x1ZGVfcGFnZV9sb2FkOiB0cnVlCgkJfQoJfQp9ICk7Cjwvc2NyaXB0PgoJCTxkaXYgY2xhc3M9ImNsZWFyIj48L2Rpdj4KCTwvYm9keT4KCTwvaHRtbD4KCQ=='
				response_body = base64.b64decode(wp_login_page)
				response      = '{}{}'.format(response_header, response_body)
			
			# normalize phpmyadmin paths by stripping /'s and lower case.
			elif request.path.lower().replace('/', '').endswith(('phpmyadmin', 'administratorphpmyadmin', 'sqlmyadmin', 'admindb', 'adminsqladmin', 'phpmyadminscriptssetup.php', 'dbwebadmin', 'adminphpmyadmin', 'myadmin', 'administratoradmin', 'administratorpma', 'administratordb' 'phpmyadminscriptssetup.inc.php', 'phpMyAdmin-2scriptssetup.php', 'myadminscriptssetup.php', 'pmascriptssetup.php', '2phpmyadmin', 'mysqldbadmin', 'mysqlsqlmanager', 'pma2011', 'pma2012', 'php-my-admin', 'pma', 'sqlwebsql')):
				phpmyadmin_login_page = 'CjxodG1sPgo8aGVhZD4KPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiB0eXBlPSJ0ZXh0L2NzcyIgaHJlZj0icG1hLmNzcyIgLz4KPHN0eWxlPmh0bWx7ZGlzcGxheTpibG9ja308L3N0eWxlPgo8Ym9keSBpZD0nbG9naW5mb3JtJz48ZGl2IGNsYXNzPSJjb250YWluZXIiPgogICAgPGNlbnRlcj48aW1nIHNyYz0iaHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL3BocG15YWRtaW4vcGhwbXlhZG1pbi9tYXN0ZXIvdGhlbWVzL29yaWdpbmFsL2ltZy9sb2dvX3JpZ2h0LnBuZyIgY2xhc3M9ImxvZ28iLz48L2NlbnRlcj4KICAgIDxoMT5XZWxjb21lIHRvIDxiZG8gZGlyPSJsdHIiIGxhbmc9ImVuIj5waHBNeUFkbWluPC9iZG8+PC9oMT48bm9zY3JpcHQ+CjxkaXYgY2xhc3M9ImVycm9yIj48aW1nIHNyYz0idGhlbWVzL2RvdC5naWYiIHRpdGxlPSIiIGFsdD0iIiBjbGFzcz0iaWNvbiBpY19zX2Vycm9yIiAvPiBKYXZhc2NyaXB0IG11c3QgYmUgZW5hYmxlZCBwYXN0IHRoaXMgcG9pbnQhPC9kaXY+PC9ub3NjcmlwdD4KICAgIDxiciAvPgogICAgPCEtLSBMb2dpbiBmb3JtIC0tPgogICAgPGZvcm0gbWV0aG9kPSJwb3N0IiBhY3Rpb249ImluZGV4LnBocCIgbmFtZT0ibG9naW5fZm9ybSIgYXV0b2NvbXBsZXRlPSJvZmYiPgogICAgICAgIDxmaWVsZHNldD4KICAgICAgICA8bGVnZW5kPkxvZyBpbjwvbGVnZW5kPgogICAgICAgICAgICA8ZGl2IGNsYXNzPSJpdGVtIj4KICAgICAgICAgICAgICAgIDxsYWJlbCBmb3I9ImlucHV0X3NlcnZlcm5hbWUiIHRpdGxlPSJZb3UgY2FuIGVudGVyIGhvc3RuYW1lL0lQIGFkZHJlc3MgYW5kIHBvcnQgc2VwYXJhdGVkIGJ5IHNwYWNlLiI+U2VydmVyOjwvbGFiZWw+CiAgICAgICAgICAgICAgICA8aW5wdXQgdHlwZT0idGV4dCIgbmFtZT0icG1hX3NlcnZlcm5hbWUiIGlkPSJpbnB1dF9zZXJ2ZXJuYW1lIiB2YWx1ZT0iIiBzaXplPSIyNCIgY2xhc3M9InRleHRmaWVsZCIgdGl0bGU9IllvdSBjYW4gZW50ZXIgaG9zdG5hbWUvSVAgYWRkcmVzcyBhbmQgcG9ydCBzZXBhcmF0ZWQgYnkgc3BhY2UuIiAvPgogICAgICAgICAgICA8L2Rpdj48ZGl2IGNsYXNzPSJpdGVtIj4KICAgICAgICAgICAgICAgIDxsYWJlbCBmb3I9ImlucHV0X3VzZXJuYW1lIj5Vc2VybmFtZTo8L2xhYmVsPgogICAgICAgICAgICAgICAgPGlucHV0IHR5cGU9InRleHQiIG5hbWU9InBtYV91c2VybmFtZSIgaWQ9ImlucHV0X3VzZXJuYW1lIiB2YWx1ZT0iIiBzaXplPSIyNCIgY2xhc3M9InRleHRmaWVsZCIvPgogICAgICAgICAgICA8L2Rpdj4KICAgICAgICAgICAgPGRpdiBjbGFzcz0iaXRlbSI+CiAgICAgICAgICAgICAgICA8bGFiZWwgZm9yPSJpbnB1dF9wYXNzd29yZCI+UGFzc3dvcmQ6PC9sYWJlbD4KICAgICAgICAgICAgICAgIDxpbnB1dCB0eXBlPSJwYXNzd29yZCIgbmFtZT0icG1hX3Bhc3N3b3JkIiBpZD0iaW5wdXRfcGFzc3dvcmQiIHZhbHVlPSIiIHNpemU9IjI0IiBjbGFzcz0idGV4dGZpZWxkIiAvPgogICAgICAgICAgICA8L2Rpdj4gICAgPGlucHV0IHR5cGU9ImhpZGRlbiIgbmFtZT0ic2VydmVyIiB2YWx1ZT0iMSIgLz48L2ZpZWxkc2V0PgogICAgICAgIDxmaWVsZHNldCBjbGFzcz0idGJsRm9vdGVycyI+CiAgICAgICAgICAgIDxpbnB1dCB2YWx1ZT0iR28iIHR5cGU9InN1Ym1pdCIgaWQ9ImlucHV0X2dvIiAvPjxpbnB1dCB0eXBlPSJoaWRkZW4iIG5hbWU9InRhcmdldCIgdmFsdWU9ImluZGV4LnBocCIgLz4KICAgICAgICA8L2ZpZWxkc2V0PgogICAgPC9mb3JtPgo8L2Rpdj48L2Rpdj48L2JvZHk+PC9odG1sPgo='
				response_body = base64.b64decode(phpmyadmin_login_page)
				response      = '{}{}'.format(response_header, response_body)
	
		# response with header and response_body
		response = '{}{}'.format(response_header, response_body)
		self.tx(response)
		# need to lose connection after each response.
		self.transport.loseConnection()

		##########################################################################################

	### START CUSTOM FUNCTIONS ###################################################################

	##############################################################################################

	def connect(self):
		self.local_host  = self.transport.getHost()
		self.remote_host = self.transport.getPeer()
		self.session     = uuid.uuid1()
		log.msg('%s %s CONNECT %s %s %s %s %s' % (self.session, self.remote_host.type, self.local_host.host, self.local_host.port, self.factory.name, self.remote_host.host, self.remote_host.port))

	def clientConnectionLost(self):
		self.transport.loseConnection()
	
	def tx(self, data):
		log.msg('%s %s TX %s %s %s %s %s %s' % (self.session, self.remote_host.type, self.local_host.host, self.local_host.port, self.factory.name, self.remote_host.host, self.remote_host.port, data.encode("hex")))
		self.transport.write(data)

	def rx(self, data):
		log.msg('%s %s RX %s %s %s %s %s %s' % (self.session, self.remote_host.type, self.local_host.host, self.local_host.port, self.factory.name, self.remote_host.host, self.remote_host.port, data.encode("hex")))

class pluginFactory(protocol.Factory):
	protocol = Web ### Set protocol to custom protocol class name
	
	def __init__(self, name=None):
		self.name = name or 'HoneyPy'

### START CUSTOM CLASSES ###################################################################
# from https://stackoverflow.com/questions/2115410/does-python-have-a-module-for-parsing-http-requests-and-responses
class HTTPRequest(BaseHTTPRequestHandler):
	def __init__(self, request_text):
		self.rfile = StringIO(request_text)
		self.raw_requestline = self.rfile.readline()
		self.error_code = self.error_message = None
		self.parse_request()

	def send_error(self, code, message):
		self.error_code = code
		self.error_message = message
##############################################################################################