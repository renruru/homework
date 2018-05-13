# import itchat
# from itchat.content import *
# import re

# @itchat.msg_register([TEXT])
# def replay(msg):
#     itchat.send('我在学习ing',msg['FromUserName'])
# @itchat.msg_register([PICTURE])
# def pic_replay(msg):
#     itchat.send('来啊，互相伤害啊',msg['FromUserName'])

# itchat.auto_login()
# itchat.run()


import itchat
from itchat.content import *
import re

@itchat.msg_register([TEXT])
def replay(msg):
    pattern = re.search('学习',msg['Text']).span() 
    if pattern:
        itchat.send('我在学习ing',msg['FromUserName'])
@itchat.msg_register([PICTURE])
def pic_replay(msg):
    itchat.send('来啊，互相伤害啊',msg['FromUserName'])

itchat.auto_login()
itchat.run()



# wordcloud


