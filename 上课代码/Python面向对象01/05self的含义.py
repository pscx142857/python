"""
    self:指的就是对象自己
    哪个对象调用这个方法,这个方法中的self就是这个对象

    在类里面要使用属性或者方法:
    对象.属性名   -->  self.属性名
    对象.方法名() -->  self.方法名()
"""
# 创建一个学生类
class Student:
    # 有一个说话的方法
    def speak(self):
        # self就是我自己,谁调用就是谁,self.name调用类里面的属性
        print(f"大家好,我是{self.name}")
        # 调用类里面的方法
        self.homework()

    def homework(self):
        print("我在写作业")

# 实例化两个对象
st1 = Student()
st2 = Student()
# 给这两个对象添加属性name
st1.name = "张三"
st2.name = "李四"
# 调用方法
st1.speak() # 大家好,我是张三
st2.speak() # 大家好,我是李四
