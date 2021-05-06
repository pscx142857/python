"""
    类属性: 通过类创建的所有的对象,共有的属性
    实例属性: 通过类创建的所有的对象,特有的属性

    调用的方式不同:
        类属性:
            类名.属性名          # 区别,不用创建对象,节约了内存空间
            或者
            1.创建对象
            2.对象名.属性名
        实例属性:
            1.创建对象
            2.对象名.属性名
"""
# 定义一个学生类
class Student(object):
    # 类属性
    classname = "软件测试班"
    # 实例属性
    def __init__(self,name,age):
        self.name = name
        self.age = age

# 实例化一个学生对象
st = Student("张三",30)

# 使用类属性
print(Student.classname) # 类名.属性名     没有创建对象,节约了内存空间
print(st.classname)
# 使用实例属性
print(st.name)