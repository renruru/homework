
# for x in range(10)
#     x%2==1
#     x+=1
#     print (x)

# list1 = [1,2,3,4,5]
# list1.pop()
# print(list1[1:])
# 切片有仨个参数（起始值，结束值，步长）
# 切片都是中括号

# tuple1 = [1,2,3,4,5]
# print(tuple1[1:3])
# str = 'tas'
# list2 = ['qw','dfs']
# # list1= ['tas']
# list1.append(str)
# list1.extend(list2)
# print(list1)

# 元组不可改变，so 没有方法

# tuplex = (1,2,4,5,6,[3,4,6])

# tuplex = (1,2,4,5,6,[2,4,6])
# x = tuplex[5:]
# y = list(x)
# y[0] = 3
# print(y)


# tuplex=(1,2,4,5,6,[3,4,6])
# tuplex=(1,2,4,5,6,[2,4,6])
# tuplex[5][0]=2

# print(tuplex)


# tuplex=(1,2,4,5,6,'hello')
# print(str(tuplex))
# str(tuplex)[5][1]='a'
# print(tuplex)

# tuplex=(1,2,4,5,6,["hello"])
# # tuplex=(1,2,4,5,6,[2,4,6])
# tuplex[5][0]=2
# print(tuplex)

# list7=['a','s','d','f','k']
# a = input()
# if a in list7:
#     print(a)
# else:
#     print("Not null")



# list7=['a','s','d','f','k']
# s=input()
# i = 0
# for i in list7:
#     if s in list7:
#         print(s)
#     else :
#           print("not in ")



# if 后边跟执行条件 or满足一个条件  and同时满足多个条件 
# else 没有条件

# 乘法口诀表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print (i,"*",j,"=",i*j,end = '    ')
#     print('   ')



# 1 3,5,7组成不同的无重复的四位数
# count = 0
# for i in range(1,9,2):
#     for j in range(1,9,2):
#          for k in range(1,9,2):
#              for m in range(1,9,2):
#                 #  print(i*1000+j*100+k*10+m)
#                 if i!=j and i!=k and i!=m and j!=k and j!=m and k!=m:
#                     print(i*1000+j*100+k*10+m)
#                     count+=1
# print(count)



# 一个整数，加上100后是完全平方数，再加上168后还是完全平方数
# x
# x+100
# x+168
# import math
# x = 0
# while x >= 0:
#     if math.sqrt(x+100)-int(math.sqrt(x+100))==0 and math.sqrt(x+268)-int(math.sqrt(x+268))==0:
#          print(x)
#          break
#     x+=1


# 去掉重复数字
# import math 
# list1 = [1,25,3,46,5,6,5,3,2,6,8]
# list2=[]

# for i in list1:
#     if i not in list2:
#         list2.append(i)
#     print(list2) #打印出列表，中括号表示

# list2 = set(list1) #打印出set，大括号表示

# set去重
# list.remove()   #一次删除一个

# list1.sort() # 永久性排序
# print(sorted(list1))  #sorted放在方法中排序

# list1.insert(2,'www')
# list1*3
# print(list1*3)
         
    





# break  跳出循环
# continue 继续循环
# pass   




xiaomin={"inteilgant":"智能的","AI":"人工智能","youdao":"有道","apple":"苹果x","factory":"富土康"}
# # print(xiaomin.keys())
# # print(xiaomin.values())
# # print(xiaomin.items())
# # dict1=xiaomin.copy()
# # dict2=xiaomin.fromkeys([1,2,3],[2,3,4])
# # dict1.popitem()

# # print(dict1)
# xiaomin['inteilgant']='jizhide'
# print(xiaomin)

# tuple1 = (5,) # 定义元组后边加逗号
# print(type(tuple1))

# print(str(xiaomin))
# print(len(xiaomin))
# print(xiaomin.pop["AI"])
# print(xiaomin.pop("AI"))
# del xiaomin["AI"]
# print(xiaomin)


# 1,1,2,3,5,8...
i =1
j = 1
while i < 2000:
    i,j = j,j + i
    print(i)