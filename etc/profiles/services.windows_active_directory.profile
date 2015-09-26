# HoneyPy Copyright (C) 2013-2015 foospidy
# services.windows_active_directory.example
# Important: service names must not contain spaces.
# Important: use port redirecting for services that listen on ports below 1024 (see https://github.com/foospidy/ipt-kit).
# References: http://technet.microsoft.com/en-us/library/dd772723(v=ws.10).aspx

[LDAP]
plugin      = Echo
low_port    = tcp:389
port        = tcp:30389
description = Echo back data received via tcp.
enabled     = Yes

[LDAP.udp]
plugin      = Echo_udp
low_port    = udp:389
port        = udp:30389
description = Echo back data received via udp.
enabled     = Yes

[SLDAP]
plugin      = Echo
low_port    = tcp:636
port        = tcp:30636
description = Echo back data received via tcp.
enabled     = Yes

[LDAP.GC]
plugin      = Echo
low_port    = tcp:3268
port        = tcp:3268
description = Echo back data received via tcp.
enabled     = Yes

[SLDAP.GC]
plugin      = Echo
low_port    = tcp:3269
port        = tcp:3269
description = Echo back data received via tcp.
enabled     = Yes

[Kerberos]
plugin      = Echo
low_port    = tcp:88
port        = tcp:30088
description = Echo back data received via tcp.
enabled     = Yes 

[Kerberos.udp]
plugin      = Echo_udp
low_port    = udp:88
port        = udp:30088
description = Echo back data received via udp.
enabled     = Yes 

[DNS]
plugin      = Echo
low_port    = tcp:53
port        = tcp:30053
description = Echo back data received via tcp.
enabled     = Yes

[DNS.udp]
plugin      = Echo_udp
low_port    = udp:53
port        = udp:30053
description = Echo back data received via udp.
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

[SMTP]
plugin      = Echo
low_port    = tcp:25
port        = tcp:30025
description = Echo back data received via tcp.
enabled     = Yes

[RPC]
plugin      = Echo
low_port    = tcp:135
port        = tcp:30135
description = Echo back data received via tcp.
enabled     = Yes

[NTP]
plugin      = Echo_udp
low_port    = udp:123
port        = udp:30123
description = Echo back data received via udp.
enabled     = Yes

[KerberosChangePassword]
plugin      = Echo
low_port    = tcp:464
port        = tcp:30464
description = Echo back data received via tcp.
enabled     = Yes

[KerberosChangePassword_udp]
plugin      = Echo_udp
low_port    = udp:464
port        = udp:30464
description = Echo back data received via udp.
enabled     = Yes

[DFS]
plugin      = Echo_udp
low_port    = udp:138
port        = udp:30138
description = Echo back data received via udp.
enabled     = Yes

[AD.DS_WS]
plugin      = Echo
low_port    = tcp:9389
port        = tcp:9389
description = Echo back data received via tcp.
enabled     = Yes

[DHCP]
plugin      = Echo_udp
low_port    = udp:67
port        = udp:30067
description = Echo back data received via udp.
enabled     = Yes

[NetLogon]
plugin      = Echo_udp
low_port    = udp:137
port        = udp:30137
description = Echo back data received via udp.
enabled     = Yes

[DFSN]
plugin      = Echo
low_port    = tcp:139
port        = tcp:30139
description = Echo back data received via tcp.
enabled     = Yes
