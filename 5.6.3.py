import re
import requests
import urllib.request as R

respose = requests.get('https://www.douban.com/doulist/13704241/')
respose.encoding = 'utf-8'

patternPIC = re.compile(r'<img width="100".*?src="(https://.*?)"',re.S)
patternDis = re.compile(r'<div class="title">.+?<a href.+?_blank">(.*?).*?</a></div>',re.S)

reslist1 = re.findall(patternPIC,respose.text)
reslist2 = re.findall(patternDis,respose.text)
print(reslist1)
print(reslist2)


