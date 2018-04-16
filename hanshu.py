# def foo():
#     return ('abc',[4-2j,'python'],"guide")
# aTuple = foo() 
# print(aTuple)


# def printinfo(arg1,*vartuple1):
#     print(arg1)
#     for var in vartuple1:
#         print(var)
#     return

# printinfo(10)
# printinfo(30,40,50,60) 

# def f(a):
#     if a==1:
#         return 1
#     else:
#         return a+f(a-1)
# print(f(10))



# a=lambda x:x+1
# print(a(4))

# a = lambda x,y:2*x+1+2*y
# print(a(8,4))


# name = "111"
# def f1():
#     print(name)
#     def f2():
#         name = "222"
#         f1()
#         print(name)
# f1()


# a=10
# def fa(a):
#     a=11
#     return a
# def fb(a):
#     a=12
#     return a
# print(fb(a))
# print(fa(a))


# def func():
#     count = 1
#     def foo():
#         nonlocal count
#         count=12
#     foo()
#     print(count)
# func()


# def make_counter(): 
#     count = 0 
#     def counter(): 
#         nonlocal count 
#         count += 1 
#         return count 
#     return counter 
       
# def make_counter_test(): 
#   mc = make_counter() 
#   print(mc())
#   print(mc())
#   print(mc())
 
# make_counter_test()



s=0
def glo():
    global s
    s+=1
    print(s)
glo()