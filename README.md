# web monitoring
用python实现对多个网站能否正常访问进行监控，并向邮箱发送报警邮件


使用：
python3  "../url.txt"   #脚本后加需要检测的url网址的txt文件路径


需要的库
import requests
import time
import os
import smtplib
import sys
from email.mime.text import MIMEText
from pathlib import Path
