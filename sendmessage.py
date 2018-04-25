#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
msg = MIMEText(url,'plain','utf-8')
from_addr = ''
password = ''
to_addr = ''
smtp_server = ''
	
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = 'the frist mail'
	
server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, to_addr, msg.as_string())
server.quit()
