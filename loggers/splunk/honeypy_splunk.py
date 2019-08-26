# HoneyPy Copyright (C) 2013-2019 foospidy
# https://github.com/foospidy/HoneyPy
# See LICENSE for details

import sys
import hashlib
from datetime import datetime
import time
from twisted.python import log
import requests

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

        post(config, parts[0] + ' ' + time_parts[0], time_parts[1], parts[3], parts[4], parts[5], parts[6], parts[7], parts[8], parts[9], parts[10], parts[11])
    else:
        # UDP splits differently (see comment section above)
        if len(parts) == 12:
            parts.append('')  # no data sent

        post(config, parts[0] + ' ' + time_parts[0], time_parts[1], parts[4], parts[5], parts[6], parts[7], parts[8], parts[9], parts[10], parts[11], parts[12])

def post(config, date_time, millisecond, session, protocol, event, local_host, local_port, service, remote_host, remote_port, data):
    useragent = config.get('honeypy', 'useragent')
    host = config.get('honeypy', 'nodename') or 'honeypy'
    url = config.get('splunk', 'url')
    token = config.get('splunk', 'token')

    index = config.get('splunk', 'index')
    source = config.get('splunk', 'source')
    sourcetype = config.get('splunk', 'sourcetype')

    h = hashlib.md5()
    h.update(data)

    date_time_w_millisecond = date_time + '.' + str(millisecond)
    complete_date_time = datetime.strptime(date_time_w_millisecond, "%Y-%m-%d %H:%M:%S.%f").isoformat() + 'Z'

    epoch = str(int(time.mktime(time.strptime(date_time_w_millisecond, "%Y-%m-%d %H:%M:%S.%f")))) + '.' + str(millisecond)

    headers = {
        'User-Agent': useragent,
        "Content-Type": "application/json",
        "Authorization": "Splunk " + token
    }

    eventdata = {
        'date_time': complete_date_time,
        'session_id': session,
        'protocol': protocol,
        'event': event,
        'dest_ip': local_host,
        'dest_port': local_port,
        'service': service,
        'src_ip': remote_host,
        'src_port': remote_port,
        'data': data,
        'bytes': str(len(data)),
        'data_hash': h.hexdigest()
    }

    parentdata = {
        'time': epoch,
        'index': index,
        'source': source,
        'sourcetype': sourcetype,
        'host': host,
        'event': eventdata
    }

    try:
        r = requests.post(url, headers=headers, json=parentdata, verify=False, timeout=3)
        resp = r.text

        log.msg('Post event to Splunk, response: %s' % (str(resp).strip()))
    except Exception as e:
        log.msg('Error posting to Splunk: %s' % (str(e.message).strip()))
