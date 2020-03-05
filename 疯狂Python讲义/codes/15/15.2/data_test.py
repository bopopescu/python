from urllib.request import *

# 向 https://localhost/cgi-bin/test.cgi 发送请求数据
# with urlopen(url='https://localhost/cgi-bin/test.cgi',
with urlopen(url='http://localhost:8888/test/test',  # ①
             data='测试数据'.encode('utf-8')) as f:
    # 读取服务器全部响应
    print(f.read().decode('utf-8'))

import urllib.parse

params = urllib.parse.urlencode({'name': 'fkit', 'password': '123888'})
# 将请求参数添加到 URL 的后面
url = 'http://localhost:8888/test/get.jsp?%s' % params
with urlopen(url=url) as f:
    # 读取服务器全部响应
    print(f.read().decode('utf-8'))

import urllib.parse

params = urllib.parse.urlencode({'name': '疯狂软件', 'password': '123888'})
params = params.encode('utf-8')
# 使用 data 指定请求参数
with urlopen("http://localhost:8888/test/post.jsp", data=params) as f:
    print(f.read().decode('utf-8'))
