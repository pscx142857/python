# 3.新建一个文件，定义一个猫类，创建一个猫对象，调用上面的属性和方法
# 定义一个猫类
class Cat:
    # 定义初始化方法,在创建对象的时候会自动执行,给这个对象添加属性
    def __init__(self,name):
        self.name = name
    # 定义一个run方法,这个方法里面通过self.属性名,来调用属性
    def run(self):
        print(f"我的名字是{self.name},我会跑")
# 实例化一个对象
cat1 = Cat("喵喵")
# 调用猫类的方法
cat1.run()
