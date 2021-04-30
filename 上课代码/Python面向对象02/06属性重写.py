"""
    __init__方法的重写问题:
    super().父类的方法名() ,在子类中调用父类的方法执行一次
"""
class Father(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def smoke(self):
        print("我会抽烟")

class Sun(Father):
    def __init__(self,name,age,sex):
        # 调用一次父类的__init__方法就可以继承上面的属性了name,age
        super().__init__(name,age)
        self.sex = sex
    def smoke(self):
        print(f"我的名字是{self.name},我的年龄是{self.age},我是{self.sex}的")

s = Sun("张三","14","男")
s.smoke()