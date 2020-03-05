from urllib.request import *

# 打开 URL 对应的资源
result = urlopen('http://www.crazyit.org/index.php')
# 按字节读取数据
data = result.read(326)
# 将字节数据恢复成字符串
print(data.decode('utf-8'))

# 用 context manager 来管理打开的 URL 资源
with urlopen('http://www.crazyit.org/index.php') as f:
    # 按字节读取数据
    data = f.read(326)
    # 将字节数据恢复成字符串
    print(data.decode('utf-8'))
