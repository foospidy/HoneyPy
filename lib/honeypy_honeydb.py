# HoneyPy Copyright (C) 2013-2015 foospidy
# https://github.com/foospidy/HoneyPy
# See LICENSE for details
# HoneyPy HoneyDB logger

import sys
import hashlib
import urllib
import urllib2
from twisted.python import log

# prevent creation of compiled bytecode files
sys.dont_write_bytecode = True

def post_log(url, api_id, api_key, date, time, date_time, millisecond, session, protocol, event, local_host, local_port, service, remote_host, remote_port, data):
	# post events to honeydb logger
	h = hashlib.md5()
	h.update(data)

	# applying [:-3] to time to truncate millisecond
	d = urllib.urlencode([('date', date), ('time', time), ('date_time', date_time), ('millisecond', str(millisecond)[:-3]), ('api_id', api_id), ('api_key', api_key), ('session', session), ('protocol', protocol), ('event', event), ('local_host', local_host), ('local_port', local_port), ('service', service), ('remote_host', remote_host), ('remote_port', remote_port), ('data', data), ('bytes', str(len(data))), ('data_hash', h.hexdigest())])

	try:
		req      = urllib2.Request(url, d, {'User-Agent':'HoneyPy'})
		response = urllib2.urlopen(req)
		page     = response.read()

		# hmmmm, maybe later...
		log.msg('Post event to honeydb, response: %s' % (str(page).strip()))
	except urllib2.URLError, e:
		log.msg('Error posting to honeydb: %s' % (str(e.reason).strip()))
