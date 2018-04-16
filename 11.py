# from lianxi import my_abs

# print(my_abs(-9))

# a={'a':'10','b':'20','c':'30'}
# def sss(a):
#     return a*10
# print(sss(a))

# def hello(a):
#     print()

def printinfo(arg1,*vartuple1):
    print("输出： ")
    print(arg1)
    for var in vartuple1:
        print(var)
    return

printinfo(10)
printinfo(30,40,50,60) 
