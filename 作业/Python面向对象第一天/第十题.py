# 10.新建一个文件，定义一个龟类，创建一个龟对象，调用上面的属性和方法
# 创建一个龟类
class Turtle():
    # 定义初始化方法,在创建对象的时候会自动执行,给这个对象添加属性
    def __init__(self,age):
        self.age = age

    # 定义一个方法,这个方法里面通过self.属性名,来调用属性
    def show(self):
        print(f"我的年龄是{self.age}")
# 实例化一个对象
turtle = Turtle("3600")
# 调用龟类的方法
turtle.show()