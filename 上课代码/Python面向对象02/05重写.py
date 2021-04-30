"""
    重写:
        重新写,重写发生在继承中
        子类的方法和属性和父类的重名,那么子类就重写了父类的属性或者方法,以子类的为准
"""
class Father(object):
    def smoke(self):
        print("我会抽烟")

class Sun(Father):
    def smoke(self):
        print("我抽的是华子!!!")

s = Sun()
s.smoke()