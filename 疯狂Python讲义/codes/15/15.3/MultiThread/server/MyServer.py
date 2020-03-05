import socket
import threading

# 定义保存所有 socket 的列表
socket_list = []
# 创建 socket 对象
ss = socket.socket()
# 将 socket 绑定到本机 IP 和端口
ss.bind(('localhost', 30000))
# 服务端开始监听来自客户端的连接
ss.listen()


def read_from_client(s):
    try:
        return s.recv(2048).decode('utf-8')
    # 如果捕获到异常，则表明该 socket 对应的客户端已经关闭
    except:
        # 删除该 socket
        socket_list.remove(s);  # ①


def server_target(s):
    try:
        # 采用循环不断地从 socket 中读取客户端发送过来的数据
        while True:
            content = read_from_client(s)
            print(content)
            if content is None:
                break
            for client_s in socket_list:
                client_s.send(content.encode('utf-8'))
    except e:
        print(e.strerror)


while True:
    # 此行代码会阻塞，将一直等待别人的连接
    s, addr = ss.accept()
    socket_list.append(s)
    # 每当客户端连接后启动一个线程为该客户端服务
    threading.Thread(target=server_target, args=(s,)).start()
