# class oops:
#     a=10
#     def myfunc(self,name):
#         self.name=name
#
#     def myfunc1(self):
#         print("name", self.name)
#
#     def myfunc2(self):
#         print("name", self.name)
# obj=oops()
# obj.myfunc("susi")
# obj.myfunc1()
# obj.myfunc2()
# print(obj.a)
#
# class Addition:
#     def add(self):
#         a= int(input("entert the value"))
#         b= int(input("entert the value"))
#         c=a+b
#         print(c)
# class subraction:
#     def sub(self):
#         a= int(input("entert the value"))
#         b= int(input("entert the value"))
#         c=a-b
#         print(c)
# obj1=Addition()
# obj1.add()
#
# obj1=subraction()
# obj1.sub()

def deco(feature):
    def test():
        print("login")
        feature()
        print("logoff")
    return test
@deco
def task():
    print("running")
task()


dd=[3,2,1,3,2,1,2,3]
a1 = []
for i in dd:
    for i in not dd:
        a1.append(i)
    print(a1)