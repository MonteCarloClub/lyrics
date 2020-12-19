import os
import enchant

'''
    rapper                   top200       rest      total
    -----------------------------------------------------
    Drake                    201524      91433     292957
    Eminem                    31294      17130      48424
    JCole                    104683      52241     156924
    JuiceWRLD                 41581      19471      61052
    KendrickLamar            131783      71553     203336
    LilUziVert                93532      43460     136992
    LilWayne                 264488     143022     407510
    PostMalone                41285      16908      58193
    SnoopDogg                176559      92868     269427
    TravisScott               66580      34964     101544
'''

root = './useful/sorted'
output = './analysis'

english_words = enchant.Dict("en_US")

for rapperfilename in os.listdir(root):
    
    totalcount = 0
    wordtypes = 0   # 词汇量
    wordcount = 0   # 单词出现的数量
    digitcount = 0  # 数字出现的数量
    wrongcount = 0  # 拼写错误的数量

    errorlines = 0  # 解析出错的行数

    with open(f'{root}/{rapperfilename}', 'r', encoding='gbk') as rapperfile:

        line = rapperfile.readline()

        while line.startswith('0'):
                try:
                        emmm, num = line.split('\t')
                        word = emmm[7:]

                        # is digit
                        if word.isdigit():
                            digitcount += int(num)
                            continue
                        
                        # correct english word
                        if english_words.check(word):
                            wordtypes += 1
                            wordcount += int(num)
                        
                        # wrong english words
                        else:
                            wrongcount += int(num)


        except:
            errorlines += 1

                    else:
                        totalcount = line.split()[-1]
                        totalcount = int(totalcount)



    print(f'{rapperfilename[:-4]:<20} {wordtypes:>10} {wordcount:>10} {digitcount:>10} {wrongcount:>10} {totalcount:>10}  --- [err] {errorlines}')
