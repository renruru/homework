# import jieba 
# from wordcloud import WordCloud 
# import matplotlib.pyplot as plt


# s1 = """ 在克鲁伊夫时代，巴萨联赛中完成了四连冠，后三个冠军都是在末轮逆袭获得的。 
# 在91/92赛季，巴萨末轮前落后皇马1分，结果皇马客场不敌特内里费使得巴萨逆转。 
# 一年之后，巴萨用几乎相同的方式逆袭，皇马还是末轮输给了特内里费。 
# 在93/94赛季中，巴萨末轮前落后拉科1分。 
# 巴萨末轮5比2屠杀塞维利亚，拉科则0比0战平瓦伦西亚，巴萨最终在积分相同的情况下靠直接交锋时的战绩优势夺冠。 
# 神奇的是，拉科球员久基奇在终场前踢丢点球，这才有了巴萨的逆袭。"""  
   
# s2 = """ 巴萨上一次压哨夺冠，发生在09/10赛季中。末轮前巴萨领先皇马1分，只要赢球就将夺冠。 
# 末轮中巴萨4比0大胜巴拉多利德，皇马则与对手踢平。 
# 巴萨以99分的佳绩创下五大联赛积分纪录，皇马则以96分成为了悲情的史上最强亚军。"""  
   
# s3 = """在48/49赛季中，巴萨末轮2比1拿下同城死敌西班牙人，以2分优势夺冠。 
# 52/53赛季，巴萨末轮3比0战胜毕巴，以2分优势力压瓦伦西亚夺冠。 
# 在59/60赛季，巴萨末轮5比0大胜萨拉戈萨。皇马巴萨积分相同，巴萨靠直接交锋时的战绩优势夺冠。"""  
   
# mylist = [s1, s2, s3]  
# word_list = [" ".join(jieba.cut(sentence)) for sentence in mylist]  
# new_text = ' '.join(word_list)  
# wordcloud = WordCloud(font_path="D:\\pythoncode\\wordcloud\\MSYH.TTF", background_color="black").generate(new_text)  
# plt.imshow(wordcloud)  
# plt.axis("off")  
# plt.show()  



# from os import path  
# from scipy.misc import imread  
# import matplotlib.pyplot as plt  
  
  
# from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator  
# import sys  
# reload(sys)  
# sys.setdefaultencoding('utf-8')  
# # 获取当前文件路径  
# # __file__ 为当前文件, 在ide中运行此行会报错,可改为  
# # d = path.dirname('.')  
# d = path.dirname(__file__)  
  
  
# # 读取文本 alice.txt 在包文件的example目录下  
# #内容为  
  
  
# """ 
# Project Gutenberg's Alice's Adventures in Wonderland, by Lewis Carroll 
 
 
# This eBook is for the use of anyone anywhere at no cost and with 
# almost no restrictions whatsoever.  You may copy it, give it away or 
# re-use it under the terms of the Project Gutenberg License included 
# with this eBook or online at www.gutenberg.org 
# ' 
# """  
  
  
# text = open(path.join(d, 'alice.txt')).read()  
  
  
# # read the mask / color image  
# # taken from http://jirkavinse.deviantart.com/art/quot-Real-Life-quot-Alice-282261010  
# # 设置背景图片  
# alice_coloring = imread(path.join(d, "2222.png"))  
  
  
# wc = WordCloud(background_color="white", #背景颜色max_words=2000,# 词云显示的最大词数  
# mask=alice_coloring,#设置背景图片  
# stopwords=STOPWORDS.add("said"),  
# max_font_size=40, #字体最大值  
# random_state=42)  
# # 生成词云, 可以用generate输入全部文本(中文不好分词),也可以我们计算好词频后使用generate_from_frequencies函数  
# wc.generate(text)  
# # wc.generate_from_frequencies(txt_freq)  
# # txt_freq例子为[('词a', 100),('词b', 90),('词c', 80)]  
# # 从背景图片生成颜色值  
# image_colors = ImageColorGenerator(alice_coloring)  
  
  
# # 以下代码显示图片  
# plt.imshow(wc)  
# plt.axis("off")  
# # 绘制词云  
# plt.figure()  
# # recolor wordcloud and show  
# # we could also give color_func=image_colors directly in the constructor  
# plt.imshow(wc.recolor(color_func=image_colors))  
# plt.axis("off")  
# # 绘制背景图片为颜色的图片  
# plt.figure()  
# plt.imshow(alice_coloring, cmap=plt.cm.gray)  
# plt.axis("off")  
# plt.show()  
# # 保存图片  
# wc.to_file(path.join(d, "名称.png"))  




import requests
import itchat
from itchat.content import *
import re

URL= 'http://www.tuling123.com/openapi/api'
DATA = {
   'key'  : "e66e074abd16416f805b1cd0b715e10d",
   'info'  :"msg",
   'userid' : 'pth-robot',
}
req = requests.post(URL, data=DATA).json()
res=req.get('text')
@itchat.msg_register([TEXT])
def auto_reply(msg):
    req = requests.post(URL, data=DATA).json()
    res=req.get('text')
    return res

itchat.auto_login()
itchat.run()



# @itchat.msg_register([TEXT])
# def replay(msg):
#     itchat.send('走，一起开黑，who怕who啊',msg['FromUserName'])
# @itchat.msg_register([PICTURE])
# def pic_replay(msg):
#     itchat.send('你要上天吗？继续啊',msg['FromUserName'])
# @itchat.msg_register([RECORDING])
# def rec_reply(msg):
#     itchat.send('风太大，听不见。。。',msg['FromUserName'])

# itchat.auto_login()
# itchat.run()


# from wordcloud import WordCloud
# import matplotlib.pyplot as plt
# from scipy.misc import imread
# import jieba


# #读取一个txt文件

# text = open('F:\\aa\\testaa.txt','r').read()

# #读入背景图片

# bg_pic = imread('F:\\aa\\3.png')

# #生成词云

# wordcloud = WordCloud(font_path="C:\\Windows\\Fonts\\simsun.ttc",mask=bg_pic,relative_scaling=0.5,background_color='black',scale=1.5).generate(text)

# # image_colors = ImageColorGenerator(bg_pic)
# #显示词云图片
# cut_text = " ".join(jieba.cut(text))
# plt.imshow(wordcloud)
# plt.axis('off')
# plt.show()


# #保存图片

# wordcloud.to_file('F:\\aa\\test.jpg')