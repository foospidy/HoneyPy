# Configuring HoneyPy

There are two configuration files for HoneyPy, both are located in the HoneyPy `etc` directory (e.g. `/opt/HoneyPy/etc`). The main configuration file is `honeypy.cfg`, and the services configuration file is `services.cfg`.

## HoneyPy

In the `honeypy.cfg` file, the main configuration section is the `[honeypy]` section and actually only has one option to configure.

Name | Description
---------- | -------
nodename | Name for this HoneyPy node to be displayed in tweets, Slack messages, and other integrations.

### Loggers

The remaining sections in the `honeypy.cfg` configuration file are for configuring loggers. Loggers are modules that make consuming or processing event data more convenient by sending the event data to another service. These other services and their configuration options are listed below.

__NOTE:__ More than one logger can be configured at a time. For example, if the Elasticsearch, HoneyDB, and RabbitMQ loggers are configured then all events will be sent to all three services.

__NOTE:__ By default, HoneyPy logs all events to the log file `/opt/HoneyPy/log/honeypy.log`. All events are logged to this file regardless of a logger being configured or not.

#### Elasticsearch

Name | Description
---------- | -------
enabled | Enable this logger (e.g. Yes or No).
es_url | URL to Elasticsearch endpoint (e.g.  http://localhost:9200/honeypot/honeypy).

#### HoneyDB

Name | Description
---------- | -------
enabled | Enable this logger (e.g. Yes or No).
api_id | Your HoneyDB API id.
api_key | Your HoneyDB API key.

#### Logstash

Name | Description
---------- | -------
enabled | Enable this logger (e.g. Yes or No).
host | Logstash host.
port | Logstash port.

#### RabbitMQ

Name | Description
---------- | -------
enabled | Enable this logger (e.g. Yes or No). 
url_param | RabbitMQ config url (e.g. amqp://username:password@rabbitmq_host/%2f).
exchange | Name of the Rabbitmq Exchange
routing_key | Rabbitmq routing Key (if not configured in RabbitmQ, leave blank)

#### Slack

Name | Description
---------- | -------
enabled | Enable this logger (e.g. Yes or No).
webhook_url | Slack channel webhook URL.

#### Splunk

Name | Description
---------- | -------
enabled | Enable this logger (e.g. Yes or No).
url | Splunk API endpoint (e.g. https://localhost:8089/services/receivers/simple).
username | Username for authentication. 
password | Password for authentication.

#### Telegram

Name | Description
---------- | -------
enabled | Enable this logger (e.g. Yes or No).
bot_id | Telegram bot HTTP API token.

#### Twitter

Name | Description
---------- | -------
enabled | Enable this logger (e.g. Yes or No).
consumerkey | Your Twitter consumer key.
consumersecret | Your Twitter consumer secret.
oauthtoken | Your Twitter OAuth token.
oauthsecret | Your Twitter OAuth secret.

## Services

The `service.cfg` file tells HoneyPy which services to launch. There are several additional service configuration files located in the `etc/profiles` directory. The service config file is used to define service names, ports, and plugins to run on your honeypot. Each service defined in the file has an `enabled` option. This option can be set to Yes or No to determine which services run on start. You can also use one of the provided config files, or create your own. To use one of the other files simply copy the file over service.cfg. For example:

`cp profiles/services.windows_iis.profile service.cfg`

If you want to revert back to the default service config file simply run

`cp profiles/service.default.profile service.cfg`
