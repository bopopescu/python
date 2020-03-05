# 导入 socket 模块
import socket

# 创建 socket 对象
s = socket.socket()
# 将 socket 绑定到本机 IP 和端口
s.bind(('localhost', 30000))
# 服务端开始监听来自客户端的连接
s.listen()
while True:
    # 每当接收到客户端 socket 的请求时，该方法返回对应的 socket 和远程地址
    c, addr = s.accept()
    print(c)
    print('连接地址：', addr)
    c.send('您好，您收到了服务器的新年祝福！'.encode('utf-8'))
    # 关闭连接
    c.close()
