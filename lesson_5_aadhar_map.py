import sys
import string
import logging



def mapper():


    header = sys.stdin.readline()
    for line in sys.stdin:
        data = line.split(',')
        if len(data) != 12:
            continue
        district = data[3]
        aadhar_generated = data[8]
        print "{0}\t{1}".format(district, aadhar_generated)
        

mapper()
