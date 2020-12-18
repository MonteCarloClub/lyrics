from creepers.qq import QQ
from tqdm import tqdm
from settings import lyricsFolder
import os

qqmusic = QQ()
# rapper rank top10:
# Eminem TravisScott SnoopDogg Drake JuiceWRLD KendrickLamar PostMalone LilUziVert JCole LilWayne
# rank from https://www.ranker.com/list/most-famous-rappers-right-now/celebrity-lists
rapper = "JuiceWRLD"
start_page = 1
pages_num = 50
songs_per_page = 20

if not os.path.exists(lyricsFolder):
    os.mkdir(lyricsFolder)

LyricFolder = f"{lyricsFolder}/{rapper}"
if not os.path.exists(LyricFolder):
    os.mkdir(LyricFolder)

logFolder = "./log"
if not os.path.exists(logFolder):
    os.mkdir(logFolder)

def log_error(songmid, name):
    """
    log error
    """
    try:
        with open(f'{logFolder}/errors.log', 'a', encoding='utf-8') as f:
            f.write(f'[err] {songmid} {name}' + '\n')
    except:
        pass
    

def parse_to_words(lrcline):
    """
    format lyric to pure words
    eg. 
        [00:30.69]Hit the strip club don&apos;t forget ones get your dick rubbed
        ->  Hit the strip club don't forget ones get your dick rubbed
    """
    lrcline = lrcline.strip()

    if len(lrcline) < 11:
        return ''
    
    if not lrcline[9] == ']':
        return ''

    if lrcline.find(rapper) > -1:
        return ''

    if lrcline.find('Written by') > -1:
        return ''
    
    if lrcline.find('Composed by') > -1:
        return ''
    
    return lrcline[10:].replace('&apos;', "'") + '\n'

def write_to_file(lyric, filename):
    """
    write lyrics to file
    """
    lyric = lyric.strip()
    if not lyric:
        return
    
    if len(lyric) < 100:
        return

    # filename = bytes(filename, 'gbk').decode('utf-8', 'ignore')
    lrcfile = f'{LyricFolder}/{filename}.txt'

    if os.path.exists(lrcfile):
        # return if lyric exists
        return

    # lyric = bytes(lyric, 'gbk').decode('utf-8', 'ignore')

    with open(lrcfile, 'w', encoding='utf-8') as f:
        # lyric string has \n
        lines = lyric.split('\n')
        for line in lines:
            # write to file line by line
            f.write(parse_to_words(line))


async def getLyric():

    count = 0

    for page in range(start_page, start_page + pages_num):
        result = await qqmusic.searchSong(rapper, page, songs_per_page)
        songs = result['songs']
        
        for song in tqdm(songs, desc=f'[({page - start_page:>2}/{pages_num}), {len(songs):>2} songs]', ncols=120):
            songmid = song['idforres']
            name = song['name']
            try:
                lyric = await qqmusic.lyric(songmid)
                write_to_file(lyric, name)
                count += 1
            except:
                log_error(songmid, name)
        
        if len(songs) < songs_per_page:
            break
    
    total = pages_num * songs_per_page
    print(f'success rate is [{count}/{total}]')

if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(getLyric())