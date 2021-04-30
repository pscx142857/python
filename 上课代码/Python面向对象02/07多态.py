"""
    多态:
    在Python语法中,可以在多个子类中重写父类的方法
    这个时候所有的子类和父类中虽然都有相同名字的方法,
    但是实现的效果是不同的,这就是多态
"""
# 定义一个动物类
class Animal(object):
    def eat(self):
        print("我会吃")
# 定义一个狗类
class Dog(Animal):
    def eat(self):
        print("我会吃骨头")
# 定义一个哈士奇类
class Hashiqi(Dog):
    def eat(self):
        print("我会吃狗骨头")
# 实例化对象
h = Hashiqi()
h.eat()
h = Dog()
h.eat()
h = Hashiqi()
h.eat()