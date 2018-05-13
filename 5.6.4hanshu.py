import re
import requests
import urllib.request as R

# def testurl(urll):
#     respose = requests.get(urll)
#     respose.encoding = 'utf-8'
#     patternPIC = re.compile(r'<img width="100".*?src="(https://.*?)"',re.S)
#     reslist1 = re.findall(patternPIC,respose.text)
#     return reslist1


# def testurlres(reslist1,html):
#     i = 1
#     for x in reslist1:
#         x.encode = 'utf-8'
#         R.urlretrieve(x.encode = 'utf-8','C:\Users\Administrator.W7-201607191031\Desktop\%s'%i,)
#         i += 1
#     return x


# print(testurlres(testurl('https://www.douban.com/doulist/13704241/')))






# def testurl(urll):
#     respose = requests.get(urll)
#     return respose.text

# def testurlres(html,pattern):
#     pattern = re.compile(html,re.S)
#     resoult = re.findall(pattern)
#     # resoult = html.findall(pattern)
#     return resoult
   

# if '__name__' == '__main__':
#     testurl('https://www.douban.com/doulist/13704241/')



import itchat
from itchat.content import *


@itchat.msg_register([TEXT])
def reply(msg):
    itchat.send("你说啥，再说一次",msg['FromUserName'])


@itchat.msg_register([PICTURE])
def pic_reply(msg):
    itchat.send("来啊，互相伤害啊",msg['FromUserName'])

itchat.auto_login()
itchat.run()




