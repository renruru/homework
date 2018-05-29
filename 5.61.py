import requests
respose = requests.get('heep://www.baidu.com')
try:
 file = open('wcq.html','w',encoding='utf-8')
 file.write(respose.text)
except:
    print('Error')
finally:
    file.close
# respose.text