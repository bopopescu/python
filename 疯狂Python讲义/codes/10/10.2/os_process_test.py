import os

# 运行平台上的cmd命令
os.system('cmd')
# 使用Excel打开g:\abc.xls文件
os.startfile('g:\\abc.xls')
os.spawnl(os.P_NOWAIT, 'C:\\Program Files\\Notepad++\\notepad++.exe', ' ')
os.execl('D:\\Python\\Python36\\python.exe', ' ', 'os_test.py', 'i')
