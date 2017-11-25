# Developers

The core of HoneyPy is a framework that handles configuring and launching services as well as logging. Developers can easily create new service plugin or logging plugin to extend HoneyPy's capability.

Terms:

- Plugin - a service plugin that implements a network protocol (e.g. Telnet, SSH, HTTP, etc). All plugins reside in the `plugins` directory.
- Logger - a logging plugin that sends event data to an external service or SIEM (e.g. Twitter, HoneyDB, Splunk, etc.). All loggers reside in the `loggers` directory.

## Plugins

Hopefully creating new plugins is easy. HoneyPy takes care of sending/receiving data and logging, all you have to do is write the custom protocol/logic. The service emulators in the plugins directory can be used as templates to create new emulators.

Example: [https://github.com/foospidy/HoneyPy/blob/master/plugins/HashCountRandom/HashCountRandom.py](https://github.com/foospidy/HoneyPy/blob/master/plugins/HashCountRandom/HashCountRandom.py)

There are three sections to edit: custom import, custom protocol, and custom functions. To keep the template well organized, you should only make modifciaitons in the designated sections, note the comments that denote each section.

Example of custom import. Import the Python modules you need:

```python
### START CUSTOM IMPORT
import time
import os
import md5
### END CUSTOM IMPORT
```

Next, use the custom protocol section to write your logic. use the `self.tx()` function to transfer (send) data to the socket, and use the `self.rx()` function to receive data from the socket.

```python
### START CUSTOM PROTOCOL ###########################################################
self.tx('ACCEPT_CONN: ' + str(self.remote_host) + ':' + str(self.remote_port) + '\n')
count = 0

while True:
	count = count + 1
	self.tx(self.md5sum(count) + ':' + str(os.urandom(99)) + '\n')
	self.rx()
	time.sleep(1)

### END CUSTOM PROTOCOL #############################################################
```

Add custom functions as needed at the bottom. All functions must have the first parameter be `self`. When you call custom functions from the custom protocol section you must prefix them with `self.`, for example: `self.md5sum('test')`

```python
### START CUSTOM FUNCTIONS ##########################################################
def md5sum(self, data):
	m = md5.new()
	m.update(str(data))
	return m.hexdigest()

### END CUSTOM FUNCTIONS ############################################################
```

## Loggers

todo
