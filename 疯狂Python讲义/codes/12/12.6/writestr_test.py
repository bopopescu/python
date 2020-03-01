import os

f = open('x.txt', 'w+')
# os.linesep 代表当前操作系统上的换行符
f.write('我爱Python' + os.linesep)
f.writelines(('土门壁甚坚，' + os.linesep,
              '杏园度亦难。' + os.linesep,
              '势异邺城下，' + os.linesep,
              '纵死时犹宽。' + os.linesep))
