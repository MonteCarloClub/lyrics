import os
from settings import lyricsFolder, songsFolder

# list all rappers in lyrics
for rapper in os.listdir(lyricsFolder):
    # create output file according to rapper's name
    with open(f'{songsFolder}/{rapper}.txt', 'w', encoding='utf-8') as rappersongs:
        count = 0
        # list rapper's all lyric files
        for songname in os.listdir(f'{lyricsFolder}/{rapper}'):
            # check size, record if file is not empty
            if os.stat(f'{lyricsFolder}/{rapper}/{songname}').st_size:
                try:
                    # output to file
                    rappersongs.write(songname + '\n')
                    count += 1
                except:
                    print(songname)

        print(count)