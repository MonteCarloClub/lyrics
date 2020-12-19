#!/bin/bash


local_lyrics=(
"lyrics_KendrickLamar"
"lyrics_LilUziVert"
"lyrics_LilWayne"
"lyrics_PostMalone"
"lyrics_SnoopDogg"
"lyrics_TravisScott"
)


for file in ${local_lyrics[*]}
do
    # ls ~/lyrics/$file | wc -l
    # hadoop fs -put ~/lyrics/$file /user/u20210240059/input
    echo "$file" >> ~/logs/test.log
done

