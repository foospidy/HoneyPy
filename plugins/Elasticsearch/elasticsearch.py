# HoneyPy Copyright (C) 2013-2017 foospidy
# https://github.com/foospidy/HoneyPy
# See LICENSE for details

from twisted.internet import protocol, reactor, endpoints
from twisted.python import log
import uuid


### START CUSTOM IMPORTS ###

############################

class Elasticsearch(protocol.Protocol):  ### Set custom protocol class name
    localhost = None
    remote_host = None
    session = None

    ### START CUSTOM VARIABLES ###############################################################

    ##########################################################################################

    # handle events
    def connectionMade(self):
        self.connect()

    ### START CUSTOM CODE ####################################################################

    ##########################################################################################

    def dataReceived(self, data):
        self.rx(data)

        ### START CUSTOM CODE ####################################################################

        # response = 'HTTP/1.1 200 OK\nServer: Apache/2.4.10 (Debian)\nConnection: close\nContent-Type: text/html\n\nOK!'
        if data.startswith("GET / HTTP"):
            response = """{ "status" : 200, "name" : "Flake", "cluster_name" : "elasticsearch", "version" : {"number" : "1.4.1","\
                        "build_hash" : "61ccbdf1fab017166ec4b96a88e82e8ab88f43fc",\
                        "build_timestamp" : "2016-04-11T03:14:12Z",\
                        "build_snapshot" : false, "lucene_version" : "4.10.4"},\
                        "tagline" : "You Know, for Search"}"""
            self.tx(response)

        elif "/_nodes" in data:
            response = self.fakeNodes()
            self.tx(response)

        elif "/_search" in data:
            response = self.fakeSearch()
            self.tx(response)  # close connection anyways
        self.transport.loseConnection()

        ##########################################################################################

    ### START CUSTOM FUNCTIONS ###################################################################
    def fakeSearch(self):
        res = """{
            "took" : 6,
            "timed_out" : false,
            "_shards" : {
                "total" : 6,
                "successful" : 6,
                "failed" : 0
            },
            "hits" : {
                "total" : 1,
                "max_score" : 1.0,
                "hits" : [ {
                    "_index" : ".kibana",
                    "_type" : "index-pattern",
                    "_id" : "logstash-*",
                    "_score" : 1.0,
                    "_source":{"title":"logstash-*","timeFieldName":"@timestamp","customFormats":"{}","fields":"[{\"type\":\"string\",\"indexed\":true,\"analyzed\":true,\"doc_values\":false,\"name\":\"host\",\"count\":0},{\"type\":\"string\",\"indexed\":false,\"analyzed\":false,\"name\":\"_source\",\"count\":0},{\"type\":\"string\",\"indexed\":true,\"analyzed\":false,\"doc_values\":false,\"name\":\"message.raw\",\"count\":0},{\"type\":\"string\",\"indexed\":false,\"analyzed\":false,\"name\":\"_index\",\"count\":0},{\"type\":\"string\",\"indexed\":true,\"analyzed\":false,\"doc_values\":false,\"name\":\"@version\",\"count\":0},{\"type\":\"string\",\"indexed\":true,\"analyzed\":true,\"doc_values\":false,\"name\":\"message\",\"count\":0},{\"type\":\"date\",\"indexed\":true,\"analyzed\":false,\"doc_values\":false,\"name\":\"@timestamp\",\"count\":0},{\"type\":\"string\",\"indexed\":true,\"analyzed\":false,\"name\":\"_type\",\"count\":0},{\"type\":\"string\",\"indexed\":true,\"analyzed\":false,\"name\":\"_id\",\"count\":0},{\"type\":\"string\",\"indexed\":true,\"analyzed\":false,\"doc_values\":false,\"name\":\"host.raw\",\"count\":0},{\"type\":\"geo_point\",\"indexed\":true,\"analyzed\":false,\"doc_values\":false,\"name\":\"geoip.location\",\"count\":0}]"}
                }]
              }
            }"""
        return res


    def fakeNodes(self):
        res = """{
            "cluster_name" : "elasticsearch",
            "nodes" : {
                "x1JG6g9PRHy6ClCOO2-C4g" : {
                  "name" : "%s",
                  "transport_address" : "inet[/
                %s:9300]",
                  "host" : "elk",
                  "ip" : "127.0.1.1",
                  "version" : "%s",
                  "build" : "89d3241",
                  "http_address" : "inet[/%s:9200]",
                  "os" : {
                    "refresh_interval_in_millis" : 1000,
                    "available_processors" : 12,
                    "cpu" : {
                      "total_cores" : 24,
                      "total_sockets" : 48,
                      "cores_per_socket" : 2
                    }
                  },
                  "process" : {
                    "refresh_interval_in_millis" : 1000,
                    "id" : 2039,
                    "max_file_descriptors" : 65535,
                    "mlockall" : false
                  },
                  "jvm" : {
                    "version" : "1.7.0_65"
                  },
                  "network" : {
                    "refresh_interval_in_millis" : 5000,
                    "primary_interface" : {
                      "address" : "%s",
                      "name" : "eth0",
                      "mac_address" : "08:01:c7:3F:15:DD"
                    }
                  },
                  "transport" : {
                    "bound_address" : "inet[/0:0:0:0:0:0:0:0:9300]",
                    "publish_address" : "inet[/%s:9300]"
                  },
                  "http" : {
                    "bound_address" : "inet[/0:0:0:0:0:0:0:0:9200]",
                    "publish_address" : "inet[/%s:9200]",
                    "max_content_length_in_bytes" : 104857600
                  }}
                }
            }"""
        return res

    ##############################################################################################

    def connect(self):
        self.local_host = self.transport.getHost()
        self.remote_host = self.transport.getPeer()
        self.session = uuid.uuid1()
        log.msg('%s %s CONNECT %s %s %s %s %s' % (
        self.session, self.remote_host.type, self.local_host.host, self.local_host.port, self.factory.name,
        self.remote_host.host, self.remote_host.port))

    def clientConnectionLost(self):
		self.transport.loseConnection()
        
    def tx(self, data):
        # log.msg('%s %s TX %s %s %s %s %s %s' % (self.session, self.remote_host.type, self.local_host.host, self.local_host.port, self.factory.name, self.remote_host.host, self.remote_host.port, data.encode("hex")))
        log.msg('%s %s TX %s %s %s %s %s %s' % (
            self.session, self.remote_host.type, self.local_host.host, self.local_host.port, self.factory.name,
            self.remote_host.host, self.remote_host.port, data.encode('hex')))
        self.transport.write(data)

    def rx(self, data):
        log.msg('%s %s RX %s %s %s %s %s %s' % (
        self.session, self.remote_host.type, self.local_host.host, self.local_host.port, self.factory.name,
        self.remote_host.host, self.remote_host.port, data.encode('hex')))


class pluginFactory(protocol.Factory):
    protocol = Elasticsearch  ### Set protocol to custom protocol class name

    def __init__(self, name=None):
        self.name = name or 'HoneyPy'
