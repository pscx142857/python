# 定义一个学生类,初始化时可以添加属性
class Student(object):
    def __init__(self,name):
        self.name = name

# 实例化一个学生对象
s = Student("张三")
print(s.name)
# 把name属性修改成李四
s.name = "李四"
print(s.name)