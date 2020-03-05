from urllib.request import *
import http.cookiejar, urllib.parse

# 以指定文件创建 CookieJar 对象，对象将可以把 cookie 保存在文件中
cookie_jar = http.cookiejar.MozillaCookieJar('a.txt')
# 直接加载 a.txt 中的 Cookie 信息
cookie_jar.load('a.txt', ignore_discard=True, ignore_expires=True)
# 遍历 a.txt 中保存的 cookie 信息
for item in cookie_jar:
    print('Name =' + item.name)
    print('Value =' + item.value)
# 创建 HTTPCookieProcessor 对象
cookie_processor = HTTPCookieProcessor(cookie_jar)
# 创建 OpenerDirector 对象
opener = build_opener(cookie_processor)

# 定义模拟 Chrome 浏览器的 user_agent
user_agent = r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36' \
             r' (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
# 定义请求头
headers = {'User-Agent': user_agent, 'Connection': 'keep-alive'}

# -------------下面代码发送访问被保护资源的 GET 请求----------------
# 创建向"受保护页面"发送GET请求的Request
request = Request('http://localhost:8888/test/secret.jsp',
                  headers=headers)
response = opener.open(request)
print(response.read().decode())
