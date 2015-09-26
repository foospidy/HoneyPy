# HoneyPy Copyright (C) 2013-2015 foospidy
# services.default.profile
# Important: service names must not contain spaces.
# Important: use port redirecting for services that listen on ports below 1024 (see https://github.com/foospidy/ipt-kit).

[Echo]
plugin      = Echo
low_port    = tcp:7
port        = tcp:10007
description = Echo back data received via tcp.
enabled     = Yes

[Echo.udp]
plugin      = Echo_udp
low_port    = udp:7
port        = udp:10007
description = Echo back data received via udp.
enabled     = Yes

[MOTD]
plugin      = MOTD
low_port    = tcp:8
port        = tcp:10008
description = Send a message via tcp and close connection.
enabled     = Yes

[MOTD.udp]
plugin      = MOTD_udp
low_port    = udp:8
port        = udp:10008
description = Send a message via udp.
enabled     = Yes

[Telnet]
plugin      = TelnetDebian7
low_port    = tcp:23
port        = tcp:10009
description = Emulate Debian telnet login vai tcp.
enabled     = Yes

[WindowsTelnet]
plugin      = TelnetWindows
low_port    = tcp:24
port        = tcp:10010
description = Emulate Windows telnet login via tcp.
enabled     = Yes

[Random]
plugin      = Random
low_port    = tcp:2048
port        = tcp:2048
description = Send random data via tcp.
enabled     = Yes

[HashCountRandom]
plugin      = HashCountRandom
low_port    = tcp:4096
port        = tcp:4096
description = Send random data prefixed with a hash of a counter via tcp.
enabled     = Yes
