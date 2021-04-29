"""
    面向对象三大特征:
        封装,继承,多态
    在面向对象的语言中,万物皆对象
"""
# 创建一个学生类,class 类名第一个字母大写:
class Student:
    name = "皮皮"
    def show(self):
        print("大家好,我叫皮皮")
"""
    使用对象,创建类,创建对象
    类有什么,对象就有什么,我们才能用什么
    使用属性,对象.属性
    使用方法,对象.方法名()
"""
stu1 = Student()
stu1.show()
print(stu1.name)
"""
    在类里面调用属性和方法,使用self
    self就是调用方法的这个对象
    
"""
#创建一个老师类
class Teacher:
    # 定义一个方法,可以设置属性
    def init(self,name):
        self.name = name
    # 用self使用属性和方法
    def speak(self):
        self.run()
        print(f"我叫{self.name}")
    def run(self):
        print("我跑着去上课")
teacher = Teacher()
teacher.init("李四")
teacher.speak()
"""
    魔法方法:固定名字和格式,两边是下划线__init__    __str__
            都会在特定的时间,自动执行
    __init__:在创建对象的时候就会自动执行,所以一般用来设置属性
    __str__:在使用打印的时候就会自动执行
"""
class Dog:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return "我在打印的时候执行"
# 创建对象的时候执行__init__方法,设置属性
dog = Dog("兮兮")
print(dog.name)
# 使用打印的时候执行__str__方法
print(dog)
