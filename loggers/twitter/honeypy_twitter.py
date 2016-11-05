# HoneyPy Copyright (C) 2013-2016 foospidy
# https://github.com/foospidy/HoneyPy
# See LICENSE for details
# HoneyPy twitter module

from twitter import Twitter
from twitter.oauth import OAuth
from twisted.python import log

def post_tweet(honeypycfg, service, clientip):

	ck = honeypycfg.get('twitter', 'consumerkey')
	cs = honeypycfg.get('twitter', 'consumersecret')
	ot = honeypycfg.get('twitter', 'oauthtoken')
	os = honeypycfg.get('twitter', 'oauthsecret')

	t        = Twitter(auth=OAuth(ot, os, ck, cs))
	nodename = honeypycfg.get('honeypy', 'nodename')

	try:
		t.statuses.update(status=nodename + ': #' + service + ' Possible '  + service + ' attack from ' + clientip + ' https://riskdiscovery.com/honeydb/#host/' + clientip)
	except Exception, err:
		log.msg('Error posting to Twitter: %s' % err)
