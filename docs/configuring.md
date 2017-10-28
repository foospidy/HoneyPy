# Configuring HoneyPy

There are two configuration files for HoneyPy, both are located in the HoneyPy `etc` directory (e.g. `/opt/HoneyPy/etc`). The main configuration file is `honeypy.cfg`, and the services configuration file is `services.cfg`.

## HoneyPy

In the `honeypy.cfg` file, the main configuration section is the `[honeypy]` section and actually only has one option to configure.

Name | Description
---------- | -------
nodename | Name for this HoneyPy node to be displayed in tweets, Slack messages, and other integrations.

The remaining sections in the configuration file are for configuring loggers.

## Services
