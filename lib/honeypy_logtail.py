from twisted.python import log
from lib.followtail import FollowTail

class HoneyPyLogTail(FollowTail):
    # class varaibles for HoneyDB
    got_hmac     = False
    hmac_hash    = None
    hmac_message = None

    def lineReceived(self, line):
        parts = line.split()
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

        # only process actual events
        if len(parts) > 10:
            # this is a bit hacky - need to handle log message parsing better.
            if '[-]' != parts[2] and 'details:' != parts[0]:
                # time_parts[0]: time
                # time_parts[1]: millisecond
                # time_parts[2]: time zone
                time_parts = parts[1].split(',')

                try: 
                    # Twitter integration
                    if 'Yes' == self.config.get('twitter', 'enabled'):
                        from loggers.twitter.honeypy_twitter import post_tweet

                        if 'TCP' == parts[4]:
                            post_tweet(self.config, parts[8], parts[9])
                        else:
                            # UDP splits differently (see comment section above)
                            post_tweet(self.config, parts[9], parts[10])

                    # Slack integration
                    if 'Yes' == self.config.get('slack', 'enabled'):
                        from loggers.slack.honeypy_slack import post_slack

                        if 'TCP' == parts[4] and 'CONNECT' == parts[5]:
                            post_slack(self.config, parts[8], parts[9])
                        elif 'RX' == parts[6]:
                            # UDP splits differently (see comment section above)
                            post_slack(self.config, parts[9], parts[10])

                    # HoneyDB integration
                    if 'Yes' == self.config.get('honeydb', 'enabled'):
                        from loggers.honeydb.honeypy_honeydb import post_log, get_hmac

                        if None == self.hmac_hash:
                            log.msg('HoneyDB logger: retrieving initial hmac.')
                            self.got_hmac, self.hmac_hash, self.hmac_message = get_hmac(self.useragent, self.config.get('honeydb', 'hmac_url'), self.config.get('honeydb', 'api_id'), self.config.get('honeydb', 'api_key'))

                        for i in range(1,4):
                            log.msg('HoneyDB logger: post attempt {}.'.format(i))

                            if self.got_hmac:
                                response = None

                                if 'TCP' == parts[4]:
                                    if 11 == len(parts):
                                        parts.append('') # no data for CONNECT events

                                    response = post_log(self.useragent, self.config.get('honeydb', 'url'), self.hmac_hash, self.hmac_message, parts[0], time_parts[0], parts[0] + ' ' + time_parts[0], time_parts[1], parts[3], parts[4], parts[5], parts[6], parts[7], parts[8], parts[9], parts[10], parts[11])
                                    
                                else:
                                    # UDP splits differently (see comment section above)
                                    if 12 == len(parts):
                                        parts.append('') # no data sent

                                    response = post_log(self.useragent, self.config.get('honeydb', 'url'), self.hmac_hash, self.hmac_message, parts[0], time_parts[0], parts[0] + ' ' + time_parts[0], time_parts[1], parts[4], parts[5], parts[6], parts[7], parts[8], parts[9], parts[10], parts[11], parts[12])
                        
                                if 'Success' == response:
                                    break

                                else:
                                    if 'Invalid HMAC' == response and i < 3:
                                        log.msg('HoneyDB logger: hmac invalid, retrieving new hmac.')
                                        self.got_hmac, self.hmac_hash, self.hmac_message = get_hmac(self.useragent, self.config.get('honeydb', 'hmac_url'), self.config.get('honeydb', 'api_id'), self.config.get('honeydb', 'api_key'))
                                    
                                    elif 'Invalid HMAC' == response and i == 3:
                                        log.msg('HoneyDB logger: hmac invalid, 3 failed attempts, giving up.')
                                    
                                    elif i < 3:
                                        log.msg('HoneyDB logger: {}, make another attempt.'.format(response))
                                    
                                    else:   
                                        log.msg('HoneyDB logger: {}, 3 failed attempts, giving up.'.format(response))

                    # Logstash integration
                    if 'Yes' == self.config.get('logstash', 'enabled'):
                        from loggers.logstash.honeypy_logstash import post_logstash

                        if 'TCP' == parts[4]:
                            if 11 == len(parts):
                                parts.append('') # no data for CONNECT events

                            post_logstash(self.useragent, self.config.get('logstash', 'host'), self.config.get('logstash', 'port'), parts[0], time_parts[0], parts[0] + ' ' + time_parts[0], time_parts[1], parts[3], parts[4], parts[5], parts[6], parts[7], parts[8], parts[9], parts[10], parts[11])
                        else:
                            # UDP splits differently (see comment section above)
                            if 12 == len(parts):
                                parts.append('') # no data sent

                            post_logstash(self.useragent, self.config.get('logstash', 'host'), self.config.get('logstash', 'port'), parts[0], time_parts[0], parts[0] + ' ' + time_parts[0], time_parts[1], parts[4], parts[5], parts[6], parts[7], parts[8], parts[9], parts[10], parts[11], parts[12])

                    # Elasticsearch integration
                    if 'Yes' == self.config.get('elasticsearch', 'enabled'):
                        from loggers.elasticsearch.honeypy_elasticsearch import post_elasticsearch

                        if 'TCP' == parts[4]:
                            if 11 == len(parts):
                                parts.append('') # no data for CONNECT events

                            post_elasticsearch(self.useragent, self.config.get('elasticsearch', 'es_url'), parts[0], time_parts[0], parts[0] + ' ' + time_parts[0], time_parts[1], parts[3], parts[4], parts[5], parts[6], parts[7], parts[8], parts[9], parts[10], parts[11])
                        else:
                            # UDP splits differently (see comment section above)
                            if 12 == len(parts):
                                parts.append('') # no data sent

                            post_elasticsearch(self.useragent, self.config.get('elasticsearch', 'es_url'), parts[0], time_parts[0], parts[0] + ' ' + time_parts[0], time_parts[1], parts[4], parts[5], parts[6], parts[7], parts[8], parts[9], parts[10], parts[11], parts[12])

                    # Telegram integration
                    if 'Yes' == self.config.get('telegram', 'enabled'):
                        from loggers.telegram.honeypy_telegram import send_telegram_message
                        if 'TCP' == parts[4]:
                            send_telegram_message(self.config, parts[8], parts[9])
                        else:
                            # UDP splits differently (see comment section above)
                            send_telegram_message(self.config, parts[9], parts[10])

                    # Elasticsearch integration
                    if 'Yes' == self.config.get('splunk', 'enabled'):
                        from loggers.splunk.honeypy_splunk import post_splunk

                        url 		= self.config.get('splunk', 'url')
                        username 	= self.config.get('splunk', 'username')
                        password 	= self.config.get('splunk', 'password')

                        if 'TCP' == parts[4]:
                            if 11 == len(parts):
                                parts.append('') # no data for CONNECT events

                            post_splunk(username, password, self.useragent, url, parts[0], time_parts[0], parts[0] + ' ' + time_parts[0], time_parts[1], parts[3], parts[4], parts[5], parts[6], parts[7], parts[8], parts[9], parts[10], parts[11])
                        else:
                            # UDP splits differently (see comment section above)
                            if 12 == len(parts):
                                parts.append('') # no data sent

                            post_splunk(username, password, self.useragent, url, parts[0], time_parts[0], parts[0] + ' ' + time_parts[0], time_parts[1], parts[4], parts[5], parts[6], parts[7], parts[8], parts[9], parts[10], parts[11], parts[12])

                    # Rabbitmq integration.
                    if 'Yes' == self.config.get('rabbitmq', 'enabled'):
                        from loggers.rabbitmq.honeypy_rabbitmq import post_rabbitmq

                        if 'TCP' == parts[4]:
                            if 11 == len(parts):
                                parts.append('')  # no data for CONNECT events

                            post_rabbitmq(self.config.get('rabbitmq', 'url_param'), self.config.get('rabbitmq', 'exchange'),
                                        self.config.get('rabbitmq', 'routing_key'),parts[0],
                                        time_parts[0], parts[0] + ' ' + time_parts[0], time_parts[1], parts[3], parts[4], parts[5],
                                        parts[6], parts[7], parts[8], parts[9], parts[10], parts[11])

                        else:
                            # UDP splits differently (see comment section above)
                            if 12 == len(parts):
                                parts.append('')  # no data sent

                            post_rabbitmq(self.config.get('rabbitmq', 'url_param'), self.config.get('rabbitmq', 'exchange'),
                                        self.config.get('rabbitmq', 'routing_key'),parts[0],
                                        time_parts[0], parts[0] + ' ' + time_parts[0], time_parts[1], parts[4], parts[5], parts[6],
                                        parts[7], parts[8], parts[9], parts[10], parts[11], parts[12])
                except Exception as e:
                    log.msg('Exception: HoneyPyLogTail: {}: {}'.format(str(e), str(parts)))
