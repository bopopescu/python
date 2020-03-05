import socket

# 创建 socket 对象
s = socket.socket()
# 将 socket 绑定到本机 IP 和端口
s.bind(('localhost', 30000))
# 服务端开始监听来自客户端的连接
s.listen()
# 每当接收到客户端 socket 的请求时，该方法返回对应的 socket 和远程地址
skt, addr = s.accept()
skt.send("服务器的第一行数据".encode('utf-8'))
skt.send("服务器的第二行数据".encode('utf-8'))
# 关闭 socket 的输出，表明输出数据已经结束
skt.shutdown(socket.SHUT_WR)
while True:
    # 从 socket 读取数据
    line = skt.recv(2048).decode('utf-8')
    if line is None or line == '':
        break
    print(line)
skt.close()
s.close()
