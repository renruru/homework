
import re

# import re
# key = r"<h1>hello world<h1>"#这段是你要匹配的文本 
# p1 = r".+"#这是我们写的正则表达式规则，你现在可以不理解啥意思 
# pattern1 = re.compile(p1)#我们在编译这段正则表达式 
# # matcher1 = re.search(pattern1,key)#在源文本中搜索符合正则表达式的部分 
# # print(matcher1.group(0))#打印出来
# print(pattern1.findall(key))

# print(help(re))
# key = r"<h1>hello world<h1>" 
# p1 = r".*"
# pattern1 = re.compile(p1)
# print(pattern1.findall(key))


# key = r"2533450@sina.pq.ali.amaz.com"
# p1 = r".*"
# pattern1 = re.compile(p1)
# print(pattern1.findall(key))

# key = r"http://www,https://www,httpss://www"
# p1 = r"https*"
# pattern1 = re.compile(p1)
# print(pattern1.findall(key))


# key2=r"<HtMl><Body><h1>welcome</h1></bODy></hTmL>"
# p2 = r"<[Hh],[Tt],[Mm],[Ll]>,<[Bb],>"
# p1 = r".+"
# pattern1 = re.compile(p1)
# print(pattern1.findall(key2))

# key = r"2533450@sina.pq.ali.amaz.com"
# p1 = r"\w+@[a-z]+\.\w+\.+\w+\.\w+\.+\w+"
# p2 = r"\d+\D+"
# pattern1 = re.compile(p2)
# print(pattern1.findall(key))

# key =key = r"chuxiuhong@hit.edu.cn"
# p2 = r"@.+?\."
# pattern1 = re.compile(p2)
# print(pattern1.findall(key))

key = r"192.168.1.1"
p2 = r"\d+"
pattern1 = re.compile(p2)
print(pattern1.findall(key))
