# Configuring HoneyPy

There are two configuration files for HoneyPy, both are located in the HoneyPy `etc` directory (e.g. `/opt/HoneyPy/etc`). The main configuration file is `honeypy.cfg`, and the services configuration file is `services.cfg`.

## HoneyPy

In the `honeypy.cfg` file, the main configuration section is the `[honeypy]` section and actually only has one option to configure.

Name | Description
---------- | -------
nodename | Name for this HoneyPy node to be displayed in tweets, Slack messages, and other integrations.

### Loggers

The remaining sections in the `honeypy.cfg` configuration file are for configuring loggers.

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

#### Twitter

Name | Description
---------- | -------
enabled | Enable this logger (e.g. Yes or No).
bot_id | Telegram bot HTTP API token.

## Services

Name | Description
---------- | -------
enabled | Enable this logger (e.g. Yes or No).
