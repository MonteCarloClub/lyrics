#!/bin/bash

date > ~/logs/count.log

for file in $(ls ~/lyrics)
do
    echo "$file"
    # ls ~/lyrics/$file | wc -l >> ~/logs/count.log
    hadoop fs -count output/$file >> ~/logs/count.log
done