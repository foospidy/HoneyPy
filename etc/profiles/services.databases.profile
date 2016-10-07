# HoneyPy Copyright (C) 2013-2016 foospidy
# services.peer_to_peer.profile
# Important: service names must not contain spaces.
# Important: use port redirecting for services that listen on ports below 1024 (see https://github.com/foospidy/ipt-kit).

[MSSQL]
plugin      = Echo
low_port    = tcp:1433
port        = tcp:1433
description = MSSQL port 1433
enabled     = Yes

[MSSQL]
plugin      = Echo
low_port    = tcp:1434
port        = tcp:1434
description = MSSQL port 1434
enabled     = Yes

[OracleXDB]
plugin      = Echo
low_port    = tcp:2100
port        = tcp:2100
description = Oracle XDB port 2100
enabled     = Yes

[OracleDB]
plugin      = Echo
low_port    = tcp:2483
port        = tcp:2483
description = Oracle XDB port 2483
enabled     = Yes

[OracleDB]
plugin      = Echo
low_port    = tcp:2484
port        = tcp:2484
description = Oracle DB port 2484
enabled     = Yes

[InterbaseDB]
plugin      = Echo
low_port    = tcp:3050
port        = tcp:3050
description = Interbase DB port 3050
enabled     = Yes

[MySQL]
plugin      = Echo
low_port    = tcp:3306
port        = tcp:3306
description = MySQL DB port 3306
enabled     = Yes

[mSQL]
plugin      = Echo
low_port    = tcp:4333
port        = tcp:4333
description = mSQL port 4333
enabled     = Yes

[PostgreSQL]
plugin      = Echo
low_port    = tcp:5432
port        = tcp:5432
description = PostgreSQL port 5432
enabled     = Yes

[DB2]
plugin      = Echo
low_port    = tcp:50000
port        = tcp:50000
description = DB2 port 50000
enabled     = Yes
