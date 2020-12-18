import os

prefix = 'lyrics_'

for name in os.listdir('.'):
    # list folders in current dir
    if os.path.isdir(os.path.join(f'./{name}')) and name.startswith(prefix):
        # if folder'name start with 'lyrics_'
        # get artist's name
        artist = name[len(prefix):]

        # create output file according to artist's name
        with open(f'./filter_{artist}.txt', 'w') as f:
            count = 0
            for filename in os.listdir(f'./{name}'):
                # get lyric file's name
                try:
                    # output to file
                    f.write(filename + '\n')
                    count += 1
                except:
                    pass
            
            print(count)