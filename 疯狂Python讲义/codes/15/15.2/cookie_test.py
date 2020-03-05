from urllib.request import *
import http.cookiejar, urllib.parse

# 以指定文件创建 CookieJar 对象，对象将可以把 cookie 保存在文件中
cookie_jar = http.cookiejar.MozillaCookieJar('a.txt')
# 创建 HTTPCookieProcessor 对象
cookie_processor = HTTPCookieProcessor(cookie_jar)
# 创建 OpenerDirector 对象
opener = build_opener(cookie_processor)

# 定义模拟 Chrome 浏览器的 user_agent
user_agent = r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36' \
             r' (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
# 定义请求头
headers = {'User-Agent': user_agent, 'Connection': 'keep-alive'}

# -------------下面代码发送登录的 POST 请求----------------
# 定义登录系统的请求参数
params = {'name': 'crazyit.org', 'pass': 'leegang'}
postdata = urllib.parse.urlencode(params).encode()
# 创建向登录页面发送 POST 请求的 Request
request = Request('http://localhost:8888/test/login.jsp',
                  data=postdata, headers=headers)
# 使用 OpenerDirector 发送 POST 请求
response = opener.open(request)
print(response.read().decode('utf-8'))

# 将 cookie 信息写入磁盘文件
cookie_jar.save(ignore_discard=True, ignore_expires=True)  # ①

# -------------下面代码发送访问被保护资源的 GET 请求----------------
# 创建向"受保护页面"发送 GET 请求的 Request
request = Request('http://localhost:8888/test/secret.jsp',
                  headers=headers)
response = opener.open(request)
print(response.read().decode())
