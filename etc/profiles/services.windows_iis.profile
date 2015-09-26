# HoneyPy Copyright (C) 2013-2015 foospidy
# services.windows_iis.profile
# Important: service names must not contain spaces.
# Important: use port redirecting for services that listen on ports below 1024 (see https://github.com/foospidy/ipt-kit).

[SMTP]
plugin      = Echo
low_port    = tcp:25
port        = tcp:30025
description = Echo back data received via tcp.
enabled     = Yes

[FTP]
plugin      = Echo
low_port    = tcp:21
port        = tcp:30021
description = Echo back data received via tcp.
enabled     = Yes

[Telnet]
plugin      = TelnetWindows
low_port    = tcp:23
port        = tcp:30023
description = Emulate Windows telnet via tcp.
enabled     = Yes

[HTTP]
plugin      = Echo
low_port    = tcp:80
port        = tcp:30080
description = Echo back data received via tcp.
enabled     = Yes

[HTTPS]
plugin      = Random
low_port    = tcp:443
port        = tcp:30443
description = Send random data received via tcp.
enabled     = Yes

[CIFS]
plugin      = Echo
low_port    = tcp:445
port        = tcp:30445
description = Echo back data received via tcp.
enabled     = Yes

[CIFS.udp]
plugin      = Echo_udp
low_port    = udp:445
port        = udp:30445
description = Echo back data received via udp.
enabled     = Yes
