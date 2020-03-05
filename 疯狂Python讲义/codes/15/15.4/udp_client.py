import socket

PORT = 30000
# 定义每个数据报的大小最大为 4KB
DATA_LEN = 4096
DEST_IP = "localhost"
# 通过 type 属性指定创建基于 UDP 协议的 socket
s = socket.socket(type=socket.SOCK_DGRAM)
# 不断地读取键盘输入
while True:
    line = input('')
    if line is None or line == 'exit':
        break
    data = line.encode('utf-8')
    # 发送数据报
    s.sendto(data, (DEST_IP, PORT))
    # 读取 socket 中的数据
    data = s.recv(DATA_LEN)
    print(data.decode('utf-8'))
s.close()
