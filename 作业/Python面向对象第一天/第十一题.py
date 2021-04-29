# 11.新建一个文件，定义一个猴子类，创建一个猴子对象，调用上面的属性和方法
# 创建一个猴子类
class Monkey():
    # 定义初始化方法,在创建对象的时候会自动执行,给这个对象添加属性
    def __init__(self,name):
        self.name = name

    # 定义一个方法,这个方法里面通过self.属性名,来调用属性
    def eat(self):
        print(f"我的名字是{self.name},我爱吃桃子")
# 实例化一个对象
monkey = Monkey("孙悟空")
# 调用猴子类的方法
monkey.eat()