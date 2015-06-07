import sys

def reducer():


    riders = 0      # The number of total riders for this key
    num_hours = 0   # The number of hours with this key
    old_key = None
    average = 0

    for line in sys.stdin:
        data = line.split('\t')
        if len(data) != 2:
            continue
        this_key, entries = data
        if old_key and old_key != this_key:
            average = float(riders)/num_hours
            print "{0}\t{1}".format(old_key, average)
            riders = 0
            num_hours = 0
        riders += float(entries)
        num_hours += 1
        old_key = this_key
    if old_key != None:
        average = float(riders)/num_hours
        print "{0}\t{1}".format(old_key, average)
        
        

reducer()
