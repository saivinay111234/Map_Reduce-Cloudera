#!/usr/bin/env python

import sys
import re

# Regular expression to match numeric values
numeric_pattern = re.compile(r'[-+]?\d*\.\d+|[-+]?\d+')

for line in sys.stdin:
    line = line.strip()
    values = re.findall(numeric_pattern, line)
    
    for value in values:
        # Output the value as a float and '1' to count it
        print '%s\t%s' % (value, 1)