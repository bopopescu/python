import os

f = open('y.txt', 'wb+')
# os.linesep 代表当前操作系统上的换行符
f.write(('我爱Python' + os.linesep).encode('utf-8'))
f.writelines((('土门壁甚坚，' + os.linesep).encode('utf-8'),
              ('杏园度亦难。' + os.linesep).encode('utf-8'),
              ('势异邺城下，' + os.linesep).encode('utf-8'),
              ('纵死时犹宽。' + os.linesep).encode('utf-8')))
