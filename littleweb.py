#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import time
import os
import smtplib
import sys
from email.mime.text import MIMEText
from pathlib import Path

    
def  geturllistpath():
    urllistpath=sys.argv[1]#传入url列表txt的绝对路径
    return urllistpath

def send_message(url):                                   
    msg = MIMEText(url,'plain','utf-8')
    from_addr = ''#自己邮箱地址
    password = ''#密码
    to_addr = ''#需要接受邮箱的地址
    smtp_server = 'smtp.163.com'#邮件服务器

    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = 'the web is wrong!!!!'#主题

    server = smtplib.SMTP(smtp_server, 25)#邮件服务端口号
    #server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, to_addr, msg.as_string())
    server.quit()
#发送邮件



def urlrequest(url):
    try:
        r = requests.get(url,timeout=10)
        httpCode = r.status_code
        return httpCode
    except requests.exceptions.HTTPError as error:
        return error

def get_web_code():
    p2=geturllistpath()
    
    f = open(r'{0}'.format(p2), 'r')
    #将url目录的路径填入
   
    urllist = f.readlines()
    
    for url in urllist:
        try:
            url=url.strip('\n')
            print("---------------------------")
            print(url)
            hcode =urlrequest(url)
            if hcode == 200 or hcode == 302:
                print ("ok")
            elif hcode == 404 or hcode == 502:
                send_message(url)
            else:
                print("请手动检测！！")
        except requests.exceptions.ConnectTimeout:
            send_message(url)
            
            
            
if __name__ == '__main__':
    try:
        get_web_code()
    except:
        print("break")