# HoneyPy Copyright (C) 2013-2017 foospidy
# https://github.com/foospidy/HoneyPy
# See LICENSE for details
# HoneyPy HoneyDB logger

import sys
import hashlib
import itertools
import operator
import json
import random
import requests
from uuid import getnode
from twisted.python import log

# prevent creation of compiled bytecode files
sys.dont_write_bytecode = True


def process(config, section, parts, time_parts, useragent):
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
        # class varaibles for HoneyDB
    got_hmac = False
    hmac_hash = None
    hmac_message = None

    if hmac_hash is None:
        log.msg('HoneyDB logger: retrieving initial hmac.')
        got_hmac, hmac_hash, hmac_message = get_hmac(useragent, config.get('honeydb', 'hmac_url'), config.get('honeydb', 'api_id'), config.get('honeydb', 'api_key'))

    for i in range(1, 4):
        log.msg('HoneyDB logger: post attempt {}.'.format(i))

        if got_hmac:
            response = None

            if parts[4] == 'TCP':
                if len(parts) == 11:
                    parts.append('')  # no data for CONNECT events

                response = post(useragent, config.get('honeydb', 'url'), hmac_hash, hmac_message, parts[0], time_parts[0], parts[0] + ' ' + time_parts[0], time_parts[1], parts[3], parts[4], parts[5], parts[6], parts[7], parts[8], parts[9], parts[10], parts[11])

            else:
                # UDP splits differently (see comment section above)
                if len(parts) == 12:
                    parts.append('')  # no data sent

                response = post(useragent, config.get('honeydb', 'url'), hmac_hash, hmac_message, parts[0], time_parts[0], parts[0] + ' ' + time_parts[0], time_parts[1], parts[4], parts[5], parts[6], parts[7], parts[8], parts[9], parts[10], parts[11], parts[12])

            if response == 'Success':
                break

            else:
                if response == 'Invalid HMAC' and i < 3:
                    log.msg('HoneyDB logger: hmac invalid, retrieving new hmac.')
                    got_hmac, hmac_hash, hmac_message = get_hmac(useragent, config.get('honeydb', 'hmac_url'), config.get('honeydb', 'api_id'), config.get('honeydb', 'api_key'))

                elif response == 'Invalid HMAC' and i == 3:
                    log.msg('HoneyDB logger: hmac invalid, 3 failed attempts, giving up.')

                elif i < 3:
                    log.msg('HoneyDB logger: {}, make another attempt.'.format(response))

                else:
                    log.msg('HoneyDB logger: {}, 3 failed attempts, giving up.'.format(response))




def get_hmac(useragent, url, api_id, api_key):
    headers = {'User-Agent': useragent, 'X-HoneyDb-ApiId': api_id, 'X-HoneyDb-ApiKey': api_key}
    url = 'https://riskdiscovery.com/honeydb/api/hmac'

    try:
        r = requests.get(url, headers=headers, timeout=3)
        j = json.loads(r.text)

        if j['status'] == 'Success':
            log.msg('HoneyDB logger: hmac received with message: {}'.format(j['hmac_message']))
            return True, j['hmac_hash'], j['hmac_message']
        else:
            raise Exception(j['status'])

    except Exception as e:
        log.msg('HoneyDB logger: Error retrieving hmac: %s' % (str(e.message).strip()))
        return False, None, None

def post(useragent, url, hmac_hash, hmac_message, date, time, date_time, millisecond, session, protocol, event, local_host, local_port, service, remote_host, remote_port, data):
    # post events to honeydb logger
    h = hashlib.md5()
    h.update(data)

    mac_addr = ':'.join((itertools.starmap(operator.add, zip(*([iter("%012X" % getnode())] * 2)))))
    urls = ('https://service.us.apiconnect.ibmcloud.com/gws/apigateway/api/046b612677d0c8b57420ea0e9b3cc4960a21b6bfea00a0a22a63ddb81aae64ab/honeydb/collector',
            'https://z17veyvn82.execute-api.us-east-1.amazonaws.com/prod/collector')
    url = random.choice(urls)

    headers = {'User-Agent': useragent, "Content-Type": "application/json"}
    # applying [:-3] to time to truncate millisecond
    data = {
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
        r = requests.post(url, headers=headers, json=data, timeout=10)
        response = json.loads(r.text)

        log.msg('Post event to honeydb, response: %s' % (str(response).strip().replace('\n', ' ')))

        return response['status']

    except Exception as e:
        log.msg('HoneyDB logger, post error: %s' % (str(e.message).strip().replace('\n', ' ')))

        return 'Error'
