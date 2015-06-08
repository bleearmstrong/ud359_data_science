import sys


def reducer():


    max_entries = 0
    max_date = ''
    max_time = ''
    old_key = None
    

    for line in sys.stdin:
        data = line.split('\t')
        if len(data) != 4:
            continue
        this_key, entries, date, time = data
        entries = float(entries)
        time = time[:8]
        if old_key and old_key != this_key:
            print "{0}\t{1} {2}\t{3}".format(old_key, max_date, max_time, max_entries)
            max_entries = 0
            max_date = ''
            max_time = ''
        if entries >= max_entries:
            max_entries = entries
            max_date = date
            max_time = time
        old_key = this_key
    if old_key != None:
            print "{0}\t{1} {2}\t{3}".format(old_key, max_date, max_time, max_entries)


reducer()
