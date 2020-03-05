import socket

PORT = 30000
# 定义每个数据报的大小最大为 4KB
DATA_LEN = 4096
# 定义一个字符串数组，服务器端发送该数组的元素
books = ("疯狂 Python 讲义",
         "疯狂 Kotlin 讲义",
         "疯狂 Android 讲义",
         "疯狂 Swift 讲义")
# 通过 type 属性指定创建基于 UDP 协议的 socket
s = socket.socket(type=socket.SOCK_DGRAM)
# 将该 socket 绑定到本机的指定 IP 和端口
s.bind(('localhost', PORT))
# 采用循环接收数据
for i in range(1000):
    # 读取 s 中的数据的数据的发送地址
    data, addr = s.recvfrom(DATA_LEN)
    # 将接收到的内容转换成字符串后输出
    print(data.decode('utf-8'))
    # 从字符串数组中取出一个元素作为发送数据
    send_data = books[i % 4].encode('utf-8')
    # 将数据报发送给 addr 地址
    s.sendto(send_data, addr)
s.close()
