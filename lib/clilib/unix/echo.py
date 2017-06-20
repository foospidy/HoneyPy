def echo(*params):
	"""
	ECHO(1)                                                                    User Commands                                                                    ECHO(1)

NAME
       echo - display a line of text

SYNOPSIS
       echo [SHORT-OPTION]... [STRING]...
       echo LONG-OPTION

DESCRIPTION
       Echo the STRING(s) to standard output.

       -n     do not output the trailing newline

       -e     enable interpretation of backslash escapes

       -E     disable interpretation of backslash escapes (default)

       --help display this help and exit

       --version
              output version information and exit

       If -e is in effect, the following sequences are recognized:

       \\     backslash

       \a     alert (BEL)

       \b     backspace

       \c     produce no further output

       \e     escape

       \f     form feed

       \n     new line

       \r     carriage return

       \t     horizontal tab
	   
	    \v     vertical tab

       \0NNN  byte with octal value NNN (1 to 3 digits)

       \\xHH   byte with hexadecimal value HH (1 to 2 digits)

       NOTE:  your  shell  may  have  its own version of echo, which usually supersedes the version described here.  Please refer to your shell's documentation for
       details about the options it supports.

AUTHOR
       Written by Brian Fox and Chet Ramey.

REPORTING BUGS
       GNU coreutils online help: <http://www.gnu.org/software/coreutils/>
       Report echo translation bugs to <http://translationproject.org/team/>

COPYRIGHT
       Copyright @ 2014 Free Software Foundation, Inc.  License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>.
       This is free software: you are free to change and redistribute it.  There is NO WARRANTY, to the extent permitted by law.

SEE ALSO
       Full documentation at: <http://www.gnu.org/software/coreutils/echo>
       or available locally via: info '(coreutils) echo invocation'

GNU coreutils 8.23                                                           March 2015                                                                     ECHO(1)
	"""
	
	output = ''
	escape = False
	
	if None != params:
         for param in params:
			if param in {'-e'}:
				escape = True
			else:
				# remove quotes if quoted
				if param.startswith('"') and param.endswith('"'):
					param = param[1:-1]
				
				if param.startswith("'") and param.endswith("'"):
					param = param[1:-1]
				
				if escape:
					output = output + str(param).decode('string_escape')
				else:
					output = output + str(param)

	return output
