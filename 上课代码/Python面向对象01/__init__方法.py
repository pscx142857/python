"""
    魔法方法:__init__   __str__     __new__     __del__     __call__
    __str__方法:在对象被打印的时候,自动调用执行
    特点是名字固定,都会在某一个时机下,自动调用执行
    __init__方法: 初始化方法
    在创建对象的时候自动执行
"""

class Student:
    # 有一个说话的方法
    def __init__(self,name,age=18,sex="男",tel=13456789123):
        self.name = name
        self.age = age
        self.sex = sex
        self.tel = tel
        # print(f"我的名字是{self.name},我的年龄是{self.age},我的性别是{self.sex},我的电话是{self.tel}")
    def speak(self):
        # self就是我自己,谁调用就是谁,self.name调用类里面的属性
        print(f"大家好,我是{self.name}")
        # 调用类里面的方法
        self.homework()

    def homework(self):
        print("我在写作业")
    def __str__(self):
        return "打印的时候我被执行了"
# 创建对象的时候,自动调用__init__方法,给对象添加属性
st1 = Student("张三")
st2 = Student("李四")

print(st1)
st1.speak()
st2.speak()
