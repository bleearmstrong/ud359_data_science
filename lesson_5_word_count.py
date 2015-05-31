import logging
import sys
import string
import re

from util import logfile

logging.basicConfig(filename=logfile, format='%(message)s',
                   level=logging.INFO, filemode='w')


def word_count():


    word_counts = {}

    for line in sys.stdin:
        data = line.strip().split(" ")
        
        for word in data:
            word = re.sub(r'[^\w\s]', '', word).lower()
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
    print word_counts

word_count()
