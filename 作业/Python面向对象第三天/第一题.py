"""
1.上课代码1遍
"""
# 类属性和实例属性
class Student(object):
    # 类属性
    classname = "测试班"
    def __init__(self,name):
        # 实例属性
        self.name = name
 # 创建一个学生对象
st = Student("张三")
# 调用类属性
print(Student.classname) # 不用创建对象,节约内存空间
# 调用实例属性
print(st.name)
# 类方法和静态方法
class Teacher(object):
    @classmethod # 类方法
    def info(cls):
        print("我是类方法")
    @staticmethod # 静态方法
    def show():
        print("我是静态方法")
Teacher.info()
Teacher.show()
# __new__方法
class Father(object):
    def __new__(cls, *args, **kwargs):
        print("创建对象的时候执行")
        return super().__new__(cls)
    def __init__(self):
        print("初始化")
fa = Father()
print(fa)
# 单例模式
class Singleton(object):
    # 定义一个类属性,私有化
    __addr = None
    # 重写__new__方法
    def __new__(cls, *args, **kwargs):
        # 如果为空,则创建对象
        if cls.__addr == None:
            cls.__addr = super().__new__(cls)
        # 如果不为空,则不创建,直接返回对象
        return cls.__addr
# 实例化对象
s1 = Singleton()
s2 = Singleton()
print(s1)
print(s2)
# 异常
print("-----开始-----")
try:
    # 可能出现异常的代码
    print(name)
except Exception as e:
    # 处理异常的代码
    print(e,type(e))
else:
    # 没有异常执行的代码
    print("没有出现异常")
finally:
    # 不管有没有异常,都会执行的代码
    print("----结束----")

# 异常的传递
try:
    try:
        print(name)
    # 第一次捕获失败
    except FileNotFoundError:
        print("第一次捕获")
# 传递到外层,捕获成功
except NameError:
    print("第二次捕获")
# 手动抛出异常
password = "123456"
if password == "8888":
    print("登录成功")
else:
    print("登录失败")
    # 手动抛出异常后,后面代码不再执行
    # raise Exception("登录失败了")
print("可以开始购物了")

# 导入模块
import module

print(module.name)
module.info()
module.Animal().show()