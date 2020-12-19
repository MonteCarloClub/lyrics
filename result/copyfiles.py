import os
import shutil

raw = './raw'
useful = './useful'

if not os.path.exists(useful):
    os.mkdir(useful)


for name in os.listdir(raw):

    path = f'{raw}/{name}'
    if not os.path.isdir(path):
        continue
    
    foldername = name
    folderpath = path

    destinationFolder = f'./{useful}/{foldername}'

    if not os.path.exists(destinationFolder):
        os.mkdir(destinationFolder)
        
    for lyrics_rapper in os.listdir(folderpath):

        rapper = lyrics_rapper[7:]
        source = f"{folderpath}/{lyrics_rapper}/part-00000"
        destination = f'{destinationFolder}/{rapper}.txt'

        shutil.copyfile(source, destination)

    print(folderpath)