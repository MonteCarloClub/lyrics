#!/bin/bash


for file in $(ls ~/lyrics)
do
    hadoop fs -get output/$file outputs
    echo "[succ] $file is inside outputs/"
done
