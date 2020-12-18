import os

prefix = 'lyrics_'

for name in os.listdir('.'):
    # list folders in current dir
    if os.path.isdir(os.path.join(f'./{name}')) and name.startswith(prefix):
        # if folder'name start with 'lyrics_'
        # get artist's name
        artist = name[len(prefix):]

        # create output file according to artist's name
        with open(f'./songs_{artist}.txt', 'w') as f:
            count = 0
            for filename in os.listdir(f'./{name}'):
                # check size, record if file is not empty
                if os.stat(f'./{name}/{filename}').st_size:
                    try:
                        # convert lyric file's name to utf-8
                        filename = bytes(filename, 'gbk').decode('utf-8', 'ignore')
                        # output to file
                        f.write(filename + '\n')
                        count += 1
                    except:
                        print(filename)
            
            print(count)