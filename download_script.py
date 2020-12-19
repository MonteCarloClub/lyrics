import os
import time
from subprocess import Popen, PIPE

def download_rappers(rappers):

    running_procs = [Popen(args=f'python ./rapper_lyrics_from_qq.py {rapper}', shell=True, encoding='utf-8') for rapper in rappers]

    while running_procs:
        for proc in running_procs:
            retcode = proc.poll()
            if retcode is not None: # Process finished.
                running_procs.remove(proc)
                break
            else: # No process is done, wait a bit and check again.
                time.sleep(.1)
                continue

    print('finish')
    

if __name__ == "__main__":
    # rapper rank top10:
    # Eminem TravisScott SnoopDogg Drake JuiceWRLD KendrickLamar PostMalone LilUziVert JCole LilWayne
    # rank from https://www.ranker.com/list/most-famous-rappers-right-now/celebrity-lists
    rank = [
        'Eminem', 
        'TravisScott', 
        'SnoopDogg', 
        'Drake', 
        'JuiceWRLD', 
        'KendrickLamar', 
        'PostMalone', 
        'LilUziVert', 
        'JCole', 
        'LilWayne'
    ]

    download_rappers(rank[:2])
    # download_rappers(rank[5:])