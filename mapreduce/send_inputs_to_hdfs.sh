#!/bin/bash


for file in $(ls ~/lyrics)
do
    hadoop fs -put ~/lyrics/$file input
    echo "$file finished"
done
