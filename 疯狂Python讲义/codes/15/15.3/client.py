# 导入socket模块
import socket

# 创建 socket 对象
s = socket.socket()
# 连接远程主机
s.connect(('localhost', 30000))  # ①
print('--%s--' % s.recv(1024).decode('utf-8'))
s.close()
