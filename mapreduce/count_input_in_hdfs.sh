#!/bin/bash

date > ~/logs/count.log

for file in $(ls ~/lyrics)
do
    echo "$file"
    hadoop fs -count input/$file >> ~/logs/count.log
done