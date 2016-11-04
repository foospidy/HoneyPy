# HoneyPy Copyright (C) 2013-2016 foospidy
# https://github.com/foospidy/HoneyPy
# See LICENSE for details
# HoneyPy Slack Integration

import sys
import requests
from twisted.python import log

# prevent creation of compiled bytecode files
sys.dont_write_bytecode = True

def post_slack(honeypycfg, service, clientip):
    headers = { 'Content-type': 'application/json', 'User-Agent': honeypycfg.get('honeypy', 'useragent') }
    data    = '{"text": "' + honeypycfg.get('honeypy', 'nodename') + ': Possible *' + service + '* attack from ' + clientip + ' <https://riskdiscovery.com/honeydb/#host/' + clientip + '>"}'

    url     = honeypycfg.get('slack', 'webhook_url')
    r       = requests.post(url, headers=headers, data=data)

    if r.status_code != requests.codes.ok:
        log.msg('Error posting to Slack: %s' % str(r.status_code))
