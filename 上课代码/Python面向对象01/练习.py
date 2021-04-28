# f = open("test.txt",encoding="utf8")
# while True:
#     a = f.readline()  # 读取下一行内容  a = "将 login.txt 的文件 复制一份\n"
#     b = "#"
#     if a == "":
#         f.close()
#         break
#     elif a[0] == b[0]:
#         continue
#     else:
#         print(a, end="")
#
"""
如何在对象方法中使用对象上的属性和方法呢?
self指的啥
"""

class Student:
    # __init__是个什么玩意儿?
    def __init__(self,name,age=18,sex="男",tel=13456789123):
        self.name = name
        self.age = age
        self.sex = sex
        self.tel = tel
    def speak(self):
        print(f"大家好,我是{self.name}")
        self.homework()

    def homework(self):
        print("我在写作业")
    # __str__是个什么玩意儿?
    def __str__(self):
        return "-----"

st1 = Student("张三")
print(st1.name) # 张三
st2 = Student("李四")

print(st1)
# 为什么不用给self传递实参?
st1.speak()
st2.speak()
