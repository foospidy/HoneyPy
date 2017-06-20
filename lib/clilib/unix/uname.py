def uname(*params):
	"""
	UNAME(1)                         User Commands                        UNAME(1)

	NAME
		uname - print system information
	
	SYNOPSIS
		uname [OPTION]...
	
	DESCRIPTION
		Print certain system information.  With no OPTION, same as -s.
		
		-a, --all
				print  all  information,  in the following order, except omit -p
				and -i if unknown:
		
		-s, --kernel-name
				print the kernel name
		
		-n, --nodename
				print the network node hostname
		
		-r, --kernel-release
				print the kernel release
		
		-v, --kernel-version
				print the kernel version
		
		-m, --machine
				print the machine hardware name
		
		-p, --processor
				print the processor type or "unknown"
		
		-i, --hardware-platform
				print the hardware platform or "unknown"
		
		-o, --operating-system
				print the operating system
		
		--help display this help and exit
		
		--version
				output version information and exit
	
	AUTHOR
		Written by David MacKenzie.
	
	REPORTING BUGS
		GNU coreutils online help: http://www.gnu.org/software/coreutils/
		Report uname translation bugs to http://translationproject.org/team/
	
	COPYRIGHT
		Copyright @ 2014 Free Software Foundation, Inc.   License  GPLv3+:  GNU
		GPL version 3 or later http://gnu.org/licenses/gpl.html.
		This  is  free  software:  you  are free to change and redistribute it.
		There is NO WARRANTY, to the extent permitted by law.
	"""
	output = 'Linux'
	
	if None != params:
		for param in params:
			if param in ('-a', '--all'):
				output = 'Linux bitminer 3.16.0-4-amd64 #1 SMP Debian 3.16.7-ckt9-3~deb8u1 (2015-04-24) x86_64 GNU/Linux'
	
	return output
