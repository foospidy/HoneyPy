# HoneyPy Copyright (C) 2013-2016 foospidy
# services.peer_to_peer.profile
# Important: service names must not contain spaces.
# Important: use port redirecting for services that listen on ports below 1024 (see https://github.com/foospidy/ipt-kit).
# Peer to Peer related ports as noted by http://packetlife.net/media/library/23/common_ports.pdf

[Echo]
plugin      = Echo
low_port    = tcp:7
port        = tcp:10007
description = Echo on port 7
enabled     = Yes

[Chargen]
plugin      = Echo
low_port    = tcp:19
port        = tcp:10019
description = Chargen on port 19
enabled     = Yes

[FTP]
plugin      = Echo
low_port    = tcp:20
port        = tcp:10020
description = FTP on port 20
enabled     = Yes

[FTP]
plugin      = Echo
low_port    = tcp:21
port        = tcp:10021
description = FTP on port 21
enabled     = Yes

[SSH]
plugin      = Echo
low_port    = tcp:22
port        = tcp:10022
description = SSH/SCP on port 22
enabled     = Yes

[Telnet]
plugin      = Echo
low_port    = tcp:23
port        = tcp:10023
description = Telnet on port 23
enabled     = Yes

[SMTP]
plugin      = Echo
low_port    = tcp:25
port        = tcp:10025
description = SMTP on port 25
enabled     = Yes

[WINS.Replication]
plugin      = Echo
low_port    = tcp:42
port        = tcp:10042
description = Replication on port 42
enabled     = Yes

[WHOIS]
plugin      = Echo
low_port    = tcp:43
port        = tcp:10043
description = WHOIS on port 43
enabled     = Yes

[TACACS]
plugin      = Echo
low_port    = tcp:49
port        = tcp:10049
description = TACACS on port 49
enabled     = Yes

[DNS]
plugin      = Echo
low_port    = tcp:53
port        = tcp:10053
description = DNS on port 53
enabled     = Yes

[DHCP.BOOTP]
plugin      = Echo
low_port    = tcp:67
port        = tcp:10067
description = DHCP/BOOTP on port 67
enabled     = Yes

[DHCP.BOOTP]
plugin      = Echo
low_port    = tcp:68
port        = tcp:10068
description = DHCP/BOOTP on port 68
enabled     = Yes

[TFTP]
plugin      = Echo
low_port    = tcp:69
port        = tcp:10069
description = TFTP on port 69
enabled     = Yes

[Gopher]
plugin      = Echo
low_port    = tcp:70
port        = tcp:10070
description = Gopher on port 70
enabled     = Yes

[Finger]
plugin      = Echo
low_port    = tcp:79
port        = tcp:10079
description = Finger on port 79
enabled     = Yes

[HTTP]
plugin      = Echo
low_port    = tcp:80
port        = tcp:10080
description = HTTP on port 80
enabled     = Yes

[Kerberos]
plugin      = Echo
low_port    = tcp:88
port        = tcp:10088
description = Kerberos on port 88
enabled     = Yes

[MSExchange]
plugin      = Echo
low_port    = tcp:102
port        = tcp:10102
description = Exchange on port 102
enabled     = Yes

[POP3]
plugin      = Echo
low_port    = tcp:110
port        = tcp:10110
description = POP3 on port 110
enabled     = Yes

[Ident]
plugin      = Echo
low_port    = tcp:113
port        = tcp:10113
description = Ident on port 113
enabled     = Yes

[NNTP.Usenet]
plugin      = Echo
low_port    = tcp:119
port        = tcp:10119
description = (Usenet) on port 119
enabled     = Yes

[NTP]
plugin      = Echo
low_port    = tcp:123
port        = tcp:10123
description = NTP on port 123
enabled     = Yes

[Microsoft.RPC]
plugin      = Echo
low_port    = tcp:135
port        = tcp:10135
description = RPC on port 135
enabled     = Yes

[NetBIOS]
plugin      = Echo
low_port    = tcp:137
port        = tcp:10137
description = NetBIOS on port 137
enabled     = Yes

[NetBIOS]
plugin      = Echo
low_port    = tcp:138
port        = tcp:10138
description = NetBIOS on port 138
enabled     = Yes

[NetBIOS]
plugin      = Echo
low_port    = tcp:139
port        = tcp:10139
description = NetBIOS on port 139
enabled     = Yes

[IMAP4]
plugin      = Echo
low_port    = tcp:143
port        = tcp:10143
description = IMAP4 on port 143
enabled     = Yes

[SNMP]
plugin      = Echo
low_port    = tcp:161
port        = tcp:10161
description = SNMP on port 161
enabled     = Yes

[SNMP]
plugin      = Echo
low_port    = tcp:162
port        = tcp:10162
description = SNMP on port 162
enabled     = Yes

[XDMCP]
plugin      = Echo
low_port    = tcp:177
port        = tcp:10177
description = XDMCP on port 177
enabled     = Yes

[BGP]
plugin      = Echo
low_port    = tcp:179
port        = tcp:10179
description = BGP on port 179
enabled     = Yes

[AppleTalk]
plugin      = Echo
low_port    = tcp:201
port        = tcp:10201
description = AppleTalk on port 201
enabled     = Yes

[BGMP]
plugin      = Echo
low_port    = tcp:264
port        = tcp:10264
description = BGMP on port 264
enabled     = Yes

[TSP]
plugin      = Echo
low_port    = tcp:318
port        = tcp:10318
description = TSP on port 318
enabled     = Yes

[HP.Openview]
plugin      = Echo
low_port    = tcp:381
port        = tcp:10381
description = Openview on port 381
enabled     = Yes

[HP.Openview]
plugin      = Echo
low_port    = tcp:382
port        = tcp:10382
description = Openview on port 382
enabled     = Yes

[HP.Openview]
plugin      = Echo
low_port    = tcp:383
port        = tcp:10383
description = Openview on port 383
enabled     = Yes

[LDAP]
plugin      = Echo
low_port    = tcp:389
port        = tcp:10389
description = LDAP on port 389
enabled     = Yes

[Direct_Connect]
plugin      = Echo
low_port    = tcp:411
port        = tcp:10411
description = Connect on port 411
enabled     = Yes

[Direct_Connect]
plugin      = Echo
low_port    = tcp:412
port        = tcp:10412
description = Connect on port 412
enabled     = Yes

[HTTPS]
plugin      = Echo
low_port    = tcp:443
port        = tcp:10443
description = SSL on port 443
enabled     = Yes

[Microsoft.DS]
plugin      = Echo
low_port    = tcp:445
port        = tcp:10445
description = DS on port 445
enabled     = Yes

[Kerberos]
plugin      = Echo
low_port    = tcp:464
port        = tcp:10464
description = Kerberos on port 464
enabled     = Yes

[SMTPS]
plugin      = Echo
low_port    = tcp:465
port        = tcp:10465
description = SSL on port 465
enabled     = Yes

[Retrospect]
plugin      = Echo
low_port    = tcp:497
port        = tcp:10497
description = Retrospect on port 497
enabled     = Yes

[ISAKMP]
plugin      = Echo
low_port    = tcp:500
port        = tcp:10500
description = ISAKMP on port 500
enabled     = Yes

[rexec]
plugin      = Echo
low_port    = tcp:512
port        = tcp:10512
description = rexec on port 512
enabled     = Yes

[rlogin]
plugin      = Echo
low_port    = tcp:513
port        = tcp:10513
description = rlogin on port 513
enabled     = Yes

[syslog]
plugin      = Echo
low_port    = tcp:514
port        = tcp:10514
description = syslog on port 514
enabled     = Yes

[LPD_LPR]
plugin      = Echo
low_port    = tcp:515
port        = tcp:10515
description = LPD/LPR on port 515
enabled     = Yes

[RIP]
plugin      = Echo
low_port    = tcp:520
port        = tcp:10520
description = RIP on port 520
enabled     = Yes

[RIPng.IPv6]
plugin      = Echo
low_port    = tcp:521
port        = tcp:10521
description = (IPv6) on port 521
enabled     = Yes

[UUCP]
plugin      = Echo
low_port    = tcp:540
port        = tcp:10540
description = UUCP on port 540
enabled     = Yes

[RTSP]
plugin      = Echo
low_port    = tcp:554
port        = tcp:10554
description = RTSP on port 554
enabled     = Yes

[DHCPv6]
plugin      = Echo
low_port    = tcp:546
port        = tcp:10546
description = DHCPv6 on port 546
enabled     = Yes

[DHCPv6]
plugin      = Echo
low_port    = tcp:547
port        = tcp:10547
description = DHCPv6 on port 547
enabled     = Yes

[rmonitor]
plugin      = Echo
low_port    = tcp:560
port        = tcp:10560
description = rmonitor on port 560
enabled     = Yes

[NNTP.SSL]
plugin      = Echo
low_port    = tcp:563
port        = tcp:10563
description = NNTP over SSL on port 563
enabled     = Yes

[SMTP]
plugin      = Echo
low_port    = tcp:587
port        = tcp:10587
description = SMTP on port 587
enabled     = Yes

[FileMaker]
plugin      = Echo
low_port    = tcp:591
port        = tcp:10591
description = FileMaker on port 591
enabled     = Yes

[Microsoft_DCOM]
plugin      = Echo
low_port    = tcp:593
port        = tcp:10593
description = DCOM on port 593
enabled     = Yes

[Internet_Printing]
plugin      = Echo
low_port    = tcp:631
port        = tcp:10631
description = Printing on port 631
enabled     = Yes

[LDAPS]
plugin      = Echo
low_port    = tcp:636
port        = tcp:10636
description = SSL on port 636
enabled     = Yes

[MSDP.PIM]
plugin      = Echo
low_port    = tcp:639
port        = tcp:10639
description = (PIM) on port 639
enabled     = Yes

[LDP.MPLS]
plugin      = Echo
low_port    = tcp:646
port        = tcp:10646
description = (MPLS) on port 646
enabled     = Yes

[MSExchange]
plugin      = Echo
low_port    = tcp:691
port        = tcp:10691
description = Exchange on port 691
enabled     = Yes

[iSCSI]
plugin      = Echo
low_port    = tcp:860
port        = tcp:10860
description = iSCSI on port 860
enabled     = Yes

[rsync]
plugin      = Echo
low_port    = tcp:873
port        = tcp:10873
description = rsync on port 873
enabled     = Yes

[VMware.Server]
plugin      = Echo
low_port    = tcp:902
port        = tcp:10902
description = Server on port 902
enabled     = Yes

[SFTP]
plugin      = Echo
low_port    = tcp:989
port        = tcp:10989
description = SSL on port 989
enabled     = Yes

[SFTP]
plugin      = Echo
low_port    = tcp:990
port        = tcp:10990
description = SSL on port 990
enabled     = Yes

[IMAP4.SSL]
plugin      = Echo
low_port    = tcp:993
port        = tcp:10993
description = SSL on port 993
enabled     = Yes

[POP3.SL]
plugin      = Echo
low_port    = tcp:995
port        = tcp:10995
description = SSL on port 995
enabled     = Yes

[Microsoft.RPC]
plugin      = Echo
low_port    = tcp:1025
port        = tcp:1025
description = RPC on port 1025
enabled     = Yes

[Windows_Messenger]
plugin      = Echo
low_port    = tcp:1026
port        = tcp:1026
description = Messenger on port 1026
enabled     = Yes

[Windows_Messenger]
plugin      = Echo
low_port    = tcp:1027
port        = tcp:1027
description = Messenger on port 1027
enabled     = Yes

[Windows_Messenger]
plugin      = Echo
low_port    = tcp:1028
port        = tcp:1028
description = Messenger on port 1028
enabled     = Yes

[Windows_Messenger]
plugin      = Echo
low_port    = tcp:1029
port        = tcp:1029
description = Messenger on port 1029
enabled     = Yes

[SOCKS_Proxy]
plugin      = Echo
low_port    = tcp:1080
port        = tcp:1080
description = Proxy on port 1080
enabled     = Yes

[MyDoom]
plugin      = Echo
low_port    = tcp:1080
port        = tcp:1080
description = MyDoom on port 1080
enabled     = Yes

[OpenVPN]
plugin      = Echo
low_port    = tcp:1194
port        = tcp:1194
description = OpenVPN on port 1194
enabled     = Yes

[Kazaa]
plugin      = Echo
low_port    = tcp:1214
port        = tcp:1214
description = Kazaa on port 1214
enabled     = Yes

[Nessus]
plugin      = Echo
low_port    = tcp:1241
port        = tcp:1241
description = Nessus on port 1241
enabled     = Yes

[Dell_OpenManage]
plugin      = Echo
low_port    = tcp:1311
port        = tcp:1311
description = OpenManage on port 1311
enabled     = Yes

[WASTE]
plugin      = Echo
low_port    = tcp:1337
port        = tcp:1337
description = WASTE on port 1337
enabled     = Yes

[Microsoft_SQL]
plugin      = Echo
low_port    = tcp:1433
port        = tcp:1433
description = SQL on port 1433
enabled     = Yes

[Microsoft_SQL]
plugin      = Echo
low_port    = tcp:1434
port        = tcp:1434
description = SQL on port 1434
enabled     = Yes

[WINS]
plugin      = Echo
low_port    = tcp:1512
port        = tcp:1512
description = WINS on port 1512
enabled     = Yes

[Cisco_VQP]
plugin      = Echo
low_port    = tcp:1589
port        = tcp:1589
description = VQP on port 1589
enabled     = Yes

[L2TP]
plugin      = Echo
low_port    = tcp:1701
port        = tcp:1701
description = L2TP on port 1701
enabled     = Yes

[MS_PPTP]
plugin      = Echo
low_port    = tcp:1723
port        = tcp:1723
description = PPTP on port 1723
enabled     = Yes

[Steam]
plugin      = Echo
low_port    = tcp:1725
port        = tcp:1725
description = Steam on port 1725
enabled     = Yes

[CiscoWorks_2000]
plugin      = Echo
low_port    = tcp:1741
port        = tcp:1741
description = 2000 on port 1741
enabled     = Yes

[MS_Media_Server]
plugin      = Echo
low_port    = tcp:1755
port        = tcp:1755
description = Server on port 1755
enabled     = Yes

[RADIUS]
plugin      = Echo
low_port    = tcp:1812
port        = tcp:1812
description = RADIUS on port 1812
enabled     = Yes

[RADIUS]
plugin      = Echo
low_port    = tcp:1813
port        = tcp:1813
description = RADIUS on port 1813
enabled     = Yes

[MSN]
plugin      = Echo
low_port    = tcp:1863
port        = tcp:1863
description = MSN on port 1863
enabled     = Yes

[Cisco_HSRP]
plugin      = Echo
low_port    = tcp:1985
port        = tcp:1985
description = HSRP on port 1985
enabled     = Yes

[Cisco_SCCP]
plugin      = Echo
low_port    = tcp:2000
port        = tcp:2000
description = SCCP on port 2000
enabled     = Yes

[Cisco_ACS]
plugin      = Echo
low_port    = tcp:2002
port        = tcp:2002
description = ACS on port 2002
enabled     = Yes

[NFS]
plugin      = Echo
low_port    = tcp:2049
port        = tcp:2049
description = NFS on port 2049
enabled     = Yes

[cPanel]
plugin      = Echo
low_port    = tcp:2082
port        = tcp:2082
description = cPanel on port 2082
enabled     = Yes

[cPanel]
plugin      = Echo
low_port    = tcp:2083
port        = tcp:2083
description = cPanel on port 2083
enabled     = Yes

[Oracle_XDB]
plugin      = Echo
low_port    = tcp:2100
port        = tcp:2100
description = XDB on port 2100
enabled     = Yes

[DirectAdmin]
plugin      = Echo
low_port    = tcp:2222
port        = tcp:2222
description = DirectAdmin on port 2222
enabled     = Yes

[Halo]
plugin      = Echo
low_port    = tcp:2302
port        = tcp:2302
description = Halo on port 2302
enabled     = Yes

[Oracle_DB]
plugin      = Echo
low_port    = tcp:2483
port        = tcp:2483
description = DB on port 2483
enabled     = Yes

[Oracle_DB]
plugin      = Echo
low_port    = tcp:2484
port        = tcp:2484
description = DB on port 2484
enabled     = Yes

[Bagle.H]
plugin      = Echo
low_port    = tcp:2745
port        = tcp:2745
description = Bagle.H on port 2745
enabled     = Yes

[Symantec_AV]
plugin      = Echo
low_port    = tcp:2967
port        = tcp:2967
description = AV on port 2967
enabled     = Yes

[Interbase_DB]
plugin      = Echo
low_port    = tcp:3050
port        = tcp:3050
description = DB on port 3050
enabled     = Yes

[XBOX_Live]
plugin      = Echo
low_port    = tcp:3074
port        = tcp:3074
description = Live on port 3074
enabled     = Yes

[HTTP_Proxy]
plugin      = Echo
low_port    = tcp:3124
port        = tcp:3124
description = Proxy on port 3124
enabled     = Yes

[MyDoom]
plugin      = Echo
low_port    = tcp:3127
port        = tcp:3127
description = MyDoom on port 3127
enabled     = Yes

[HTTP_Proxy]
plugin      = Echo
low_port    = tcp:3128
port        = tcp:3128
description = Proxy on port 3128
enabled     = Yes

[GLBP]
plugin      = Echo
low_port    = tcp:3222
port        = tcp:3222
description = GLBP on port 3222
enabled     = Yes

[iSCSI_Target]
plugin      = Echo
low_port    = tcp:3260
port        = tcp:3260
description = Target on port 3260
enabled     = Yes

[MySQL]
plugin      = Echo
low_port    = tcp:3306
port        = tcp:3306
description = MySQL on port 3306
enabled     = Yes

[RDP]
plugin      = Echo
low_port    = tcp:3389
port        = tcp:3389
description = Server on port 3389
enabled     = Yes

[iTunes]
plugin      = Echo
low_port    = tcp:3689
port        = tcp:3689
description = iTunes on port 3689
enabled     = Yes

[Subversion]
plugin      = Echo
low_port    = tcp:3690
port        = tcp:3690
description = Subversion on port 3690
enabled     = Yes

[World_of_Warcraft]
plugin      = Echo
low_port    = tcp:3724
port        = tcp:3724
description = Warcraft on port 3724
enabled     = Yes

[Ventrilo]
plugin      = Echo
low_port    = tcp:3784
port        = tcp:3784
description = Ventrilo on port 3784
enabled     = Yes

[Ventrilo]
plugin      = Echo
low_port    = tcp:3785
port        = tcp:3785
description = Ventrilo on port 3785
enabled     = Yes

[mSQL]
plugin      = Echo
low_port    = tcp:4333
port        = tcp:4333
description = mSQL on port 4333
enabled     = Yes

[Blaster]
plugin      = Echo
low_port    = tcp:4444
port        = tcp:4444
description = Blaster on port 4444
enabled     = Yes

[Google_Desktop]
plugin      = Echo
low_port    = tcp:4664
port        = tcp:4664
description = Desktop on port 4664
enabled     = Yes

[eMule]
plugin      = Echo
low_port    = tcp:4672
port        = tcp:4672
description = eMule on port 4672
enabled     = Yes

[Radmin]
plugin      = Echo
low_port    = tcp:4899
port        = tcp:4899
description = Radmin on port 4899
enabled     = Yes

[UPnP]
plugin      = Echo
low_port    = tcp:5000
port        = tcp:5000
description = UPnP on port 5000
enabled     = Yes

[Slingbox]
plugin      = Echo
low_port    = tcp:5001
port        = tcp:5001
description = Slingbox on port 5001
enabled     = Yes

[iperf]
plugin      = Echo
low_port    = tcp:5001
port        = tcp:5001
description = iperf on port 5001
enabled     = Yes

[RTP]
plugin      = Echo
low_port    = tcp:5004
port        = tcp:5004
description = RTP on port 5004
enabled     = Yes

[RTP]
plugin      = Echo
low_port    = tcp:5005
port        = tcp:5005
description = RTP on port 5005
enabled     = Yes

[Yahoo!_Messenger]
plugin      = Echo
low_port    = tcp:5050
port        = tcp:5050
description = Messenger on port 5050
enabled     = Yes

[SIP]
plugin      = Echo
low_port    = tcp:5060
port        = tcp:5060
description = SIP on port 5060
enabled     = Yes

[AIM_ICQ]
plugin      = Echo
low_port    = tcp:5190
port        = tcp:5190
description = AIM/ICQ on port 5190
enabled     = Yes

[XMPP_Jabber]
plugin      = Echo
low_port    = tcp:5222
port        = tcp:5222
description = XMPP/Jabber on port 5222
enabled     = Yes

[XMPP_Jabber]
plugin      = Echo
low_port    = tcp:5223
port        = tcp:5223
description = XMPP/Jabber on port 5223
enabled     = Yes

[PostgreSQL]
plugin      = Echo
low_port    = tcp:5432
port        = tcp:5432
description = PostgreSQL on port 5432
enabled     = Yes

[VNC]
plugin      = Echo
low_port    = tcp:5500
port        = tcp:5500
description = Server on port 5500
enabled     = Yes

[Sasser]
plugin      = Echo
low_port    = tcp:5554
port        = tcp:5554
description = Sasser on port 5554
enabled     = Yes

[pcAnywhere]
plugin      = Echo
low_port    = tcp:5631
port        = tcp:5631
description = pcAnywhere on port 5631
enabled     = Yes

[pcAnywhere]
plugin      = Echo
low_port    = tcp:5632
port        = tcp:5632
description = pcAnywhere on port 5632
enabled     = Yes

[VNC.HTTP]
plugin      = Echo
low_port    = tcp:5800
port        = tcp:5800
description = HTTP on port 5800
enabled     = Yes

[VNC]
plugin      = Echo
low_port    = tcp:5900
port        = tcp:5900
description = Server on port 5900
enabled     = Yes

[X11]
plugin      = Echo
low_port    = tcp:6000
port        = tcp:6000
description = X11 on port 6000
enabled     = Yes

[X11]
plugin      = Echo
low_port    = tcp:6001
port        = tcp:6001
description = X11 on port 6001
enabled     = Yes

[Battle.net]
plugin      = Echo
low_port    = tcp:6112
port        = tcp:6112
description = Battle.net on port 6112
enabled     = Yes

[DameWare]
plugin      = Echo
low_port    = tcp:6129
port        = tcp:6129
description = DameWare on port 6129
enabled     = Yes

[WinMX]
plugin      = Echo
low_port    = tcp:6257
port        = tcp:6257
description = WinMX on port 6257
enabled     = Yes

[Gnutella]
plugin      = Echo
low_port    = tcp:6346
port        = tcp:6346
description = Gnutella on port 6346
enabled     = Yes

[Gnutella]
plugin      = Echo
low_port    = tcp:6347
port        = tcp:6347
description = Gnutella on port 6347
enabled     = Yes

[GameSpy_Arcade]
plugin      = Echo
low_port    = tcp:6500
port        = tcp:6500
description = Arcade on port 6500
enabled     = Yes

[SANE]
plugin      = Echo
low_port    = tcp:6566
port        = tcp:6566
description = SANE on port 6566
enabled     = Yes

[AnalogX]
plugin      = Echo
low_port    = tcp:6588
port        = tcp:6588
description = AnalogX on port 6588
enabled     = Yes

[IRC]
plugin      = Echo
low_port    = tcp:6665
port        = tcp:6665
description = IRC on port 6665
enabled     = Yes

[IRC]
plugin      = Echo
low_port    = tcp:6666
port        = tcp:6666
description = IRC on port 6666
enabled     = Yes

[IRC]
plugin      = Echo
low_port    = tcp:6667
port        = tcp:6667
description = IRC on port 6667
enabled     = Yes

[IRC]
plugin      = Echo
low_port    = tcp:6668
port        = tcp:6668
description = IRC on port 6668
enabled     = Yes

[IRC]
plugin      = Echo
low_port    = tcp:6669
port        = tcp:6669
description = IRC on port 6669
enabled     = Yes

[IRC.SSL]
plugin      = Echo
low_port    = tcp:6679
port        = tcp:6679
description = SSL on port 6679
enabled     = Yes

[IRC.SSL]
plugin      = Echo
low_port    = tcp:6680
port        = tcp:6680
description = SSL on port 6680
enabled     = Yes

[IRC.SSL]
plugin      = Echo
low_port    = tcp:6681
port        = tcp:6681
description = SSL on port 6681
enabled     = Yes

[IRC.SSL]
plugin      = Echo
low_port    = tcp:6682
port        = tcp:6682
description = SSL on port 6682
enabled     = Yes

[IRC.SSL]
plugin      = Echo
low_port    = tcp:6683
port        = tcp:6683
description = SSL on port 6683
enabled     = Yes

[IRC.SSL]
plugin      = Echo
low_port    = tcp:6684
port        = tcp:6684
description = SSL on port 6684
enabled     = Yes

[IRC.SSL]
plugin      = Echo
low_port    = tcp:6685
port        = tcp:6685
description = SSL on port 6685
enabled     = Yes

[IRC.SSL]
plugin      = Echo
low_port    = tcp:6686
port        = tcp:6686
description = SSL on port 6686
enabled     = Yes

[IRC.SSL]
plugin      = Echo
low_port    = tcp:6687
port        = tcp:6687
description = SSL on port 6687
enabled     = Yes

[IRC.SSL]
plugin      = Echo
low_port    = tcp:6688
port        = tcp:6688
description = SSL on port 6688
enabled     = Yes

[IRC.SSL]
plugin      = Echo
low_port    = tcp:6689
port        = tcp:6689
description = SSL on port 6689
enabled     = Yes

[IRC.SSL]
plugin      = Echo
low_port    = tcp:6690
port        = tcp:6690
description = SSL on port 6690
enabled     = Yes

[IRC.SSL]
plugin      = Echo
low_port    = tcp:6691
port        = tcp:6691
description = SSL on port 6691
enabled     = Yes

[IRC.SSL]
plugin      = Echo
low_port    = tcp:6692
port        = tcp:6692
description = SSL on port 6692
enabled     = Yes

[IRC.SSL]
plugin      = Echo
low_port    = tcp:6693
port        = tcp:6693
description = SSL on port 6693
enabled     = Yes

[IRC.SSL]
plugin      = Echo
low_port    = tcp:6694
port        = tcp:6694
description = SSL on port 6694
enabled     = Yes

[IRC.SSL]
plugin      = Echo
low_port    = tcp:6695
port        = tcp:6695
description = SSL on port 6695
enabled     = Yes

[IRC.SSL]
plugin      = Echo
low_port    = tcp:6696
port        = tcp:6696
description = SSL on port 6696
enabled     = Yes

[IRC.SSL]
plugin      = Echo
low_port    = tcp:6697
port        = tcp:6697
description = SSL on port 6697
enabled     = Yes

[Napster]
plugin      = Echo
low_port    = tcp:6699
port        = tcp:6699
description = Napster on port 6699
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6881
port        = tcp:6881
description = BitTorrent on port 6881
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6882
port        = tcp:6882
description = BitTorrent on port 6882
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6883
port        = tcp:6883
description = BitTorrent on port 6883
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6884
port        = tcp:6884
description = BitTorrent on port 6884
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6885
port        = tcp:6885
description = BitTorrent on port 6885
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6886
port        = tcp:6886
description = BitTorrent on port 6886
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6887
port        = tcp:6887
description = BitTorrent on port 6887
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6888
port        = tcp:6888
description = BitTorrent on port 6888
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6889
port        = tcp:6889
description = BitTorrent on port 6889
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6890
port        = tcp:6890
description = BitTorrent on port 6890
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6891
port        = tcp:6891
description = BitTorrent on port 6891
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6892
port        = tcp:6892
description = BitTorrent on port 6892
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6893
port        = tcp:6893
description = BitTorrent on port 6893
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6894
port        = tcp:6894
description = BitTorrent on port 6894
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6895
port        = tcp:6895
description = BitTorrent on port 6895
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6896
port        = tcp:6896
description = BitTorrent on port 6896
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6897
port        = tcp:6897
description = BitTorrent on port 6897
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6898
port        = tcp:6898
description = BitTorrent on port 6898
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6899
port        = tcp:6899
description = BitTorrent on port 6899
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6900
port        = tcp:6900
description = BitTorrent on port 6900
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6901
port        = tcp:6901
description = BitTorrent on port 6901
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6902
port        = tcp:6902
description = BitTorrent on port 6902
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6903
port        = tcp:6903
description = BitTorrent on port 6903
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6904
port        = tcp:6904
description = BitTorrent on port 6904
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6905
port        = tcp:6905
description = BitTorrent on port 6905
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6906
port        = tcp:6906
description = BitTorrent on port 6906
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6907
port        = tcp:6907
description = BitTorrent on port 6907
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6908
port        = tcp:6908
description = BitTorrent on port 6908
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6909
port        = tcp:6909
description = BitTorrent on port 6909
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6910
port        = tcp:6910
description = BitTorrent on port 6910
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6911
port        = tcp:6911
description = BitTorrent on port 6911
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6912
port        = tcp:6912
description = BitTorrent on port 6912
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6913
port        = tcp:6913
description = BitTorrent on port 6913
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6914
port        = tcp:6914
description = BitTorrent on port 6914
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6915
port        = tcp:6915
description = BitTorrent on port 6915
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6916
port        = tcp:6916
description = BitTorrent on port 6916
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6917
port        = tcp:6917
description = BitTorrent on port 6917
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6918
port        = tcp:6918
description = BitTorrent on port 6918
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6919
port        = tcp:6919
description = BitTorrent on port 6919
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6920
port        = tcp:6920
description = BitTorrent on port 6920
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6921
port        = tcp:6921
description = BitTorrent on port 6921
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6922
port        = tcp:6922
description = BitTorrent on port 6922
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6923
port        = tcp:6923
description = BitTorrent on port 6923
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6924
port        = tcp:6924
description = BitTorrent on port 6924
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6925
port        = tcp:6925
description = BitTorrent on port 6925
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6926
port        = tcp:6926
description = BitTorrent on port 6926
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6927
port        = tcp:6927
description = BitTorrent on port 6927
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6928
port        = tcp:6928
description = BitTorrent on port 6928
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6929
port        = tcp:6929
description = BitTorrent on port 6929
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6930
port        = tcp:6930
description = BitTorrent on port 6930
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6931
port        = tcp:6931
description = BitTorrent on port 6931
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6932
port        = tcp:6932
description = BitTorrent on port 6932
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6933
port        = tcp:6933
description = BitTorrent on port 6933
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6934
port        = tcp:6934
description = BitTorrent on port 6934
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6935
port        = tcp:6935
description = BitTorrent on port 6935
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6936
port        = tcp:6936
description = BitTorrent on port 6936
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6937
port        = tcp:6937
description = BitTorrent on port 6937
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6938
port        = tcp:6938
description = BitTorrent on port 6938
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6939
port        = tcp:6939
description = BitTorrent on port 6939
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6940
port        = tcp:6940
description = BitTorrent on port 6940
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6941
port        = tcp:6941
description = BitTorrent on port 6941
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6942
port        = tcp:6942
description = BitTorrent on port 6942
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6943
port        = tcp:6943
description = BitTorrent on port 6943
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6944
port        = tcp:6944
description = BitTorrent on port 6944
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6945
port        = tcp:6945
description = BitTorrent on port 6945
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6946
port        = tcp:6946
description = BitTorrent on port 6946
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6947
port        = tcp:6947
description = BitTorrent on port 6947
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6948
port        = tcp:6948
description = BitTorrent on port 6948
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6949
port        = tcp:6949
description = BitTorrent on port 6949
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6950
port        = tcp:6950
description = BitTorrent on port 6950
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6951
port        = tcp:6951
description = BitTorrent on port 6951
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6952
port        = tcp:6952
description = BitTorrent on port 6952
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6953
port        = tcp:6953
description = BitTorrent on port 6953
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6954
port        = tcp:6954
description = BitTorrent on port 6954
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6955
port        = tcp:6955
description = BitTorrent on port 6955
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6956
port        = tcp:6956
description = BitTorrent on port 6956
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6957
port        = tcp:6957
description = BitTorrent on port 6957
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6958
port        = tcp:6958
description = BitTorrent on port 6958
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6959
port        = tcp:6959
description = BitTorrent on port 6959
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6960
port        = tcp:6960
description = BitTorrent on port 6960
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6961
port        = tcp:6961
description = BitTorrent on port 6961
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6962
port        = tcp:6962
description = BitTorrent on port 6962
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6963
port        = tcp:6963
description = BitTorrent on port 6963
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6964
port        = tcp:6964
description = BitTorrent on port 6964
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6965
port        = tcp:6965
description = BitTorrent on port 6965
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6966
port        = tcp:6966
description = BitTorrent on port 6966
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6967
port        = tcp:6967
description = BitTorrent on port 6967
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6968
port        = tcp:6968
description = BitTorrent on port 6968
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6969
port        = tcp:6969
description = BitTorrent on port 6969
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6970
port        = tcp:6970
description = BitTorrent on port 6970
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6971
port        = tcp:6971
description = BitTorrent on port 6971
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6972
port        = tcp:6972
description = BitTorrent on port 6972
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6973
port        = tcp:6973
description = BitTorrent on port 6973
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6974
port        = tcp:6974
description = BitTorrent on port 6974
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6975
port        = tcp:6975
description = BitTorrent on port 6975
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6976
port        = tcp:6976
description = BitTorrent on port 6976
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6977
port        = tcp:6977
description = BitTorrent on port 6977
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6978
port        = tcp:6978
description = BitTorrent on port 6978
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6979
port        = tcp:6979
description = BitTorrent on port 6979
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6980
port        = tcp:6980
description = BitTorrent on port 6980
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6981
port        = tcp:6981
description = BitTorrent on port 6981
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6982
port        = tcp:6982
description = BitTorrent on port 6982
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6983
port        = tcp:6983
description = BitTorrent on port 6983
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6984
port        = tcp:6984
description = BitTorrent on port 6984
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6985
port        = tcp:6985
description = BitTorrent on port 6985
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6986
port        = tcp:6986
description = BitTorrent on port 6986
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6987
port        = tcp:6987
description = BitTorrent on port 6987
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6988
port        = tcp:6988
description = BitTorrent on port 6988
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6989
port        = tcp:6989
description = BitTorrent on port 6989
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6990
port        = tcp:6990
description = BitTorrent on port 6990
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6991
port        = tcp:6991
description = BitTorrent on port 6991
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6992
port        = tcp:6992
description = BitTorrent on port 6992
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6993
port        = tcp:6993
description = BitTorrent on port 6993
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6994
port        = tcp:6994
description = BitTorrent on port 6994
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6995
port        = tcp:6995
description = BitTorrent on port 6995
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6996
port        = tcp:6996
description = BitTorrent on port 6996
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6997
port        = tcp:6997
description = BitTorrent on port 6997
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6998
port        = tcp:6998
description = BitTorrent on port 6998
enabled     = Yes

[BitTorrent]
plugin      = Echo
low_port    = tcp:6999
port        = tcp:6999
description = BitTorrent on port 6999
enabled     = Yes

[Windows_Live]
plugin      = Echo
low_port    = tcp:6891
port        = tcp:6891
description = Live on port 6891
enabled     = Yes

[Windows_Live]
plugin      = Echo
low_port    = tcp:6892
port        = tcp:6892
description = Live on port 6892
enabled     = Yes

[Windows_Live]
plugin      = Echo
low_port    = tcp:6893
port        = tcp:6893
description = Live on port 6893
enabled     = Yes

[Windows_Live]
plugin      = Echo
low_port    = tcp:6894
port        = tcp:6894
description = Live on port 6894
enabled     = Yes

[Windows_Live]
plugin      = Echo
low_port    = tcp:6895
port        = tcp:6895
description = Live on port 6895
enabled     = Yes

[Windows_Live]
plugin      = Echo
low_port    = tcp:6896
port        = tcp:6896
description = Live on port 6896
enabled     = Yes

[Windows_Live]
plugin      = Echo
low_port    = tcp:6897
port        = tcp:6897
description = Live on port 6897
enabled     = Yes

[Windows_Live]
plugin      = Echo
low_port    = tcp:6898
port        = tcp:6898
description = Live on port 6898
enabled     = Yes

[Windows_Live]
plugin      = Echo
low_port    = tcp:6899
port        = tcp:6899
description = Live on port 6899
enabled     = Yes

[Windows_Live]
plugin      = Echo
low_port    = tcp:6900
port        = tcp:6900
description = Live on port 6900
enabled     = Yes

[Windows_Live]
plugin      = Echo
low_port    = tcp:6901
port        = tcp:6901
description = Live on port 6901
enabled     = Yes

[Quicktime]
plugin      = Echo
low_port    = tcp:6970
port        = tcp:6970
description = Quicktime on port 6970
enabled     = Yes

[GhostSurf]
plugin      = Echo
low_port    = tcp:7212
port        = tcp:7212
description = GhostSurf on port 7212
enabled     = Yes

[CU-SeeMe]
plugin      = Echo
low_port    = tcp:7648
port        = tcp:7648
description = CU-SeeMe on port 7648
enabled     = Yes

[CU-SeeMe]
plugin      = Echo
low_port    = tcp:7649
port        = tcp:7649
description = CU-SeeMe on port 7649
enabled     = Yes

[Internet_Radio]
plugin      = Echo
low_port    = tcp:8000
port        = tcp:8000
description = Radio on port 8000
enabled     = Yes

[HTTP_Proxy]
plugin      = Echo
low_port    = tcp:8080
port        = tcp:8080
description = Proxy on port 8080
enabled     = Yes

[Kaspersky_AV]
plugin      = Echo
low_port    = tcp:8086
port        = tcp:8086
description = AV on port 8086
enabled     = Yes

[Kaspersky_AV]
plugin      = Echo
low_port    = tcp:8087
port        = tcp:8087
description = AV on port 8087
enabled     = Yes

[Privoxy]
plugin      = Echo
low_port    = tcp:8118
port        = tcp:8118
description = Privoxy on port 8118
enabled     = Yes

[VMware_Server]
plugin      = Echo
low_port    = tcp:8200
port        = tcp:8200
description = Server on port 8200
enabled     = Yes

[Adobe_ColdFusion]
plugin      = Echo
low_port    = tcp:8500
port        = tcp:8500
description = ColdFusion on port 8500
enabled     = Yes

[TeamSpeak]
plugin      = Echo
low_port    = tcp:8767
port        = tcp:8767
description = TeamSpeak on port 8767
enabled     = Yes

[Bagle.B]
plugin      = Echo
low_port    = tcp:8866
port        = tcp:8866
description = Bagle.B on port 8866
enabled     = Yes

[HP_JetDirect]
plugin      = Echo
low_port    = tcp:9100
port        = tcp:9100
description = JetDirect on port 9100
enabled     = Yes

[Bacula]
plugin      = Echo
low_port    = tcp:9101
port        = tcp:9101
description = Bacula on port 9101
enabled     = Yes

[Bacula]
plugin      = Echo
low_port    = tcp:9102
port        = tcp:9102
description = Bacula on port 9102
enabled     = Yes

[Bacula]
plugin      = Echo
low_port    = tcp:9103
port        = tcp:9103
description = Bacula on port 9103
enabled     = Yes

[MXit]
plugin      = Echo
low_port    = tcp:9119
port        = tcp:9119
description = MXit on port 9119
enabled     = Yes

[WebDAV]
plugin      = Echo
low_port    = tcp:9800
port        = tcp:9800
description = WebDAV on port 9800
enabled     = Yes

[Dabber]
plugin      = Echo
low_port    = tcp:9898
port        = tcp:9898
description = Dabber on port 9898
enabled     = Yes

[Urchin]
plugin      = Echo
low_port    = tcp:9999
port        = tcp:9999
description = Urchin on port 9999
enabled     = Yes

[Webmin]
plugin      = Echo
low_port    = tcp:10000
port        = tcp:10000
description = Webmin on port 10000
enabled     = Yes

[BackupExec]
plugin      = Echo
low_port    = tcp:10000
port        = tcp:10000
description = BackupExec on port 10000
enabled     = Yes

[NetIQ]
plugin      = Echo
low_port    = tcp:10113
port        = tcp:10113
description = NetIQ on port 10113
enabled     = Yes

[NetIQ]
plugin      = Echo
low_port    = tcp:10114
port        = tcp:10114
description = NetIQ on port 10114
enabled     = Yes

[NetIQ]
plugin      = Echo
low_port    = tcp:10115
port        = tcp:10115
description = NetIQ on port 10115
enabled     = Yes

[NetIQ]
plugin      = Echo
low_port    = tcp:10116
port        = tcp:10116
description = NetIQ on port 10116
enabled     = Yes

[OpenPGP]
plugin      = Echo
low_port    = tcp:11371
port        = tcp:11371
description = OpenPGP on port 11371
enabled     = Yes

[Second_Life]
plugin      = Echo
low_port    = tcp:12035
port        = tcp:12035
description = Life on port 12035
enabled     = Yes

[Second_Life]
plugin      = Echo
low_port    = tcp:12036
port        = tcp:12036
description = Life on port 12036
enabled     = Yes

[NetBus]
plugin      = Echo
low_port    = tcp:12345
port        = tcp:12345
description = NetBus on port 12345
enabled     = Yes

[NetBackup]
plugin      = Echo
low_port    = tcp:13720
port        = tcp:13720
description = NetBackup on port 13720
enabled     = Yes

[NetBackup]
plugin      = Echo
low_port    = tcp:13721
port        = tcp:13721
description = NetBackup on port 13721
enabled     = Yes

[Battlefield]
plugin      = Echo
low_port    = tcp:14567
port        = tcp:14567
description = Battlefield on port 14567
enabled     = Yes

[Dipnet_Oddbob]
plugin      = Echo
low_port    = tcp:15118
port        = tcp:15118
description = Dipnet/Oddbob on port 15118
enabled     = Yes

[AdminSecure]
plugin      = Echo
low_port    = tcp:19226
port        = tcp:19226
description = AdminSecure on port 19226
enabled     = Yes

[Ensim]
plugin      = Echo
low_port    = tcp:19638
port        = tcp:19638
description = Ensim on port 19638
enabled     = Yes

[Usermin]
plugin      = Echo
low_port    = tcp:20000
port        = tcp:20000
description = Usermin on port 20000
enabled     = Yes

[Synergy]
plugin      = Echo
low_port    = tcp:24800
port        = tcp:24800
description = Synergy on port 24800
enabled     = Yes

[Xfire]
plugin      = Echo
low_port    = tcp:25999
port        = tcp:25999
description = Xfire on port 25999
enabled     = Yes

[Half-Life]
plugin      = Echo
low_port    = tcp:27015
port        = tcp:27015
description = Half-Life on port 27015
enabled     = Yes

[Call_of_Duty]
plugin      = Echo
low_port    = tcp:28960
port        = tcp:28960
description = Duty on port 28960
enabled     = Yes

[traceroute]
plugin      = Echo
low_port    = tcp:33434
port        = tcp:33434
description = traceroute on port 33434
enabled     = Yes
