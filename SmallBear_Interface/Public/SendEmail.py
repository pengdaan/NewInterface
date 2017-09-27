# -*- coding: utf-8 -*-
__author__ = 'leo'
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import yaml
import time,smtplib,os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_file=parentdir+'\Config\email.yaml'
def load_email_setting():
    # 获取邮件的配置信息
    ConfigData = open(data_file,'rb')
    for data in yaml.load_all(ConfigData):
        Data=data
        yaml.safe_dump(Data) #转换成字典
        Foremail=(Data.get('foremail'))
        Pwd=(Data.get('password'))
        Toeamil=(Data.get('toeamil'))
        #print(Toeamil)
        Title=(Data.get('title'))
        return (Foremail,Pwd,Toeamil,Title)

def send_email(filepath):
    from_addr,password,mail_to,mail_body=load_email_setting()
    msg = MIMEMultipart()
    msg['Subject'] = '小树熊电商接口自动化测试报告'
    msg['From'] ='项目质量测试管理部'
    # 发送单个邮件
    # msg['To'] = mail_to
    # 发送整个list
    msg['To'] =",".join(mail_to)
    msg['Date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
    #att = MIMEText(open(r'%s'%filepath, 'rb').read(),'base64', 'utf-8')
    att = MIMEApplication(open(r'%s'%filepath,'rb').read())
    att.add_header('Content-Disposition', 'attachment', filename=filepath)

    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename="pyresult.html"'
    txt = MIMEText("Dear_All,这是测试报告的邮件，详情见附件！",'plain','gb2312')
    msg.attach(txt)
    msg.attach(att)
    try:
        server = smtplib.SMTP_SSL("smtp.qq.com",465)
        server.login(from_addr, password)
        server.sendmail(from_addr, mail_to, msg.as_string())
        server.quit()
    except:
        print('邮件发送失败，请检查配置文件')