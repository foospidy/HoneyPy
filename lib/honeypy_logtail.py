from importlib import import_module
from twisted.python import log
from lib.followtail import FollowTail

class HoneyPyLogTail(FollowTail):
    config = None

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

                #determin remote_host
                if parts[4] == 'TCP':
                    remote_host = parts[9]
                else:
                    remote_host = parts[10]

                #check if remote host is in whitelist
                if self.config.has_option('honeypy', 'whitelist') and remote_host in self.config.get('honeypy', 'whitelist').split(','):
                    log.msg("Remote host %s is whitelisted, external logging surpressed." % remote_host)
                else:
                    try:
                        # iterate through the configured sections, but not the main app section
                        for section in self.config.sections():
                            if section != 'honeypy' and self.config.get(section, 'enabled').lower() == 'yes':
                                module_name = "loggers.%s.honeypy_%s" % (section, section)
                                logger_module = import_module(module_name)
                                logger_module.process(self.config, section, parts, time_parts)

                    except Exception as e:
                        log.msg('Exception: HoneyPyLogTail: {}: {}'.format(str(e), str(parts)))
