"""
    __new__方法:
    创建对象的时候自动调用执行
    返回类的实力对象
    一般我们会重写该方法,从而自定义对象的创建过程
"""
class Student(object):
    def __new__(cls):
        print("---自定义创建对象---")
        new_obj = object.__new__(cls)
        print(new_obj)
        return new_obj

    def __init__(self):
        print("---初始化话方法中获取对象---")
        print(self)

s = Student()