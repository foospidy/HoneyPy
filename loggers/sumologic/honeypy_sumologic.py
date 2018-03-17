# HoneyPy Copyright (C) 2013-2017 foospidy
# https://github.com/foospidy/HoneyPy
# See LICENSE for details
import sys
import hashlib
from datetime import datetime
import requests
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
    url = config.get(section, 'url')
    custom_source_host = config.get(section, 'custom_source_host')
    custom_source_name = config.get(section, 'custom_source_name')
    custom_source_category = config.get(section, 'custom_source_category')

    if parts[4] == 'TCP':
        if len(parts) == 11:
            parts.append('')  # no data for CONNECT events

        post(custom_source_host, custom_source_name, custom_source_category, url, parts[0], time_parts[0], parts[0] + ' ' + time_parts[0], time_parts[1], parts[3], parts[4], parts[5], parts[6], parts[7], parts[8], parts[9], parts[10], parts[11])
    else:
        # UDP splits differently (see comment section above)
        if len(parts) == 12:
            parts.append('')  # no data sent

        post(custom_source_host, custom_source_name, custom_source_category, url, parts[0], time_parts[0], parts[0] + ' ' + time_parts[0], time_parts[1], parts[4], parts[5], parts[6], parts[7], parts[8], parts[9], parts[10], parts[11], parts[12])


def post(custom_source_host, custom_source_name, custom_source_category, url, date, time, date_time, millisecond, session, protocol, event, local_host, local_port, service, remote_host, remote_port, data):
    useragent = None
    h = hashlib.md5()
    h.update(data)

    date_time = datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S").isoformat()

    headers = {'User-Agent': useragent, "Content-Type": "application/json"}

    if custom_source_host:
        headers.update({'X-Sumo-Host' : custom_source_host})

        if custom_source_name:
            headers.update({'X-Sumo-Name' : custom_source_name})

        if custom_source_category:
            headers.update({'X-Sumo-Category' : custom_source_category})

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
        r = requests.post(url, headers=headers, json=data, verify=True, timeout=3)
        page = r.text
        log.msg('Post event to sumologic, response: %s' % (str(page).strip()))
    except Exception as e:
        log.msg('Error posting to sumologic: %s' % (str(e.message).strip()))
 