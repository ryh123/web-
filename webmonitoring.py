#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import time
import os
import smtplib
from email.mime.text import MIMEText
from selenium import webdriver
from pathlib import Path
from PIL import Image
from PIL import ImageChops



def ppath(url):
    scrpath='D:\\Exstandard'
    scypath='D:\\Exnow'
    url=url.replace('http://','')
    url=url.strip('\n')
    url=url.replace('#tips','')
    url=url.strip('/')  
    capturename = '\\'+url + '.png'                    #自定义命名截图 
    Apath=scrpath+capturename
    Bpath=scypath+capturename
    if Path(scrpath).is_dir():                         #判断文件夹路径是否已经存在
        pass    
    else: 
        Path(scrpath).mkdir()       
    if Path(scypath).is_dir():
        pass
    else:
        Path(scypath).mkdir()
    if  os.path.exists(r'D:\flag.txt'):
        return Bpath
    else:
        return Apath 

def getpicture(url):                                                                   
    picname=url.replace(".html",".jpg")
    browser = webdriver.PhantomJS()  
    browser.get(url)
    browser.implicitly_wait(10)#强制等待10秒
	browser.maximize_window()
    browser.get_screenshot_as_file(ppath(url))  
    browser.close()
#网页截图
  
def send_message(url):                                   
    msg = MIMEText(url,'plain','utf-8')
    from_addr = ''
	#发邮件的邮箱
    password = ''
    to_addr = ''
	#接收邮箱
    smtp_server = 'smtp.163.com'

    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = 'the web is wrong!!!!'

    server = smtplib.SMTP(smtp_server, 25)
    #server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, to_addr, msg.as_string())
    server.quit()
#发送邮件

def urlrequest(url):
    try:
        r = requests.get(url,timeout=15)
        httpCode = r.status_code
        return httpCode
    except requests.exceptions.HTTPError as error:
        return error
#网页正常访问检测

def get_web_code():
    f = open(r'I:\python test\网站状态监控\web监控项目\urls.txt', 'r')  # 将url目录的路径填入
    urllist = f.readlines()
    for url in urllist:
        try:
            url=url.strip('\n')
            print("==========================")
            print(url)
            hcode =urlrequest(url)
            if hcode == 200 or hcode == 302:
                print ("ok")
                getpicture(url)
            elif hcode == 404 or hcode == 502:
                send_message(url)
            else:
                print("请手动检测！！")
        except requests.exceptions.ConnectTimeout:
            send_message(url)

def compare_images(path_one, path_two, diff_save_location):
    image_one = Image.open(path_one)
    image_two = Image.open(path_two)
    diff = ImageChops.difference(image_one, image_two)
    if diff.getbbox() is None:
        print("ok")
    else:
        diff.save(diff_save_location)
#调用PIL库，实现图片对比

def compare_begin():
    diffpath='D:\\Exdiff'
    if Path(diffpath).is_dir():
        pass
    else:
        Path(diffpath).mkdir()
    f = open(r'I:\python test\网站状态监控\urls.txt', 'r')  # 将url目录的路径填入
    urllist = f.readlines()
    for url in urllist:
        url=url.replace('http://','')
        url=url.strip('\n')
        url=url.replace('#tips','')
        url=url.strip('/')
        path_one='D:\\Exnow'+'\\'+url+'.png'
        path_two='D:\\Exstandard'+'\\'+url+'.png'
        path_diff=diffpath+"\\"+url+'.png'
        if os.path.exists(path_one) and os.path.exists(path_two):       
            compare_images(path_one,path_two,path_diff)
        else:
            continue
if __name__ == '__main__':
    try:
        get_web_code()
        open(r"D:\\flag.txt","w+").close()
        compare_begin()
    except:
        print("break")