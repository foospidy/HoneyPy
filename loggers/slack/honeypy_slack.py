# HoneyPy Copyright (C) 2013-2017 foospidy
# https://github.com/foospidy/HoneyPy
# See LICENSE for details
# HoneyPy Slack Integration

import sys
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

    if parts[4] == 'TCP' and parts[5] == 'CONNECT':
        post(config, parts[8], parts[9])
    elif parts[6] == 'RX':
        # UDP splits differently (see comment section above)
        post(config, parts[9], parts[10])

def post(honeypycfg, service, clientip):
    useragent = None
    headers = {'Content-type': 'application/json', 'User-Agent': useragent}
    data = '{"text": "' + honeypycfg.get('honeypy', 'nodename') + ': Possible *' + service + '* attack from ' + clientip + ' <https://riskdiscovery.com/honeydb/#host/' + clientip + '>"}'

    url = honeypycfg.get('slack', 'webhook_url')
    r = requests.post(url, headers=headers, data=data, timeout=3)

    if r.status_code != requests.codes.ok:
        log.msg('Error posting to Slack: %s' % str(r.status_code))
