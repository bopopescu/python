import smtplib
from email.message import EmailMessage

# 定义 SMTP 服务器地址:
smtp_server = 'smtp.qq.com'
# 定义发件人地址
from_addr = 'kongyeeku@qq.com'
# 定义登录邮箱的密码
password = '12345678'
# 定义收件人地址:
to_addr = 'kongyeeku@163.com'

# 创建 SMTP 连接
# conn = smtplib.SMTP(smtp_server, 25)
conn = smtplib.SMTP_SSL(smtp_server, 465)
conn.set_debuglevel(1)
conn.login(from_addr, password)  # ①
# 创建邮件对象
msg = EmailMessage()
# 设置邮件内容
msg.set_content('您好，这是一封来自 Python 的邮件', 'plain', 'utf-8')
# 发送邮件
conn.sendmail(from_addr, [to_addr], msg.as_string())
# 退出连接
conn.quit()
