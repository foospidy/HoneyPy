# HoneyPy Copyright (C) 2013-2016 foospidy
# services.peer_to_peer.profile
# Important: service names must not contain spaces.
# Important: use port redirecting for services that listen on ports below 1024 (see https://github.com/foospidy/ipt-kit).
# Streaming related ports as noted by http://packetlife.net/media/library/23/common_ports.pdf

[MS_Media_Server]
plugin      = Echo
low_port    = tcp:1755
port        = tcp:1755
description = MS Media Server port 1755
enabled     = Yes

[Ventrilo]
plugin      = Echo
low_port    = tcp:3784
port        = tcp:3784
description = Ventrilo port 3784
enabled     = Yes

[Ventrilo]
plugin      = Echo
low_port    = tcp:3785
port        = tcp:3785
description = Ventrilo port 3785
enabled     = Yes

[Slingbox]
plugin      = Echo
low_port    = tcp:5001
port        = tcp:5001
description = Slingbox port 5001
enabled     = Yes

[RTP]
plugin      = Echo
low_port    = tcp:5004
port        = tcp:5004
description = RTP port 5004
enabled     = Yes

[RTP]
plugin      = Echo
low_port    = tcp:5005
port        = tcp:5005
description = RTP port 5005
enabled     = Yes

[SIP]
plugin      = Echo
low_port    = tcp:5060
port        = tcp:5060
description = SIP port 5060
enabled     = Yes

[Quicktime]
plugin      = Echo
low_port    = tcp:6970
port        = tcp:6970
description = Quicktime port 6970
enabled     = Yes

[Internet_Radio]
plugin      = Echo
low_port    = tcp:8000
port        = tcp:8000
description = Internet Radio port 8000
enabled     = Yes

[Synergy]
plugin      = Echo
low_port    = tcp:24800
port        = tcp:24800
description = Synergy port 24800
enabled     = Yes
