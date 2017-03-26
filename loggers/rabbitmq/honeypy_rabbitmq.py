# HoneyPy Copyright (C) 2013-2017 foospidy
# https://github.com/foospidy/HoneyPy
# See LICENSE for details
# HoneyPy logstash logger

import sys
import hashlib
import socket
import json
from twisted.python import log

#pika==0.10.0
import pika

# prevent creation of compiled bytecode files
sys.dont_write_bytecode = True


def post_rabbitmq(url_param, exchange, routing_key, date, time, date_time, millisecond, session,
                  protocol, event, local_host, local_port, service, remote_host, remote_port, data):

    h = hashlib.md5()
    h.update(data)

    # applying [:-3] to time to truncate millisecond
    data1 = {
        'date': date,
        'time': time,
        'date_time': date_time,
        'millisecond': str(millisecond)[:-3],
        'session': session,
        'protocol': protocol,
        'event': event,
        'local_host': local_host,
        'local_port': local_port,
        'service': service,
        'remote_host': remote_host,
        'remote_port': remote_port,
        'data': data,
        'bytes': str(len(data)),
        'data_hash': h.hexdigest()
    }

    logtosend = json.dumps(data1)

    try:

        connection = pika.BlockingConnection(pika.URLParameters(url_param))
        channel = connection.channel()
        channel.basic_publish(exchange=exchange,
                              routing_key=routing_key,
                              body=str(logtosend))

        connection.close()

        log.msg('Post event to rabbitmq! {%s} (%s bytes)' % (logtosend, len(logtosend)))

    except socket.error, msg:
        log.msg('[ERROR] post_rabbitmq, socket.error: %s' % msg[1])

    except Exception as e:
        log.msg('Error posting to rabbitmq: %s' % (str(e.message).strip()))
