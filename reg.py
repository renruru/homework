#爬虫

# import re
# import urllib.request
# #1.get html text

# r = urllib.request.urlopen("http://118.31.19.120:3000/")
# html = r.read(100).decode('utf-8')

# #2. html =  '<span class="top_score">7315</span>'



# # html =  '<span class="top_score">7315</span>'
# res = re.findall('<span class="top_score">(.+?)</span>',html)
# print(res)
# #
# #
# #3. 7315 --#