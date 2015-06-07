import sys
import logging


def reducer():
    

    old_key = None
    aadhar_sum = 0
    for line in sys.stdin:
        data = line.split('\t')
        if len(data) != 2:
            continue
        this_key = data[0]
        if old_key and old_key != this_key:
            print "{0}\t{1}".format(old_key, aadhar_sum)
            aadhar_sum = 0
        aadhar_sum += float(data[1])
        old_key = this_key
    
    print "{0}\t{1}".format(old_key, aadhar_sum)

reducer()
