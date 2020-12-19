import os
from settings import songsFolder, filterFolder, lyricsFolder

# list all rappers.txt
for rapper_txt in os.listdir(songsFolder):
    # get rapper name
    rapper = rapper_txt[:-4]

    # create destination folder for rapper
    destination = f'{filterFolder}/{rapper}'
    if not os.path.exists(destination):
        os.mkdir(destination)

    with open(f'{songsFolder}/{rapper_txt}', 'r', encoding='utf-8') as songsfile:
        # get content in song name file
        songnames = songsfile.readlines()
        for songname in songnames:
            # del '\n'
            songname = songname[:-1]
            source = f"{lyricsFolder}/{rapper}/{songname}"
            # file not exists
            if not os.path.exists(source):
                print(rapper, songname)
                continue
            # move file
            os.rename(source, f"{destination}/{songname}")