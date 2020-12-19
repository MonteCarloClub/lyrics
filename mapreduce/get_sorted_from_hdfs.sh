#!/bin/bash


for file in $(ls ~/lyrics)
do
    hadoop fs -get sorted/$file sort
    echo "[succ] $file is inside sort/"
done
