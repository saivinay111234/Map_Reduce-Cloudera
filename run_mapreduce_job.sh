#!/bin/bash
/usr/bin/hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
-files map.py,red.py \
-input /mapreduce/test1.txt \
-output /mapreduce/output02 \
-mapper map.py \
-reducer red.py 

