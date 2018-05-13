
# respose = requests.get('http://www.baidu.com')
# respose.encoding = 'utf-8'
# try:
#  file = open('wcq.html','w',encoding='utf-8')
#  file.write(respose.text)
# except:
#     print('Error')
# finally:
#     file.close

import requests
import re
import urllib.request as ureq

respose = requests.get('http://www.ivsky.com/tupian/haiyangshijie/index_2.html')
respose.encoding = 'utf-8'
html = respose.text

pattern = re.compile(r'<img src="(http://.*?\.jpg)"',re.S)
res = re.findall(pattern,html)
print(res)
i = 0
for x in res:
    ureq.urlretrieve(x,'C:\\Users\\Administrator.W7-201607191031\\Desktop\\a\\%s.jpg'%i)
    i+=1
    print(x)
# i = 0
# while res != 0:
#     ureq.urlretrieve(i,'C:\\Users\\Administrator.W7-201607191031\\Desktop\\a\\1.jpg')


# try:
#     file = open('rrr.html','w',encoding='utf-8')
#     file.write(html)
# except:
#     print('Error')
# finally:
#     file.close
#     print(res)
    

# respose = requests.get('http://jt.sh.cn:8082/wsbs/web/lnfltime/1.jhtml')
# respose.encoding = 'utf-8'
# html = respose.text

# pattern=re.compile(r'<tr.*?>.*?<td bgcolor="#fdeae9"  height="26" rowspan="3" width="100">\r\n\t\t\t\t\t\t\t\t\t\t(.*?)\r\n\t\t\t\t\t\t\t\t\t</td>',re.S)
# res = re.findall(pattern,html)
# print(res)
# try:
#     file = open('rrr.html','w',encoding='utf-8')
#     file.write(html)
# except:
#     print('Error')
# finally:
#     file.close
