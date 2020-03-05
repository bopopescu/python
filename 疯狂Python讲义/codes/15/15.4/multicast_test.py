import time, socket, threading, os

# 定义本机 IP 地址
SENDERIP = 'localhost'
# 定义本地端口
SENDERPORT = 30000
# 定义本程序的多点广播 IP 地址
MYGROUP = '230.0.0.1'
# 通过 type 属性指定创建基于 UDP 协议的 socket
s = socket.socket(type=socket.SOCK_DGRAM)
# 将该 socket 绑定到 0.0.0.0 的虚拟 IP
s.bind(('0.0.0.0', SENDERPORT))  # ①
# 设置广播消息的 TTL（Time-To-Live）
s.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 64)
# 设置允许多点广播使用相同的端口
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# 将 socket 进入广播组
status = s.setsockopt(socket.IPPROTO_IP,
                      socket.IP_ADD_MEMBERSHIP,
                      socket.inet_aton(MYGROUP) + socket.inet_aton(SENDERIP))


# 定义从 socket 读取数据的方法
def read_socket(sock):
    while True:
        data = sock.recv(2048)
        print("信息: ", data.decode('utf-8'))


# 以 read_socket 作为 target 启动多线程
threading.Thread(target=read_socket, args=(s,)).start()
# 采用循环不断读取键盘输入，并输出到 socket 中
while True:
    line = input('')
    if line is None or line == 'exit':
        break
        os._exit(0)
    # 将 line 输出到 socket 中
    s.sendto(line.encode('utf-8'), (MYGROUP, SENDERPORT))
