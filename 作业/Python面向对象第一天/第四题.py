# 4.新建一个文件，定义一个狗类，创建一个狗对象，调用上面的属性和方法
# 创建一个狗类
class Dog:
    # 定义初始化方法,在创建对象的时候会自动执行,给这个对象添加属性
    def __init__(self,color):
        self.color = color
    # 定义一个speak方法,这个方法里面通过self.属性名,来调用属性
    def speak(self):
        print(f"我的颜色是{self.color},汪汪汪")
# 实例化一个对象
dog1 = Dog("黄色")
# 调用狗类的方法
dog1.speak()