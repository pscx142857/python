class Student(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

s = Student("张三",18)
del s.name
s.name