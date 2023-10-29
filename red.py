#!/usr/bin/env python

from operator import itemgetter
import sys

total_sum = 0
total_count = 0

for line in sys.stdin:
    line = line.strip()
    value, count_str = line.split('\t')
    count = int(count_str)

    total_sum += float(value) * count
    total_count += count

# Calculate the final average
if total_count > 0:
    average = total_sum / total_count
    print 'AVERAGE=%.2f' % (average)
