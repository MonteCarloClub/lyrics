#!/bin/bash

date > ~/logs/sort.log

for file in $(ls ~/lyrics)
do
    echo "\n\n\n$file" >> ~/logs/sort.log
    mapred streaming -D mapred.job.name="Sort_$file" -file ~/dev/sort/mapper.py -mapper ~/dev/sort/mapper.py -file ~/dev/sort/reducer.py -reducer ~/dev/sort/reducer.py -input output/$file -output sorted/$file
    echo "$file finished"
done
