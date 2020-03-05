import poplib, os.path, mimetypes
from email.parser import BytesParser, Parser
from email.policy import default

# 输入邮件地址, 口令和 POP3 服务器地址:
email = 'kongyeeku@qq.com'
password = '123456'
pop3_server = 'pop.qq.com'

# 连接到 POP3 服务器:
# conn = poplib.POP3(pop3_server, 110)
conn = poplib.POP3_SSL(pop3_server, 995)
# 可以打开或关闭调试信息:
conn.set_debuglevel(1)
# 可选 : 打印 POP3 服务器的欢迎文字:
print(conn.getwelcome().decode('utf-8'))
# 输入用户名、密码信息
# 相当于发送 POP3 的 user 命令
conn.user(email)
# 相当于发送 POP3 的 pass 命令
conn.pass_(password)
# 获取邮件统计信息，相当于发送 POP3 的 stat 命令
message_num, total_size = conn.stat()
print('邮件数: %s. 总大小: %s' % (message_num, total_size))
# 获取服务器上的邮件列表，相当于发送 POP3 的 list 命令
# resp 保存服务器的响应码
# mails 列表保存每封邮件的编号、大小
resp, mails, octets = conn.list()
print(resp, mails)
# 获取指定邮件的内容（此处传入总长度，也就是获取最后一封邮件）
# 相当于发送 POP3 的 retr 命令
# resp 保存服务器的响应码
# data 保存该邮件的内容
resp, data, octets = conn.retr(len(mails))
# 将 data 的所有数据（原本是一个字节列表）拼接在一起
msg_data = b'\r\n'.join(data)
# 将字符串内容解析成邮件，此处一定要指定 policy=default
msg = BytesParser(policy=default).parsebytes(msg_data)  # ①
print(type(msg))
print('发件人:' + msg['from'])
print('收件人:' + msg['to'])
print('主题:' + msg['subject'])
print('第一个收件人名字:' + msg['to'].addresses[0].username)
print('第一个发件人名字:' + msg['from'].addresses[0].username)
for part in msg.walk():
    counter = 1
    # 如果 maintype 是 multipart，说明是容器（用于包含正文、附件等）
    if part.get_content_maintype() == 'multipart':
        continue
    # 如果 maintype 是 text，说明是邮件正文部分
    elif part.get_content_maintype() == 'text':
        print(part.get_content())
    # 处理附件
    else:
        # 获取附件的文件名
        filename = part.get_filename()
        # 如果没有文件名，程序要负责为附件生成文件名
        if not filename:
            # 根据附件的 contnet_type 来推测它的后缀名
            ext = mimetypes.guess_extension(part.get_content_type())
            # 如果推测不出后缀名
            if not ext:
                # 使用 .bin 作为后缀名
                ext = '.bin'
            # 程序为附件来生成文件名
            filename = 'part-%03d%s' % (counter, ext)
        counter += 1
        # 将附件写入的本地文件
        with open(os.path.join('.', filename), 'wb') as fp:
            fp.write(part.get_payload(decode=True))
# 退出服务器，相当于发送 POP3 的 quit 命令
conn.quit()
