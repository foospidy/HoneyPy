# HoneyPy Copyright (C) 2013-2017 foospidy
# https://github.com/foospidy/HoneyPy
# See LICENSE for details
# HoneyPy twitter module

from twitter import Twitter
from twitter.oauth import OAuth
from twisted.python import log

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


def post(honeypycfg, service, clientip):

    ck = honeypycfg.get('twitter', 'consumerkey')
    cs = honeypycfg.get('twitter', 'consumersecret')
    ot = honeypycfg.get('twitter', 'oauthtoken')
    os = honeypycfg.get('twitter', 'oauthsecret')

    t = Twitter(auth=OAuth(ot, os, ck, cs))
    nodename = honeypycfg.get('honeypy', 'nodename')

    try:
        t.statuses.update(status=nodename + ': #' + service + ' Possible '  + service + ' attack from ' + clientip + ' https://riskdiscovery.com/honeydb/#host/' + clientip)
    except Exception, err:
        log.msg('Error posting to Twitter: %s' % err)
