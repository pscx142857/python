# 9.新建一个文件，定义一个鸟类，创建一个鸟对象，调用上面的属性和方法
# 创建一个鸟类
class Bird():
    # 定义初始化方法,在创建对象的时候会自动执行,给这个对象添加属性
    def __init__(self,name):
        self.name = name

    # 定义一个方法,这个方法里面通过self.属性名,来调用属性
    def fly(self):
        print(f"我的名字是{self.name},我会飞")
# 实例化一个对象
bird = Bird("阿刁")
# 调用鸟类的方法
bird.fly()