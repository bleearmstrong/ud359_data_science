import sys


def reducer():

    old_key = None
    unit_total = 0
    for line in sys.stdin:
        this_key, entries = line.split('\t')
        if old_key and old_key != this_key:
            print "{0}\t{1}".format(old_key, unit_total)
            unit_total = 0
        old_key = this_key
        unit_total += float(entries)
    if old_key != None:
        print "{0}\t{1}".format(old_key, unit_total)

        
reducer()
