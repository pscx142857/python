# classmethod修饰方法 --> 类方法
class Student(object):

    def __init__(self,name):
        self.name = name

    @classmethod
    def show(cls):
        print("1111")

Student.show()