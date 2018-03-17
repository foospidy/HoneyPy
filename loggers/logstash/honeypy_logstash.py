# HoneyPy Copyright (C) 2013-2017 foospidy
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

def process(config, section, parts, time_parts):
        # TCP
        #	parts[0]: date
        #	parts[1]: time_parts
        #	parts[2]: plugin
        #	parts[3]: session
        #	parts[4]: protocol
        #	parts[5]: event
        #	parts[6]: local_host
        #	parts[7]: local_port
        #	parts[8]: service
        #	parts[9]: remote_host
        #	parts[10]: remote_port
        #	parts[11]: data
        # UDP
        #	parts[0]: date
        #	parts[1]: time_parts
        #	parts[2]: plugin string part
        #	parts[3]: plugin string part
        #	parts[4]: session
        #	parts[5]: protocol
        #	parts[6]: event
        #	parts[7]: local_host
        #	parts[8]: local_port
        #	parts[9]: service
        #	parts[10]: remote_host
        #	parts[11]: remote_port
        #	parts[12]: data

    if parts[4] == 'TCP':
        if len(parts) == 11:
            parts.append('')  # no data for CONNECT events

        post(config.get(section, 'host'), config.get(section, 'port'), parts[0], time_parts[0], parts[0] + ' ' + time_parts[0], time_parts[1], parts[3], parts[4], parts[5], parts[6], parts[7], parts[8], parts[9], parts[10], parts[11])
    else:
        # UDP splits differently (see comment section above)
        if len(parts) == 12:
            parts.append('')  # no data sent

        post(config.get(section, 'host'), config.get(section, 'port'), parts[0], time_parts[0], parts[0] + ' ' + time_parts[0], time_parts[1], parts[4], parts[5], parts[6], parts[7], parts[8], parts[9], parts[10], parts[11], parts[12])


def post(host, port, date, time, date_time, millisecond, session, protocol, event, local_host, local_port, service, remote_host, remote_port, data):
    # post events to honeydb logger
    h = hashlib.md5()
    h.update(data)

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
