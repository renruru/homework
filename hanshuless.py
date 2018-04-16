import json
import time
import calendar

q = calendar.month(2018,3)
# w = calendar.mdays(0)
t = calendar.LocaleTextCalendar()
# print(q)
print(t)


a = time.time()
b = time.localtime()
c = time.asctime(b)
d = time.clock()
e = time.gmtime()
print(a)
print(b)
print(c)
print(d)
print(e)

string1 = ('worry','hello','njdnj')
tuple1 = ('qwsw','deewded','dewdw',231)
list1 = ['dedw','2333+23e','wedw','dewdwqdwede']
dict1 = {'A':'a','B':'b','C':'c'}

str2 = json.dumps(string1)
print(str2)
print(type(str2))
str3 = json.loads(str2)
print(str3)
print(type(str3))

tuple2 = json.dumps(tuple1)
print(tuple2)
print(type(tuple2))
tuple3 = json.loads(tuple2)
print(tuple3)
print(type(tuple3))

list2 = json.dumps(list1)
print(list2)
print(type(list2))
list3 = json.loads(list2)
print(list3)
print(type(list3))

dict2 = json.dumps(dict1)
print(dict2)
print(type(dict2))
dict3 = json.loads(dict2)
print(dict3)
print(type(dict3))