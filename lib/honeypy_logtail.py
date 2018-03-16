from importlib import import_module
from ConfigParser import NoSectionError
from twisted.python import log
from lib.followtail import FollowTail

class HoneyPyLogTail(FollowTail):
    config = None
    useragent = None

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
            if parts[2] != '[-]' and parts[0] != 'details':
                # time_parts[0]: time
                # time_parts[1]: millisecond
                # time_parts[2]: time zone
                time_parts = parts[1].split(',')

                # iterate through the configured sections
                for section in self.config.sections():
                    #this is a transitional condition
                    if section in ["logstash", "honeydb", "slack", "twitter", "sumologic"] and self.config.get(section, 'enabled'):
                        self.config.items(section)
                        module_name = "loggers.%s.honeypy_%s" % (section, section)
                        logger_module = import_module(module_name)
                        logger_module.process(self.config, section, parts, time_parts, self.useragent)

                try:

                    try:
                        # Elasticsearch integration
                        if self.config.get('elasticsearch', 'enabled') == 'Yes':
                            from loggers.elasticsearch.honeypy_elasticsearch import post_elasticsearch

                            if parts[4] == 'TCP':
                                if len(parts) == 11:
                                    parts.append('')  # no data for CONNECT events

                                post_elasticsearch(self.useragent, self.config.get('elasticsearch', 'es_url'), parts[0], time_parts[0], parts[0] + ' ' + time_parts[0], time_parts[1], parts[3], parts[4], parts[5], parts[6], parts[7], parts[8], parts[9], parts[10], parts[11])
                            else:
                                # UDP splits differently (see comment section above)
                                if len(parts) == 12:
                                    parts.append('')  # no data sent

                                post_elasticsearch(self.useragent, self.config.get('elasticsearch', 'es_url'), parts[0], time_parts[0], parts[0] + ' ' + time_parts[0], time_parts[1], parts[4], parts[5], parts[6], parts[7], parts[8], parts[9], parts[10], parts[11], parts[12])
                    except NoSectionError:
                        pass

                    try:
                        # Telegram integration
                        if self.config.get('telegram', 'enabled') == 'Yes':
                            from loggers.telegram.honeypy_telegram import send_telegram_message
                            if parts[4] == 'TCP':
                                send_telegram_message(self.config, parts[8], parts[9])
                            else:
                                # UDP splits differently (see comment section above)
                                send_telegram_message(self.config, parts[9], parts[10])
                    except NoSectionError:
                        pass

                    try:
                        # Splunk
                        if self.config.get('splunk', 'enabled') == 'Yes':
                            from loggers.splunk.honeypy_splunk import post_splunk

                            url = self.config.get('splunk', 'url')
                            username = self.config.get('splunk', 'username')
                            password = self.config.get('splunk', 'password')

                            if parts[4] == 'TCP':
                                if len(parts) == 11:
                                    parts.append('')  # no data for CONNECT events

                                post_splunk(username, password, self.useragent, url, parts[0], time_parts[0], parts[0] + ' ' + time_parts[0], time_parts[1], parts[3], parts[4], parts[5], parts[6], parts[7], parts[8], parts[9], parts[10], parts[11])
                            else:
                                # UDP splits differently (see comment section above)
                                if len(parts) == 12:
                                    parts.append('')  # no data sent

                                post_splunk(username, password, self.useragent, url, parts[0], time_parts[0], parts[0] + ' ' + time_parts[0], time_parts[1], parts[4], parts[5], parts[6], parts[7], parts[8], parts[9], parts[10], parts[11], parts[12])
                    except NoSectionError:
                        pass

                    try:
                        # Rabbitmq integration.
                        if self.config.get('rabbitmq', 'enabled') == 'Yes':
                            from loggers.rabbitmq.honeypy_rabbitmq import post_rabbitmq

                            if parts[4] == 'TCP':
                                if len(parts) == 11:
                                    parts.append('')  # no data for CONNECT events

                                post_rabbitmq(self.config.get('rabbitmq', 'url_param'), self.config.get('rabbitmq', 'exchange'),
                                              self.config.get('rabbitmq', 'routing_key'), parts[0],
                                              time_parts[0], parts[0] + ' ' + time_parts[0], time_parts[1], parts[3], parts[4], parts[5],
                                              parts[6], parts[7], parts[8], parts[9], parts[10], parts[11])

                            else:
                                # UDP splits differently (see comment section above)
                                if len(parts) == 12:
                                    parts.append('')  # no data sent

                                post_rabbitmq(self.config.get('rabbitmq', 'url_param'), self.config.get('rabbitmq', 'exchange'),
                                              self.config.get('rabbitmq', 'routing_key'), parts[0],
                                              time_parts[0], parts[0] + ' ' + time_parts[0], time_parts[1], parts[4], parts[5], parts[6],
                                              parts[7], parts[8], parts[9], parts[10], parts[11], parts[12])
                    except NoSectionError:
                        pass

                except Exception as e:
                    log.msg('Exception: HoneyPyLogTail: {}: {}'.format(str(e), str(parts)))
