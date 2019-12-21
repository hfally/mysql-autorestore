colors = {
	'HEADER'	: '\033[95m',
	'OKBLUE'	: '\033[94m',
	'OKGREEN'	: '\033[0;32m',
	'YELLOW'	: '\033[0;33m',
	'FAIL'		: '\033[31m',
	'ENDC'		: '\033[0m',
	'BOLD'		: '\033[1m',
	'UNDERLINE'	: '\033[4m',
	'BGRED'		: '\033[41;37m'
}

# Handle coloration
def colorize(string, color):
	return colors[color.upper()] + string + colors['ENDC']

