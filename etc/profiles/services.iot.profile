# HoneyPy Copyright (C) 2013-2016 foospidy
# services.iot.profile
# Important: service names must not contain spaces.
# Important: use port redirecting for services that listen on ports below 1024 (see https://github.com/foospidy/ipt-kit).
# Internet of Things (IoT) related services

[Telnet]
plugin      = TelnetUnix
low_port    = tcp:23
port        = tcp:10023
description = Telnet port
enabled     = Yes

[Telnet.IoT]
plugin      = TelnetUnix
low_port    = tcp:2323
port        = tcp:2323
description = IoT telnet port, reference https://isc.sans.edu/diary/21563
enabled     = Yes

[HTTP.alt]
plugin      = Web
low_port    = tcp:8080
port        = tcp:8080
description = Alternative port for web services
enabled     = Yes

[Cactus]
plugin      = Web
low_port    = tcp:49115
port        = tcp:49115
description = IoT port, reference http://cactus.io/tutorials/web/connect-iot-device-to-the-internet
enabled     = Yes
