# 5.新建一个文件，定义一个花类，创建一个花对象，调用上面的属性和方法
# 创建一个花类
class Flower:
    # 定义初始化方法,在创建对象的时候会自动执行,给这个对象添加属性
    def __init__(self,color):
        self.color = color
    # 定义一个speak方法,这个方法里面通过self.属性名,来调用属性
    def jieguo(self):
        print(f"我的颜色是{self.color}的哦")
# 实例化一个对象
flower = Flower("蓝色")
# 调用花类的方法
flower.jieguo()