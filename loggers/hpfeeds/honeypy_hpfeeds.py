# HoneyPy hpfeeds module

import sys
import hashlib
from datetime import datetime
from twisted.python import log
import json
import os
import socket


class hpflogger:
    def __init__(self, hpfserver, hpfport, hpfident, hpfsecret, hpfchannel, serverid):
        self.hpfserver = hpfserver
        self.hpfport = hpfport
        self.hpfident = hpfident
        self.hpfsecret = hpfsecret
        self.hpfchannel = hpfchannel
        self.serverid = serverid
        self.hpc = None
        if (self.hpfserver and self.hpfport and self.hpfident and self.hpfport and self.hpfchannel and self.serverid):
            import logging
            logging.basicConfig()
            import hpfeeds
            try:
                self.hpc = hpfeeds.new(self.hpfserver, self.hpfport, self.hpfident, self.hpfsecret)
                self.status = "Logging to hpfeeds using server: {0}, channel {1}.".format(self.hpfserver, self.hpfchannel)
            except (hpfeeds.FeedException, socket.error, hpfeeds.Disconnect):
                self.status = "hpfeeds connection not successful"
    def log(self, message):
        if self.hpc:
            message['serverid'] = self.serverid
            self.hpc.publish(self.hpfchannel, json.dumps(message))

def conn(config, section):
    environreq = [
        'HPFEEDS_SERVER',
        'HPFEEDS_PORT',
        'HPFEEDS_IDENT',
        'HPFEEDS_SECRET',
        'HPFEEDS_CHANNEL',
        'SERVERID',
        ]
    if all(var in os.environ for var in environreq):
        hpfserver = os.environ.get('HPFEEDS_SERVER')
        hpfport = int(os.environ.get('HPFEEDS_PORT'))
        hpfident = os.environ.get('HPFEEDS_IDENT')
        hpfsecret = os.environ.get('HPFEEDS_SECRET')
        hpfchannel = os.environ.get('HPFEEDS_CHANNEL')
        serverid = os.environ.get('SERVERID')
    else:
        hpfserver = config.get(section, 'server')
        hpfport = int(config.get(section, 'port'))
        hpfident = config.get(section, 'ident')
        hpfsecret = config.get(section, 'secret')
        hpfchannel = config.get(section, 'channel')
        serverid = config.get(section, 'server')

    return hpflogger(hpfserver, hpfport, hpfident, hpfsecret, hpfchannel, serverid)

def process(config, connection, section, parts, time_parts):
        # TCP
        #    parts[0]: date
        #    parts[1]: time_parts
        #    parts[2]: plugin
        #    parts[3]: session
        #    parts[4]: protocol
        #    parts[5]: event
        #    parts[6]: local_host
        #    parts[7]: local_port
        #    parts[8]: service
        #    parts[9]: remote_host
        #    parts[10]: remote_port
        #    parts[11]: data
        # UDP
        #    parts[0]: date
        #    parts[1]: time_parts
        #    parts[2]: plugin string part
        #    parts[3]: plugin string part
        #    parts[4]: session
        #    parts[5]: protocol
        #    parts[6]: event
        #    parts[7]: local_host
        #    parts[8]: local_port
        #    parts[9]: service
        #    parts[10]: remote_host
        #    parts[11]: remote_port
        #    parts[12]: data

    if parts[4] == 'TCP':
        if len(parts) == 11:
            parts.append('')  # no data for CONNECT events
        post(config, section, parts[0], time_parts[0], time_parts[1], parts[3], parts[4], parts[5], parts[6], parts[7], parts[8], parts[9], parts[10], parts[11], connection)
    else:
        # UDP splits differently (see comment section above)
        if len(parts) == 12:
            parts.append('')  # no data sent
        post(config, section, parts[0], time_parts[0], time_parts[1], parts[4], parts[5], parts[6], parts[7], parts[8], parts[9], parts[10], parts[11], parts[12], connection)


def post(config, section, date, time, millisecond, session, protocol, event, local_host, local_port, service, remote_host, remote_port, data, connection):

    date_time = date + ' ' + time + '.' + str(millisecond)
    date_time = datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S.%f").isoformat() + 'Z'

    msg = {
        'date_time': date_time,
        'protocol': protocol,
        'service': service,
        'dst_host': local_host,
        'dst_port': local_port,
        'src_host': remote_host,
        'src_port': remote_port,
        'session': session,
        'event': event,
        'data': data,
    }

    # submit log
    connection.log(msg)