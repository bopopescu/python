import fileinput

# 使用 with 语句打开文件，该语句会负责关闭文件
with fileinput.input(files=('test.txt', 'info.txt')) as f:
    for line in f:
        print(line, end='')
