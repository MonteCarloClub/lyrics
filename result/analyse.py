import os
from nltk.corpus import words

def count():
    """
    统计数量
    """

    root = './useful/sorted'
    output = './useful/sorted-filter-strict'

    english_words = words.words()

    print(f'{"rapperfilename":<20} {"wordtypes":>10} {"wordcount":>10} {"digittypes":>10} {"digitcount":>10} {"shittypes":>10} {"shitcount":>10} {"abbrtypes":>10} {"abbrcount":>10} {"conjtypes":>10} {"conjcount":>10} {"wrongtypes":>10} {"wrongcount":>10} {"totalwordcount":>20} {"totalcount":>10} | {"errorlines"}')

    for rapperfilename in os.listdir(root):
        
        totalcount = 0      # 不管对错，单词总数 
        totalwordcount = 0  # 符合限制条件的单词数量

        wordtypes = 0       # 词汇量
        wordcount = 0       # 单词出现的数量

        abbrtypes = 0       # 缩写词的种类
        abbrcount = 0       # 缩写词出现的数量

        conjtypes = 0       # 短语种类
        conjcount = 0       # 短语出现的数量

        digittypes = 0      # 数字种类
        digitcount = 0      # 数字出现的数量

        shittypes = 0       # 垃圾话单词种类
        shitcount = 0       # 垃圾话单词的数量

        wrongtypes = 0      # 拼写错误的种类
        wrongcount = 0      # 拼写错误的数量

        errorlines = 0      # 解析出错的行数

        with open(f'{root}/{rapperfilename}', 'rb') as rapperfile:
            
            outputfile = open(f"{output}/{rapperfilename}", mode="w", encoding="utf-8")

            for b_line in rapperfile.readlines():
                try:
                    line = b_line.decode('gbk')

                    if line.startswith('0'):
                        emmm, num = line.split('\t')
                        word = emmm[7:]

                        # is digit
                        if word.isdigit():
                            digittypes += 1
                            digitcount += int(num)
                            continue
                        
                        # correct english word
                        if word in english_words:
                            wordtypes += 1
                            wordcount += int(num)
                            outputfile.write(f"{word:<30}{num:>10}")

                        # word contains *
                        elif '*' in word:
                            shittypes += 1
                            shitcount += int(num)

                        # word contains '
                        elif "'" in word:
                            abbrtypes += 1
                            abbrcount += int(num)

                        # word contains -
                        elif "-" in word:
                            conjtypes += 1
                            conjcount += int(num)
                        
                        # wrong english words
                        else:
                            wrongtypes += 1
                            wrongcount += int(num)

                    else:
                        totalcount = line.split()[-1]
                        totalcount = int(totalcount)

                except:
                    errorlines += 1

            outputfile.close()

        totalwordcount += wordcount

        print(f'{rapperfilename[:-4]:<20} {wordtypes:>10} {wordcount:>10} {digittypes:>10} {digitcount:>10} {shittypes:>10} {shitcount:>10} {abbrtypes:>10} {abbrcount:>10} {conjtypes:>10} {conjcount:>10} {wrongtypes:>10} {wrongcount:>10} {totalwordcount:>20} {totalcount:>10} | {errorlines}')


def top10percent():
    """
    docstring
    """
    inputroot = './useful/sorted-filter-loose'
    output = './useful/sorted-top10%'

    print(f'{"rapperfilename":<20} {"others":>10} {"top10%":>10}')

    for rapperfilename in os.listdir(inputroot):

        others = 0
        cores = 0

        with open(f'{inputroot}/{rapperfilename}', 'r', encoding='utf-8') as rapperfile:
            
            outputfile = open(f"{output}/{rapperfilename}", mode="w", encoding="utf-8")

            lines = rapperfile.readlines()

            # enheng = int(0.9 * len(lines))
            enheng = int(len(lines) - 200)

            for linenum, line in enumerate(lines):
                word, num = line.split()

                if linenum < enheng:
                    others += int(num)

                else:
                    cores += int(num)
                    outputfile.write(f"{word:<30}{num:>10}\n")

            outputfile.close()
        
        print(f'{rapperfilename[:-4]:<20} {others:>10} {cores:>10}')

if __name__ == "__main__":
    top10percent()