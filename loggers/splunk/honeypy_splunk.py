# HoneyPy Copyright (C) 2013-2016 foospidy
# https://github.com/foospidy/HoneyPy
# See LICENSE for details

import sys
import hashlib
import urllib
import requests
from datetime import datetime
from twisted.python import log

# prevent creation of compiled bytecode files
sys.dont_write_bytecode = True

def post_splunk(username, password, useragent, url, date, time, date_time, millisecond, session, protocol, event, local_host, local_port, service, remote_host, remote_port, data):
	h = hashlib.md5()
	h.update(data)

	date_time = datetime.strptime(date_time,"%Y-%m-%d %H:%M:%S").isoformat()

	headers = { 'User-Agent': useragent, "Content-Type": "application/json" }
	# applying [:-3] to time to truncate millisecond
	data    = {
		'date': date,
		'time': time,
		'date_time': date_time,
		'millisecond': str(millisecond)[:-3],
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
		r       = requests.post(url, headers=headers, data=data, auth=(username, password), verify=False)
		page    = r.text

		log.msg('Post event to splunk, response: %s' % (str(page).strip()))
	except Exception as e:
		log.msg('Error posting to splunk: %s' % (str(e.message).strip()))
