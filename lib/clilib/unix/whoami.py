def whoami(user, *params):
	"""
WHOAMI(1)                                        User Commands                                       WHOAMI(1)

NAME
       whoami - print effective userid

SYNOPSIS
       whoami [OPTION]...

DESCRIPTION
       Print the user name associated with the current effective user ID.  Same as id -un.

       --help display this help and exit

       --version
              output version information and exit

AUTHOR
       Written by Richard Mlynarik.

REPORTING BUGS
       GNU coreutils online help: <http://www.gnu.org/software/coreutils/>
       Report whoami translation bugs to <http://translationproject.org/team/>

COPYRIGHT
       Copyright  @  2014  Free  Software  Foundation,  Inc.   License  GPLv3+:  GNU  GPL  version  3 or later
       <http://gnu.org/licenses/gpl.html>.
       This is free software: you are free to change and redistribute it.  There is NO WARRANTY, to the extent
       permitted by law.

SEE ALSO
       Full documentation at: <http://www.gnu.org/software/coreutils/whoami>
       or available locally via: info '(coreutils) whoami invocation'

GNU coreutils 8.23                                March 2015                                         WHOAMI(1)
	"""
	
	output = str(user)
	
	if None != params:
         for param in params:
			if param in ('--help'):
				output = "Usage: whoami [OPTION]...\nPrint the user name associated with the current effective user ID.\nSame as id -un.\n\n      --help     display this help and exit\n      --version  output version information and exit\n\nGNU coreutils online help: <http://www.gnu.org/software/coreutils/>\nFull documentation at: <http://www.gnu.org/software/coreutils/whoami>\nor available locally via: info '(coreutils) whoami invocation'"
			elif param in ('--version'):
				output = 'whoami (GNU coreutils) 8.23\nCopyright (C) 2014 Free Software Foundation, Inc.\nLicense GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>.\nThis is free software: you are free to change and redistribute it.\nThere is NO WARRANTY, to the extent permitted by law.\n\nWritten by Richard Mlynarik.'

	return output
