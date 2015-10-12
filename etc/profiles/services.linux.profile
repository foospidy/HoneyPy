# HoneyPy Copyright (C) 2013-2015 foospidy
# services.linux.profile
# Important: service names must not contain spaces.
# Important: use port redirecting for services that listen on ports below 1024 (see https://github.com/foospidy/ipt-kit).
# Reference: https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers

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

[FTP]
plugin      = Echo
low_port    = tcp:21
port        = tcp:10021
description = Echo back data received via tcp.
enabled     = Yes

[SSH]
plugin      = Random
low_port    = tcp:22
port        = tcp:10022
description = Send random data via tcp.
enabled     = Yes

[Telnet]
plugin      = TelnetDebian7
low_port    = tcp:23
port        = tcp:10023
description = Emulate Debian telnet login via tcp.
enabled     = Yes

[SMTP]
plugin      = SmtpExim
low_port    = tcp:25
port        = tcp:10025
description = Echo back data received via tcp.
enabled     = Yes

[DNS]
plugin      = Echo
low_port    = tcp:53
port        = tcp:10053
description = Echo back data received via tcp.
enabled     = Yes

[DNS.udp]
plugin      = DnsUdp
low_port    = udp:53
port        = udp:10053
description = Echo back data received via udp.
enabled     = Yes

[Bootp]
plugin      = Echo_udp
low_port    = udp:67
port        = udp:10067
description = Echo back data received via tcp.
enabled     = Yes

[TFTP]
plugin      = Echo_udp
low_port    = udp:69
port        = udp:10069
description = Echo back data received via udp.
enabled     = Yes

[HTTP]
plugin      = Echo
low_port    = tcp:80
port        = tcp:10080
description = Echo back data received via tcp.
enabled     = Yes

[Kerberos]
plugin      = Echo
low_port    = tcp:88
port        = tcp:10088
description = Echo back data received via tcp.
enabled     = Yes 

[Kerberos.udp]
plugin      = Echo_udp
low_port    = udp:88
port        = udp:10088
description = Echo back data received via udp.
enabled     = Yes 

[POP3]
plugin      = Echo
low_port    = tcp:110
port        = tcp:10110
description = Echo back data received via tcp.
enabled     = Yes 

[SunRPC]
plugin      = Echo
low_port    = tcp:111
port        = tcp:10111
description = Echo back data received via tcp.
enabled     = Yes

[SunRPC.udp]
plugin      = Echo_udp
low_port    = udp:111
port        = udp:10111
description = Echo back data received via udp.
enabled     = Yes

[NTP]
plugin      = Echo_udp
low_port    = udp:123
port        = udp:10123
description = Echo back data received via udp.
enabled     = Yes

[NetBIOS]
plugin      = Echo_udp
low_port    = udp:137
port        = udp:10137
description = Echo back data received via udp.
enabled     = Yes

[Samba]
plugin      = Echo
low_port    = tcp:139
port        = tcp:10139
description = Echo back data received via tcp.
enabled     = Yes

[IMAP]
plugin      = Echo
low_port    = tcp:143
port        = tcp:10143
description = Echo back data received via tcp.
enabled     = Yes

[SNMP]
plugin      = Echo_udp
low_port    = udp:161
port        = udp:10161
description = Echo back data received via udp.
enabled     = Yes

[LDAP]
plugin      = Echo
low_port    = tcp:389
port        = tcp:10389
description = Echo back data received via tcp.
enabled     = Yes

[LDAP.udp]
plugin      = Echo_udp
low_port    = udp:389
port        = udp:10389
description = Echo back data received via udp.
enabled     = Yes

[HTTPS]
plugin      = Random
low_port    = tcp:443
port        = tcp:10443
description = Send random data via tcp.
enabled     = Yes

[Syslog]
plugin      = Echo_udp
low_port    = udp:514
port        = udp:10514
description = Echo back data received via udp.
enabled     = Yes

[SLDAP]
plugin      = Echo
low_port    = tcp:636
port        = tcp:10636
description = Echo back data received via tcp.
enabled     = Yes

[SLDAP.udp]
plugin      = Echo_udp
low_port    = udp:636
port        = udp:10636
description = Echo back data received via udp.
enabled     = Yes

[Rsync]
plugin      = Echo
low_port    = tcp:873
port        = tcp:10873
description = Echo back data received via tcp.
enabled     = Yes

[MySQL]
plugin      = Random
low_port    = tcp:3306
port        = tcp:3306
description = Send random data via tcp.
enabled     = Yes

[NFS]
plugin      = Echo
low_port    = tcp:2049
port        = tcp:2049
description = Echo back data received via tcp.
enabled     = Yes

[NFS.udp]
plugin      = Echo_udp
low_port    = udp:2049
port        = udp:2049
description = Echo back data received via udp.
enabled     = Yes

[X11]
plugin      = Echo
low_port    = tcp:6000
port        = tcp:6000
description = Echo back data received via tcp.
enabled     = Yes
