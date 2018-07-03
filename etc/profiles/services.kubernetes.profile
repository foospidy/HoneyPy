# HoneyPy Copyright (C) foospidy
# services.kubernetes.profile
# Important: service names must not contain spaces.
# Important: use port redirecting for services that listen on ports below 1024 (see https://github.com/foospidy/ipt-kit).
# kubernetes profile

[KubeAPI]
plugin      = Web
low_port    = tcp:6443
port        = tcp:6443
description = Kubernetes API Server
enabled     = Yes

[Kube.etcd]
plugin      = Echo
low_port    = tcp:2379
port        = tcp:2379
description = etcd server client API
enabled     = Yes

[Kube.etcd]
plugin      = Echo
low_port    = tcp:2380
port        = tcp:2380
description = etcd server client API
enabled     = Yes

[Kube.cAdvisor]
plugin      = Web
low_port    = tcp:4194
port        = tcp:4194
description = cAdvisor
enabled     = Yes

[Kube.healthzPort]
plugin      = Echo
low_port    = tcp:10248
port        = tcp:10248
description = healthzPort
enabled     = Yes

[KubeletAPI]
plugin      = Web
low_port    = tcp:10250
port        = tcp:10250
description = Kubelet API
enabled     = Yes

[KubeScheduler]
plugin      = Web
low_port    = tcp:10251
port        = tcp:10251
description = kube-scheduler
enabled     = Yes

[KubeScheduler]
plugin      = Web
low_port    = tcp:10252
port        = tcp:10252
description = kube-controller-manager
enabled     = Yes

[KubeScheduler]
plugin      = Web
low_port    = tcp:10255
port        = tcp:10255
description = Read-Only Kubelet API
enabled     = Yes
