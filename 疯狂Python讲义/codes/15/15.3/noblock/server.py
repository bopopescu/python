import selectors, socket

# 创建默认的 selectors 对象
sel = selectors.DefaultSelector()


# 负责监听“有数据可读”事件的函数
def read(skt, mask):
    try:
        # 读取数据
        data = skt.recv(1024)
        if data:
            # 将读取的数据采用循环向每个 socket 发送一次
            for s in socket_list:
                s.send(data)  # Hope it won't block
        else:
            # 如果该 socket 已被对方关闭，关闭该 socket，
            # 并从 socket_list 列表中删除
            print('关闭', skt)
            sel.unregister(skt)
            skt.close()
            socket_list.remove(skt)
    # 如果捕捉到异常, 将该 socket 关闭，并从 socket_list 列表中删除
    except:
        print('关闭', skt)
        sel.unregister(skt)
        skt.close()
        socket_list.remove(skt)


socket_list = []


# 负责监听“客户端连接进来”事件的函数
def accept(sock, mask):
    conn, addr = sock.accept()
    # 使用 socket_list 保存代表客户端的 socket
    socket_list.append(conn)
    conn.setblocking(False)
    # 使用 sel 为 conn 的 EVENT_READ 事件注册 read 监听函数
    sel.register(conn, selectors.EVENT_READ, read)  # ②


sock = socket.socket()
sock.bind(('localhost', 30000))
sock.listen()
# 设置该 socket 是非阻塞的
sock.setblocking(False)
# 使用 sel 为 sock 的 EVENT_READ 事件注册 accept 监听函数
sel.register(sock, selectors.EVENT_READ, accept)  # ①
# 采用死循环不断提取 sel 的事件
while True:
    events = sel.select()
    for key, mask in events:
        # key 的 data 属性获取为该事件注册的监听函数
        callback = key.data
        # 调用监听函数, key 的 fileobj 属性获取被监听的 socket 对象
        callback(key.fileobj, mask)
