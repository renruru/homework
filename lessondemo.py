# def add(x,y):
#     return x+y

# res = add(5,2)
# print(res)
# 声明一个类
class Employee:
    # 创建一个变量
    pay_raist_amount = 1.2
    __weight = 40#私有变量
    # 创建一个构造器
    def __init__(self,first,last,age,pay,domain="funcat.com"):
        self.first = first
        self.last = last
        self.age = age
        self.pay = pay
        self.email = first+last+"@"+domain
    # 创建一个方法
    def fullname(self):
        # return self.first+self.last+self.email
        return '{}-{}'.format(self.first,self.last)

    # def new_pay0(self):
    #     # return self.pay*self.pay_raist_amount
    #     return self.pay*Employee.pay_raist_amount

    def new_pay1(self):
        return self.pay*self.pay_raist_amount
        # return self.pay*Employee.pay_raist_amount

    def __say(self):
        print("{}".format(self.__weight))

    def Isay(self):
        self.__say()

    def speak(self):
        print("%s 说：我 %d 岁" %(self.age))

#继承
class Student(Employee):
    w = __weight = 40
    def __init__(self,first,last,pay,domain,grade=3):#参数有默认的值，必须放在参数的最后边
        # Employee.__init__(self,first,last,pay,domain="funcat.com")#需要添加self
        super().__init__(first,last,pay,domain)#不需要添加self
        self.grade = grade
    def speak(self):
        print("%s 说：我 %d 岁，%d 年级" %(self.first,self.age,self.grade))
s = Student('xiao','ming',1000,'.com',5)
# s.speak()
s.Isay()
# s.__say()
print(s.w)
# 实例化对象
# emp1 = Employee("xiaoming","wang",1000,"baidu.com",)
# emp2 = Employee("xiaoming","zhang",20000)
# emp1.Isay()
# emp1.__say()
# Employee.pay_raist_amount = 1.4 #全局变量
# emp1.pay_raist_amount = 1.5 #局部变量，只对emp1有影响s
# # print(emp1.new_pay0())
# print(emp1.new_pay1())
# # print(emp2.new_pay0())
# print(emp2.new_pay1())
# print(emp1.fullname())
# print(emp1.first,emp1.last,emp1.pay,emp1.email)
# print(emp2.first,emp2.last,emp2.pay,emp2.email)