# HoneyPy Copyright (C) 2013-2016 foospidy
# https://github.com/foospidy/HoneyPy
# See LICENSE for details
# HoneyPy logstash logger

import sys
import hashlib
import socket
import json
from twisted.python import log

# prevent creation of compiled bytecode files
sys.dont_write_bytecode = True

def post_logstash(useragent, host, port, date, time, date_time, millisecond, session, protocol, event, local_host, local_port, service, remote_host, remote_port, data):
	# post events to honeydb logger
	h = hashlib.md5()
	h.update(data)

	headers = { 'User-Agent': useragent }
	# applying [:-3] to time to truncate millisecond
	data = {
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
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		sock.connect((host, int(port)))
		
		bytes_sent = sock.send(json.dumps(data))

		sock.close()

		log.msg('Post event to logstash! (%s bytes)' % str(bytes_sent))

	except socket.error, msg:
			log.msg('[ERROR] post_logstash, socket.error: %s' % msg[1])

	except Exception as e:
		log.msg('Error posting to logstash: %s' % (str(e.message).strip()))
