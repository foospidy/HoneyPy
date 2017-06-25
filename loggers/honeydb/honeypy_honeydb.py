# HoneyPy Copyright (C) 2013-2017 foospidy
# https://github.com/foospidy/HoneyPy
# See LICENSE for details
# HoneyPy HoneyDB logger

import sys
import hashlib
import urllib
import requests
import itertools
import operator
import json
from uuid import getnode
from twisted.python import log

# prevent creation of compiled bytecode files
sys.dont_write_bytecode = True

def get_hmac(useragent, url, api_id, api_key):
	headers = { 'User-Agent': useragent, 'X-HoneyDb-ApiId': api_id, 'X-HoneyDb-ApiKey': api_key }

	try:
		r = requests.get(url, headers=headers, timeout=3)
		j = json.loads(r.text)
		
		if 'Success' == j['status']:
			log.msg('HoneyDB logger: hmac received with message: {}'.format(j['hmac_message']))
			return True, j['hmac_hash'], j['hmac_message']
		else:
			raise Exception(j['status'])
		
	except Exception as e:
		log.msg('HoneyDB logger: Error retrieving hmac: %s' % (str(e.message).strip()))
		return False, None, None

def post_log(useragent, url, hmac_hash, hmac_message, date, time, date_time, millisecond, session, protocol, event, local_host, local_port, service, remote_host, remote_port, data):
	# post events to honeydb logger
	h = hashlib.md5()
	h.update(data)

	mac_addr = ':'.join((itertools.starmap(operator.add, zip(*([iter("%012X" % getnode())] * 2)))))

	headers = { 'User-Agent': useragent, "Content-Type": "application/json" }
	# applying [:-3] to time to truncate millisecond
	data    = {
		'date': date,
		'time': time,
		'date_time': date_time,
		'millisecond': str(millisecond)[:-3],
		'hmac_hash': hmac_hash,
		'hmac_message': hmac_message,
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
		'data_hash': h.hexdigest(),
		'node': mac_addr
	}

	try:
		r        = requests.post(url, headers=headers, json=data, timeout=10)
		response = json.loads(r.text)

		log.msg('Post event to honeydb, response: %s' % (str(response).strip().replace('\n', ' ')))

		return response['status']

	except Exception as e:
		log.msg('HoneyDB logger, post error: %s' % (str(e.message).strip().replace('\n', ' ')))

		return 'Error'
