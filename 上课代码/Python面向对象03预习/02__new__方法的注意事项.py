"""
    __new__
    1,至少有一个参数cls,代表要实例化的类,有Python解释器自动提供
    2,必须要有返回值,返回实例化出来的实力
    3,如果创建对象的时候传递了实参,切重写了__new__方法,则__new__也必须预留该形参
"""

class Student(object):
    def __new__(cls,name):
        return object.__new__(cls)
    def __init__(self,name):
        self.name = name
s = Student("李四")
print(s.name)