def tftp(params=None):
	"""
TFTP(1)                                                                BSD General Commands Manual                                                                TFTP(1)

NAME
     tftp - trivial file transfer program

SYNOPSIS
     tftp [host]

DESCRIPTION
     Tftp is the user interface to the Internet TFTP (Trivial File Transfer Protocol), which allows users to transfer files to and from a remote machine.  The remote
     host may be specified on the command line, in which case tftp uses host as the default host for future transfers (see the connect command below).

COMMANDS
     Once tftp is running, it issues the prompt and recognizes the following commands:

     ? command-name ...
              Print help information.

     ascii    Shorthand for "mode ascii"

     binary   Shorthand for "mode binary"

     connect host-name [port]
              Set the host (and optionally port) for transfers.  Note that the TFTP protocol, unlike the FTP protocol, does not maintain connections betwen transfers;
              thus, the connect command does not actually create a connection, but merely remembers what host is to be used for transfers.  You do not have to use the
              connect command; the remote host can be specified as part of the get or put commands.

     get filename
     get remotename localname
     get file1 file2 ... fileN
              Get a file or set of files from the specified sources.  Source can be in one of two forms: a filename on the remote host, if the host has already been
              specified, or a string of the form hosts:filename to specify both a host and filename at the same time.  If the latter form is used, the last hostname
              specified becomes the default for future transfers.

     mode transfer-mode
              Set the mode for transfers; transfer-mode may be one of ascii or binary.  The default is ascii.

     put file
     put localfile remotefile
     put file1 file2 ... fileN remote-directory
              Put a file or set of files to the specified remote file or directory.  The destination can be in one of two forms: a filename on the remote host, if the
              host has already been specified, or a string of the form hosts:filename to specify both a host and filename at the same time.  If the latter form is used,
              the hostname specified becomes the default for future transfers.  If the remote-directory form is used, the remote host is assumed to be a UNIX machine.
    
    connect host-name [port]
              Set the host (and optionally port) for transfers.  Note that the TFTP protocol, unlike the FTP protocol, does not maintain connections betwen transfers;
              thus, the connect command does not actually create a connection, but merely remembers what host is to be used for transfers.  You do not have to use the
              connect command; the remote host can be specified as part of the get or put commands.

     get filename
     get remotename localname
     get file1 file2 ... fileN
              Get a file or set of files from the specified sources.  Source can be in one of two forms: a filename on the remote host, if the host has already been
              specified, or a string of the form hosts:filename to specify both a host and filename at the same time.  If the latter form is used, the last hostname
              specified becomes the default for future transfers.

     mode transfer-mode
              Set the mode for transfers; transfer-mode may be one of ascii or binary.  The default is ascii.

     put file
     put localfile remotefile
     put file1 file2 ... fileN remote-directory
              Put a file or set of files to the specified remote file or directory.  The destination can be in one of two forms: a filename on the remote host, if the
              host has already been specified, or a string of the form hosts:filename to specify both a host and filename at the same time.  If the latter form is used,
              the hostname specified becomes the default for future transfers.  If the remote-directory form is used, the remote host is assumed to be a UNIX machine.

     quit     Exit tftp.  An end of file also exits.

     rexmt retransmission-timeout
              Set the per-packet retransmission timeout, in seconds.

     status   Show current status.

     timeout total-transmission-timeout
              Set the total transmission timeout, in seconds.

     trace    Toggle packet tracing.

     verbose  Toggle verbose mode.

BUGS
     Because there is no user-login or validation within the TFTP protocol, the remote site will probably have some sort of file-access restrictions in place.  The exact
     methods are specific to each site and therefore difficult to document here.

HISTORY
     The tftp command appeared in 4.3BSD.

Linux NetKit (0.17)                                                          August 15, 1999                                                          Linux NetKit (0.17)
	"""
	return ''
