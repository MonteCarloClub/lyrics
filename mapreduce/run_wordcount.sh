#!/bin/bash

date > ~/logs/wordcount.log


for file in $(ls ~/lyrics)
do
    echo "\n\n\n$file" >> ~/logs/wordcount.log
    mapred streaming -D mapred.job.name="Count_$file" -file ~/dev/wordcount/mapper.py -mapper ~/dev/wordcount/mapper.py -file ~/dev/wordcount/reducer.py -reducer ~/dev/wordcount/reducer.py -input input/$file -output output/$file
    echo "$file finished"
done
