class Demo:
    def f1(self):
        print("intance methond")

    @classmethod
    def f2(cls):
        print("class method")

    @staticmethod
    def f3(name):
        print(f"{name}")

Demo.f3("test")
Demo.f2()
d=Demo()
d.f1()