import sys
import string


def mapper():
    
    header = sys.stdin.readline()
    for line in sys.stdin:
        data = line.split(',')
        if len(data) != 22:
            continue
        unit = data[1]
        entries = data[6]
        date = data[2]
        time = data[3]
        
        print "{0}\t{1}\t{2}\t{3}".format(unit, entries, date, time)

mapper()
