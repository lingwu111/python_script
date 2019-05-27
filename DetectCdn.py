#-*- coding:utf-8 -*-
# Detect CDN
# author: 凌舞
# data:2019-05-25
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import re
from bs4 import BeautifulSoup



total_ip = 1
host = "www.baidu.com"
header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)', 'host' : host}
host = "www.baidu.com"
data = {"host": host,"linetype":"%E7%94%B5%E4%BF%A1%2C%E5%A4%9A%E7%BA%BF%2C%E8%81%94%E9%80%9A%2C%E7%A7%BB%E5%8A%A8%2C%E6%B5%B7%E5%A4%96", \
        'header': header}

'''<span id="gip" class="plr5 col-blue02">17</span>'''


'''
headlesss模式
'''
options = webdriver.FirefoxOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

# req = requests.post('http://ping.chinaz.com/',data=data)
url =  'http://ping.chinaz.com/' + host
print("预计需要1分钟时间，请稍等片刻！")
driver=webdriver.Firefox(executable_path ="D:\python\python3\geckodriver\geckodriver.exe", options=options)
driver.get(url)
sleep(50)
page = driver.page_source


bs = BeautifulSoup(page, 'lxml')

driver.close()

total_ip = bs.find('span', id='gip').string      # class标签需要写成class_

ips    = bs.find_all('div' , id='ipliststr')

ips_info = []
for ip in ips:
    print(ip.text+'\n')
    


if total_ip == 1:
    print("%s 没有CDN保护!"  % (host))
elif total_ip == 2 or total_ip == 3:
    print("%s 可能有CDN保护! 共检测到独立%s 个ip:" % (host, total_ip))
    print('')
else:
    print("%s 有CDN保护! 共检测到独立%s 个ip！" % (host, total_ip))


