# -*- coding: utf-8 -*-
import time  
from selenium import webdriver

url=""
picname=url.replace(".html",".jpg")
browser = webdriver.PhantomJS()  
browser.get(url)
browser.maximize_window()   
browser.save_screenshot("shot.png")  
browser.close()
