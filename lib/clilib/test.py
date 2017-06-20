#!/usr/bin/python

from clilib import * 

print man('')
print man('uname')

print uname()
print uname('-a')

print echo()
print echo('test')
print echo("-e '\x67\x61\x79\x66\x67\x74'")

print "rm soemthing"
print rm()
print "rm -rf somepath"
print rm('/some/file/path')

print tftp()

print busybox('ECCHI')
print busybox('thing')
print busybox()

print enable()
