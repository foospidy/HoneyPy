# HoneyPy Copyright (C) 2013-2016 foospidy
# services.kali.profile
# Important: service names must not contain spaces.
# Important: use port redirecting for services that listen on ports below 1024 (see https://github.com/foospidy/ipt-kit).
# Attempt at a Kali Linux profile

[Bootp]
plugin      = Echo_udp
low_port    = udp:68
port        = udp:10068
description = bootp client
enabled     = Yes

[Beef.XSS]
plugin      = Echo
low_port    = tcp:2000
port        = tcp:2000
description = Beef related port
enabled     = Yes

[Beef.XSS]
plugin      = Echo
low_port    = tcp:3000
port        = tcp:3000
description = beef related port
enabled     = Yes

[Armitage]
plugin      = Echo
low_port    = tcp:55553
port        = tcp:55553
description = Armitage team server
enabled     = Yes
