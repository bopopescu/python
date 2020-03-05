from urllib.parse import *

# 解析 URL 字符串
result = urlparse('http://www.crazyit.org:80/index.php;yeeku?name=fkit#frag')
print(result)
# 通过属性名和索引来获取 URL 的各部分
print('scheme:', result.scheme, result[0])
print('主机和端口:', result.netloc, result[1])
print('主机:', result.hostname)
print('端口:', result.port)
print('资源路径:', result.path, result[2])
print('参数:', result.params, result[3])
print('查询字符串:', result.query, result[4])
print('fragment:', result.fragment, result[5])
print(result.geturl())
print('-----------------')
result = urlunparse(('http', 'www.crazyit.org:80', 'index.php',
                     'yeeku', 'name=fkit', 'frag'))
print('URL为:', result)
print('-----------------')
# 解析以 // 开头的 URL
result = urlparse('//www.crazyit.org:80/index.php')
print('scheme:', result.scheme, result[0])
print('主机和端口:', result.netloc, result[1])
print('资源路径:', result.path, result[2])
print('-----------------')
# 解析没有 scheme，也没有以双斜线（//）开头的URL
# 从开头部分开始就会被当成资源路径
result = urlparse('www.crazyit.org/index.php')
print('scheme:', result.scheme, result[0])
print('主机和端口:', result.netloc, result[1])
print('资源路径:', result.path, result[2])

# 解析查询字符串，返回 dict
result = parse_qs('name=fkit&name=%E7%96%AF%E7%8B%82java&age=12')
print(result)
# 解析查询字符串，返回 list
result = parse_qsl('name=fkit&name=%E7%96%AF%E7%8B%82java&age=12')
print(result)
# 将列表格式的请求参数恢复成请求参数字符串
print(urlencode(result))

# 被拼接 URL 不以斜线开头
result = urljoin('http://www.crazyit.org/users/login.html', 'help.html')
print(result)  # http://www.crazyit.org/users/help.html
result = urljoin('http://www.crazyit.org/users/login.html', 'book/list.html')
print(result)  # http://www.crazyit.org/users/book/list.html
# 被拼接 URL 以斜线（代表根路径 path）开头
result = urljoin('http://www.crazyit.org/users/login.html', '/help.html')
print(result)  # http://www.crazyit.org/help.html
# 被拼接 URL 以双斜线（代表绝对 URL）开头
result = urljoin('http://www.crazyit.org/users/login.html', '//help.html')
print(result)  # http://help.html
