import sys
import string


def mapper():

    def format_key(fog, rain):
        return '{}fog-{}rain'.format(
            '' if fog else 'no',
            '' if rain else 'no'
        )
    header = sys.stdin.readline()
    for line in sys.stdin:
    	data = line.split(',')
        if len(data) != 22:
            continue
        fog = data[14]
        rain = data[15]
        entries = data[6]
        key = format_key(float(fog), float(rain))
        print "{0}\t{1}".format(key, entries)

mapper()
