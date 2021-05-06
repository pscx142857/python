"""
__new__方法: 创建对象的时候自动调用执行
    new方法在init方法的调用前面
    new方法的作用:
        1.开辟内存空间,将对象存放在内存空间中
        2.将创建的对象和参数自动传递给inti方法使用

"""
class Student(object):
    # 重写了__new__方法,调用一次父类里面的__new__方法,才能创建对象
    def __new__(cls, *args, **kwargs):
        print("创建对象")
        return super().__new__(cls)

    def __init__(self):
        print("初始化")

# 创建一个学生对象
st = Student()
print(st)