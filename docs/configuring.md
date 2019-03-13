# Configuring HoneyPy

There are two configuration files for HoneyPy, both are located in the HoneyPy `etc` directory (e.g. `/opt/HoneyPy/etc`). The main configuration file is `honeypy.cfg`, and the services configuration file is `services.cfg`.

## HoneyPy

In the `honeypy.cfg` file, the main configuration section is the `[honeypy]` section and only has two options to configure.

Name | Description
---------- | -------
nodename | Name for this HoneyPy node to be displayed in tweets, Slack messages, and other integrations.
limit_internal_logs | Enabling this will ensure that the internal log files are limited to one day, which can be useful for limited deployments e.g. automated containers (e.g. Yes or No).
internal_log_dir | Directory for internal HoneyPy logs (not external loggers). Use leading slash for absolute path, or omit for relative path. Default: `log/`

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

#### hpfeeds

Name | Description
---------- | -------
enabled | Enable this logger (e.g. Yes or No).
persistent | Is a persistent connection required (e.g. Yes).
server | hpfeeds server
port | hpfeeds port
ident | hpfeeds ident
secret | hpfeeds secret
channel | hpfeeds channel
serverid | hpfeeds server ID

## Services

The `service.cfg` file tells HoneyPy which services to launch. There are several additional service configuration files located in the `etc/profiles` directory. The service config file is used to define service names, ports, and plugins to run on your honeypot. Each service defined in the file has an `enabled` option. This option can be set to Yes or No to determine which services run on start. You can also use one of the provided config files, or create your own. To use one of the other files simply copy the file over service.cfg. For example:

```bash
cp profiles/services.windows_iis.profile service.cfg
```

If you want to revert back to the default service config file simply run

```bash
cp profiles/service.default.profile service.cfg
```

## Low Ports

While you should not run HoneyPy with the root user, this means HoneyPy will not be able to listen on ports 1 through 1024. As a workaround you can use implement port redirection with IPTables. If you're not familiar with using IPTables you can try using [ipt-kit](https://github.com/foospidy/ipt-kit). You will need to run ipt-kit as root to modify IPTables. Once the redirection rules are in place you won't need to run HoneyPy as root for low ports.

As an example, if you want HoneyPy to listen for telnet connections on port 23, choose a port above 1024. Edit the HoneyPy service config file to have telnet run on the high port (e.g. 2300). Then use ipt-kit to redirect 23 to 2300, example commands:

if root user:

```bash
./ipt_set_tcp 23 2300
```

or if using sudo:

```bash
$sudo ./ipt_set_tcp 23 2300
```

If you have low ports configured, when you run HoneyPy it will display a list of ipt-kit commands to run. For example:

```
./ipt_set_tcp 7 10007
./ipt_set_udp 7 10007
./ipt_set_tcp 8 10008
./ipt_set_udp 8 10008
./ipt_set_tcp 21 10021
./ipt_set_tcp 23 10009
./ipt_set_tcp 24 10010
```

__NOTE:__ The commands above can be generated as a script using HoneyPy. First edit your `service.cfg`, then run `./Honey.py -ipt`. The script will be saved to `/tmp/honeypy-ipt.sh`. Copy the script to the ipt-kit directory, and make sure the script file has execute permissions, e.g. `chmod +x honeypy-ipt.sh`. Run the script as root or with sudo.

Alternatively, you can use authbind to enabled the usage of low ports by HoneyPy's run user. More on authbind here: [https://debian-administration.org/article/386/Running_network_services_as_a_non-root_user](https://debian-administration.org/article/386/Running_network_services_as_a_non-root_user)
