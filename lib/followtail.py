# Twisted FollowTail
# Mohit Muthanna <http://www.muthanna.com>
#
# A Twisted version of POE::Wheel::FollowTail. Adapted from
# a post by Kragen Sitaker on the Kragen-hacks mailing list.
#
# http://lists.canonical.org/pipermail/kragen-hacks/2005-June/000413.html
# http://0xfe.blogspot.com/2006/03/following-log-file-with-twisted.html

from twisted.internet import reactor
from twisted.protocols import basic
import os, stat

class FollowTail:
  from os import linesep as newline
  __line_buffer = ""

  def __init__( self, filename = None, seekend = True, delay = 1 ):
    self.filename = filename
    self.delay = delay
    self.seekend = seekend
    self.keeprunning = False

  def fileIdentity( self, struct_stat ):
    return struct_stat[stat.ST_DEV], struct_stat[stat.ST_INO]

  def start( self ):
    self.keeprunning = True
    self.followTail()

  def stop( self ):
    self.keeprunning = False

  def followTail( self, fileobj = None, fstat = None, offset = 0 ):
    if fileobj is None:
      fileobj = open( self.filename )
      if self.seekend: fileobj.seek( 0, 2 )
      # Save offset of reference pointer
      offset = fileobj.tell()

    # Seek to the reference pointer
    fileobj.seek(offset)

    line = fileobj.read()
    if line: self.dataReceived( line )

    # Save new reference pointer after read
    offset = fileobj.tell()

    if fstat is None: fstat = os.fstat( fileobj.fileno() )

    try: stat = os.stat( self.filename )
    except: stat = fstat

    if self.fileIdentity( stat ) != self.fileIdentity( fstat ):
      fileobj = open( self.filename )
      offset = 0
      fstat = os.fstat( fileobj.fileno() )
      self.fileReset()

    if self.keeprunning:
      reactor.callLater( self.delay, lambda: self.followTail( fileobj, fstat, offset ) )

  def dataReceived( self, data ):
    # Fill buffer
    self.__line_buffer += data

    # Split lines
    lines = self.__line_buffer.splitlines()

    if not data.endswith( self.newline ):
      self.__line_buffer = lines.pop()
    else:
      self.__line_buffer = ""

    for line in lines:
      self.lineReceived( line )

  def lineReceived( self, line ):
    """Override This"""

  def fileReset( self ):
    """Override This"""
