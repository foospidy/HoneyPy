# module for honeydb logger
import sys
import hashlib
import urllib
import urllib2

# prevent creation of compiled bytecode files
sys.dont_write_bytecode = True

def logger(url, secret, date, time, date_time, millisecond, event, local_host, local_port, service, remote_host, remote_port, data):
	# post events to honedb logger
	h = hashlib.md5()
	h.update(data)

	# applying [:-3] to time to truncate microsecond
	d = urllib.urlencode([('date', date), ('time', time), ('date_time', date_time), ('millisecond', str(millisecond)[:-3]), ('s', secret), ('event', event), ('local_host', local_host), ('local_port', local_port), ('service', service), ('remote_host', remote_host), ('remote_port', remote_port), ('data', data), ('bytes', str(len(data))), ('data_hash', h.hexdigest())])

	try:
		print url
		req      = urllib2.Request(url, d, {'User-Agent':'HoneyPy'})
		response = urllib2.urlopen(req)
		page     = response.read()

		# hmmmm, maybe later...
		#honeylogger.info('Post event to honeydb, response: %s' % (page))
	except urllib2.URLError, e:
		#honeylogger.debug('Error posting to honeydb: %s %s' % (str(e.code), str(e.reason)))
		print 'Error posting to honeydb: %s' % (str(e.reason))
