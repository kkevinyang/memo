# encoding: utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from email.mime.image import MIMEImage
from email.header import Header
from email import encoders
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
import mimetypes


def send_mail(
        sender,
        recipients,
        subject,
        html_content,
        attachments=None,
        username=None,
        password=None,
        mail_host='xx.xx.xx.xx',
        mail_port=25,
        ssl=False,
):
    """
    发送邮件
    :param sender: 发件人
    :param recipients: 收件人列表
    :param subject: 邮件主题
    :param html_content: 邮件正文内容
    :param attachments: 附件列表, 为文件目录
    :param username: 如果需要登录, 则为登录用户名
    :param password: 登录用户密码
    :param mail_host: 邮件服务器host
    :param mail_port: 邮件服务器端口
    :param ssl: 是否使用ssl方式登录
    """
    # 构造邮件
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    msg['Subject'] = Header(subject, 'utf-8')
    msg_text = MIMEText(html_content, 'html', 'utf-8')
    msg.attach(msg_text)
    # 添加附件
    if not attachments:
        attachments = []
    for path in attachments:
        filename = os.path.basename(path)
        if not os.path.isfile(path) or filename.startswith('.'):
            continue
        ctype, encoding = mimetypes.guess_type(path)
        if ctype is None or encoding is not None:
            ctype = 'application/octet-stream'
        maintype, subtype = ctype.split('/', 1)
        if maintype == 'text':
            fp = open(path)
            att = MIMEText(fp.read(), _subtype=subtype)
            fp.close()
        elif maintype == 'image':
            fp = open(path, 'rb')
            att = MIMEImage(fp.read(), _subtype=subtype)
            fp.close()
        elif maintype == 'audio':
            fp = open(path, 'rb')
            att = MIMEAudio(fp.read(), _subtype=subtype)
            fp.close()
        else:
            fp = open(path, 'rb')
            att = MIMEBase(maintype, subtype)
            att.set_payload(fp.read())
            fp.close()
            encoders.encode_base64(att)
        att.add_header('Content-Disposition', 'attachment', filename=filename)
        msg.attach(att)
    # 发送邮件
    server = smtplib.SMTP(mail_host, mail_port) if not ssl else smtplib.SMTP_SSL(mail_host, mail_port)
    if username:
        server.login(username, password)
    server.sendmail(sender, recipients, msg.as_string())


def example_1():
    sender = '<your_eamil@qq.com>'
    recipients = ['<resevive@qq.com>']
    subject = '测试邮件'
    html_content = '<h1>测试邮件</h1><p>这是一个测试邮件</p>'
    attachments = ['Screen_1.png', 'aaa.txt']
    host = 'xx'
    port = 25
    send_mail(sender, recipients, subject, html_content, attachments, mail_host=host, mail_port=port)


def example_qq():
    host = 'smtp.qq.com'
    port = 465
    sender = username = '888888888@qq.com'
    recipients = ['qqwqww@qq.com']
    subject = '测试邮件'
    html_content = '<h1>测试邮件</h1><p>这是一个测试邮件</p>'
    attachments = ['att-test/Screen_1.png', 'att-test/aaa.txt']
    password = '111111111'
    send_mail(sender, recipients, subject, html_content, attachments, username, password, host, port, True)