# -*- coding: utf-8 -*-

import sys
import json

Pronouns = ["han", "hon", "den", "det", "denna", "denne", "hen"]

# input comes from STDIN (standard input)
for line in sys.stdin:
    
    if line == '\n':
        continue
    
    line = json.loads(line)
    
    if line["retweeted"] != False:
        continue
    
    words = line["text"].split()
    for word in words:
        word = word.lower()
        if word in Pronouns:
            print('%s\t%s' % (word, 1))
    
    print('total\t%s' % (1))