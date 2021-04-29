# 8.新建一个文件，定义一个蛇类，创建一个蛇对象，调用上面的属性和方法
# 创建一个蛇类
class Sneak():
    # 定义初始化方法,在创建对象的时候会自动执行,给这个对象添加属性
    def __init__(self,type):
        self.type = type

    # 定义一个方法,这个方法里面通过self.属性名,来调用属性
    def color(self):
        print(f"我的颜色是{self.colo}")
# 实例化一个对象
sneak = Sneak("眼镜蛇")
# 给这个对象添加一个属性
sneak.colo = "绿色"
# 调用蛇类的方法
sneak.color()

