# 6.新建一个文件，定义一个马类，创建一个马对象，调用上面的属性和方法
# 创建一个花类
class House:
    # 定义初始化方法,在创建对象的时候会自动执行,给这个对象添加属性
    def __init__(self,weight):
        self.weight = weight
    # 定义一个speak方法,这个方法里面通过self.属性名,来调用属性
    def go(self):
        print(f"我的体重是{self.weight}")
# 实例化一个对象
house = House(1238)
# 调用花类的方法
house.go()