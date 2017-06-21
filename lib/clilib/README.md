# clilib
A library of emulated command line commands. The goal of this library is to
emulate the most common cammands for Unix and Windows. The primary
use case for this library is in honeypots.

### Usage
Import clilib into your script with `from clilib import *`

You should now be able to call command cuntions form your script. Command functions always return printable output so you can store the output to a variable or print it directly. Examples:

`myvar = print uname('-a')`
`print myvar`

or

`print uname('-a')`

more examples are in the test script here: https://github.com/foospidy/HoneyPy/blob/master/lib/clilib/test.py
