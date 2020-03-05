import CrazyitProtocol


def server_target(s, clients):
    try:
        while True:
            # 从 socket 读取数据
            line = s.recv(2048).decode('utf-8')
            print(line)
            # 如果读到的行以 CrazyitProtocol.USER_ROUND 开始，并以其结束
            # 则可以确定读到的是用户登录的用户名
            if line.startswith(CrazyitProtocol.USER_ROUND) \
                    and line.endswith(CrazyitProtocol.USER_ROUND):
                # 得到真实消息
                user_name = line[CrazyitProtocol.PROTOCOL_LEN: \
                                 -CrazyitProtocol.PROTOCOL_LEN]
                # 如果用户名重复
                if user_name in clients:
                    print("重复")
                    s.send(CrazyitProtocol.NAME_REP.encode('utf-8'))
                else:
                    print("成功")
                    s.send(CrazyitProtocol.LOGIN_SUCCESS.encode('utf-8'))
                    clients[user_name] = s
            # 如果读到的行以 CrazyitProtocol.PRIVATE_ROUND 开始，并以其结束
            # 则可以确定是私聊信息，私聊信息只向特定的 socket 发送
            elif line.startswith(CrazyitProtocol.PRIVATE_ROUND) \
                    and line.endswith(CrazyitProtocol.PRIVATE_ROUND):
                # 得到真实消息
                user_and_msg = line[CrazyitProtocol.PROTOCOL_LEN: \
                                    -CrazyitProtocol.PROTOCOL_LEN]
                # 以 SPLIT_SIGN 分割字符串，前半是私聊用户，后半是聊天信息
                user = user_and_msg.split(CrazyitProtocol.SPLIT_SIGN)[0]
                msg = user_and_msg.split(CrazyitProtocol.SPLIT_SIGN)[1]
                # 获取私聊用户对应的 socket，并发送私聊信息
                clients[user].send((clients.key_from_value(s) \
                                    + "悄悄地对你说：" + msg).encode('utf-8'))
            # 公聊要向每个 socket 发送
            else:
                # 得到真实消息
                msg = line[CrazyitProtocol.PROTOCOL_LEN: \
                           -CrazyitProtocol.PROTOCOL_LEN]
                # 遍历 clients 中的每个 socket
                for client_socket in clients.values():
                    client_socket.send((clients.key_from_value(s) \
                                        + "说：" + msg).encode('utf-8'))
    # 捕获到异常后，表明该 socket 对应的客户端已经出现了问题
    # 所以程序将其对应的 socket 从 dict 中删除
    except:
        clients.remove_by_value(s)
        print(len(clients))
        # 关闭网络、IO资源
        if s is not None:
            s.close()
