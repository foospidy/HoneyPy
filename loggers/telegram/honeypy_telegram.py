# HoneyPy Copyright (C) 2013-2017 foospidy
# https://github.com/foospidy/HoneyPy
# See LICENSE for details
# HoneyPy telegram module by aancw

import json
import urllib3
import certifi


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
        post(config, parts[8], parts[9])
    else:
        # UDP splits differently (see comment section above)
        post(config, parts[9], parts[10])

def get_chat_id(bot_id):
    try:
        https = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
        r = https.request('GET', 'https://api.telegram.org/bot' + bot_id + '/getUpdates')
        result_dump = json.loads(r.data)
        chat_id = result_dump['result'][0]['message']['chat']['id']
        return chat_id
    except urllib3.exceptions.SSLError as err:
        print('[ERROR] Telegram SSL error', err)

def post(honeypycfg, service, clientip):
    bot_id = honeypycfg.get('telegram', 'bot_id')
    message = service + ' Possible '  + service + ' attack from ' + clientip + ' https://riskdiscovery.com/honeydb/#host/' + clientip
    chat_id = get_chat_id(bot_id)

    try:
        https = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
        r = https.request('GET', 'https://api.telegram.org/bot' + bot_id + '/sendMessage?chat_id=' + str(chat_id) + '&text=' + message)
    except urllib3.exceptions.SSLError as err:
        print('[ERROR] Telegram SSL error', err)
