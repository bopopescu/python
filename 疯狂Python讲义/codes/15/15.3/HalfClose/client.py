import socket

# 创建 socket 对象
s = socket.socket()
# 连接远程主机
s.connect(('localhost', 30000))
while True:
    # 从 socket 读取数据
    line = s.recv(2048).decode('utf-8')
    if line is None or line == '':
        break
    print(line)
s.send("客户端的第一行数据".encode('utf-8'))
s.send("客户端的第二行数据".encode('utf-8'))
s.close()
