"""
    1,单继承
    2,继承链 a-->b-->c
    3,多继承,一个子类同时继承多个父类
"""
# 定义一个动物类
class Animal(object):
    def eat(self):
        print("我会吃")
# 定义一个狗类
class Dog(Animal):
    def jiao(self):
        print("我会吃哦")
# 定义一个哈士奇类
class Hashiqi(Dog):
    def chaijia(self):
        print("我会拆家哦")
# 实例化对象
h = Hashiqi()
h.eat()
h.jiao()
h.chaijia()