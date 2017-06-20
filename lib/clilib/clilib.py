import os
import sys

sys.dont_write_bytecode = True

UNIX    = {'posix', 'mac'}
WINDOWS = {'nt'}

if os.name in UNIX:
	from unix import *
elif os.name in WINDOWS:
	from windows import *
else:
	print 'Error!'
