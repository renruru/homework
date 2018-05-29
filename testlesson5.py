# class Student:
#     def __init__(self,name,age,*grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
#     def getname(self):
#         print(self.name)
#         return
#     def getage(self):
#         print(self.age)
#         return
#     def getcourse(self):
#         print(max(self.grade))
#         return

# str = Student("renruru",18,60,80,77)
# str.getname()
# str.getage()
# str.getcourse()




# # class List1:
# #     listw = []
# #     listq = []
# #     def jiaoji():
# #         print()
# #     def bingji():

# class Listcount:
#     def __init__(self, list1, list2):
#         self.list1 = list1
#         self.list2 = list2

#     def count1(self):
#         return (self.list1 & self.list2) #jiaoji

#     def count2(self):
#         return (self.list1 | self.list2) #bingji

#     def count3(self):
#         return (self.list1 ^ self.list2) #chaji


# L1 = set([1, 2, 3])
# L2 = set([1, 4, 5])
# lc = Listcount(L1, L2)
# lc1 = lc.count1()
# lc2 = lc.count2()
# lc3 = lc.count3()
# print(lc1, lc2, lc3)


# property装饰器把方法换成属性，调用不需要括号
class Stu:
    def __init__(self, birth=1990):
        self.birth = birth

    def get_birth(self):
        return self.birth

    def set_birth(self, value):
        self.birth = value

    birthday = property(set_birth, get_birth)


a = Stu()
a.birthday = 1992
print(a.birthday)
        
        

        
