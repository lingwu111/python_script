
#-*- coding:utf-8 -*-
# url_clean
# author: 凌舞
# data:2019-05-24



import re

'''^http:\/\/[A-Za-z0-9]+\.[A-Za-z0-9]+[\/=\?%\-&_~`@[\]\':+!]*([^<>\"\"])*$'''
'''IP：(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])'''


with open("ZghUrl.txt", 'r+', encoding='utf-8') as f, \
     open("ZghResults.txt", 'w+', encoding='utf-8') as g:
        
    lines_f = f.readlines()
    for line_f in lines_f:
        url_f = line_f.strip().replace('"', '').replace(' ', '')
        url1 = re.findall('(?<![\.\d])(?:\d{1,3}\.){3}[^\s]*', url_f)
        url1 = ''.join(url1) + '\n'
        url2= re.findall('([a-zA-z]+://[^\s]*)', url_f)
        url2 = ''.join(url2) .strip('/')+ '\n'
          
        
        if url1 == '\n' :
            url1 = url1.strip("\n")
        else:
            url1 = url1
        g.write(url1)
        if url2 == '\n' :
            url2 = url2.strip("\n")
        else:
            url2= url2
        g.write(url2)       
        
            
print('success!')