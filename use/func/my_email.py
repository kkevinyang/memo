# -*- coding:UTF8 -*-
from email.mime.text import MIMEText
import smtplib


def sendmail(subject, content):
    _user = "ZZZZZZZ@qq.com"
    _pwd = "XXXXXXXX"
    _to = "GGGGGG@QQQQQQ.com"

    # 使用MIMEText构造符合smtp协议的header及body
    msg = MIMEText(content)
    msg["Subject"] = subject
    msg["From"] = _user
    msg["To"] = _to

    s = smtplib.SMTP("smtp.qq.com", timeout=30)
    s.login(_user, _pwd)  # 登陆服务器
    s.sendmail(_user, _to, msg.as_string())
    s.close()
