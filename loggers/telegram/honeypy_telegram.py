# HoneyPy Copyright (C) 2013-2016 foospidy
# https://github.com/foospidy/HoneyPy
# See LICENSE for details
# HoneyPy telegram module by aancw

import urllib3
import certifi
import sys
import json
from twisted.python import log

def get_chat_id(bot_id):
    try:
        https = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
        r = https.request('GET', 'https://api.telegram.org/bot' + bot_id + '/getUpdates')
        result_dump = json.loads(r.data)
        chat_id = result_dump['result'][0]['message']['chat']['id']
        return chat_id
    except urllib3.exceptions.SSLError as err:
        print('[ERROR] Telegram SSL error', err)

def send_telegram_message(honeypycfg, service, clientip):
    bot_id = honeypycfg.get('telegram', 'bot_id')
    message = service + ' Possible '  + service + ' attack from ' + clientip + ' https://riskdiscovery.com/honeydb/#host/' + clientip
    chat_id = get_chat_id(bot_id)

    try:
        https = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
        r = https.request('GET', 'https://api.telegram.org/bot' + bot_id + '/sendMessage?chat_id=' + str(chat_id) + '&text=' + message)
    except urllib3.exceptions.SSLError as err:
        print('[ERROR] Telegram SSL error', err)
