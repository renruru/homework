class Employee:
    
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property #把方法换成属性
    def fullname(self):
        # return self.first+self.last+self.email
        return '{}-{}'.format(self.first,self.last)

    def setName(self,name):
        self.first,self.last = name.split(' ')

    @staticmethod
    def printmail(username):
        print("email")

e1 = Employee('xiao','ming',7000)
print(e1.fullname)
e1.setName("john master")
# e1.printmail()