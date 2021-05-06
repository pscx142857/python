from datetime import datetime
"""
类方法: 方法体中只使用类成员,定义成类方法
        @classmethod装饰
        调用不创建对象,节约内存空间
实例方法:方法体中只使用对象成员,定义成实例方法
静态方法: 不使用类上面的成员,也不使用对象上的成员
        @staticmethod装饰
        调用不创建对象,节约内存空间

"""
# 定义一个学生类


class Student(object):
    # 类属性
    className = "测试班"
    # 实例属性

    def __init__(self, name, age):
        self.name = name
        self.age = age
    # 类方法,用@classmethod修饰

    @classmethod
    def showClassName(cls):
        print(f"我的班级是:{cls.className}")
    # 实例方法

    def showName(self):
        print(f"我的名字是:{self.name}")
    # 静态方法,用staticmethod修改

    @staticmethod
    def showTime():
        print(datetime.now())


# 调用类方法,类名.方法名
Student.showClassName()
# 调用实例方法,对象.方法名
st = Student("张三", 18)
st.showName()
# 调用静态方法,类名.方法名
Student.showTime()
