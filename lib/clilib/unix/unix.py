from busybox import *
from cd import *
from echo import *
from enable import *
from rm import *
from sh import *
from tftp import *
from uname import *
from wget import *
from which import *
from whoami import *


def man(command=None):
  if None == command or '' == command:
    return 'What manual page do you want?'
  else:
    return eval(command).__doc__
