# HoneyPy Copyright (C) 2013-2016 foospidy
# https://github.com/foospidy/HoneyPy
# See LICENSE for details
# HoneyPy HoneyDB logger

import sys
import hashlib
import urllib
import requests
from twisted.python import log

# prevent creation of compiled bytecode files
sys.dont_write_bytecode = True

def post_log(useragent, url, api_id, api_key, date, time, date_time, millisecond, session, protocol, event, local_host, local_port, service, remote_host, remote_port, data):
	# post events to honeydb logger
	h = hashlib.md5()
	h.update(data)

	headers = { 'User-Agent': useragent }
	# applying [:-3] to time to truncate millisecond
	data    = {
		'date': date,
		'time': time,
		'date_time': date_time,
		'millisecond': str(millisecond)[:-3],
		'api_id': api_id,
		'api_key': api_key,
		'session': session,
		'protocol': protocol,
		'event': event,
		'local_host': local_host,
		'local_port': local_port,
		'service': service,
		'remote_host': remote_host,
		'remote_port': remote_port,
		'data': data,
		'bytes': str(len(data)),
		'data_hash': h.hexdigest()
	}

	try:
		r       = requests.post(url, headers=headers, data=data)
		page    = r.text
		
		log.msg('Post event to honeydb, response: %s' % (str(page).strip()))
	except Exception as e:
		log.msg('Error posting to honeydb: %s' % (str(e.message).strip()))
