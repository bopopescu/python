import socket, threading, CrazyitDict, CrazyitProtocol

from server_thread import server_target

SERVER_PORT = 30000
# 使用 CrazyitDict 来保存每个客户名字和对应 socket 之间的对应关系
clients = CrazyitDict.CrazyitDict()
# 创建 socket 对象
s = socket.socket()
try:
    # 将 socket 绑定到本机 IP 和端口
    s.bind(('localhost', SERVER_PORT))
    # 服务端开始监听来自客户端的连接
    s.listen()
    # 采用死循环来不断地接收来自客户端的请求
    while True:
        # 每当接收到客户端 socket 的请求时，该方法返回对应的 socket 和远程地址
        c, addr = s.accept()
        threading.Thread(target=server_target, args=(c, clients)).start()
# 如果抛出异常
except:
    print("服务器启动失败，是否端口%d已被占用？" % SERVER_PORT)
