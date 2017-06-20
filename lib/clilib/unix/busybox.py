def busybox(*params):
	"""
No manual entry for busybox
	"""

	output = ''

	if None != params:
		for param in params:

			#https://isc.sans.edu/diary/21543
			if 'ECCHI' == param:
				output = 'ECCHI: applet not found'

	return output
