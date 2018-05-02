# coding:utf-8
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
date = datetime.now().strftime("%Y%m%d")
class SendMail:
    def send_email(self,report_file):
        sender = "RHCIMS测试"
        receiver = "str"
        smtpserver = "str"
        username = "str"
        password = "str"

        file = open(report_file,"rb")
        mail_body = file.read()
        file.close()

        msg = MIMEText(mail_body, _subtype="html", _charset="utf-8")
        msg["Subject"] = date+u"-自动化测试报告"

        smtp = smtplib.SMTP_SSL("smtp.163.com")
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()
        print("Email has send out !")