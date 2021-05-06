"""
    厨师:炒菜方法
    服务员:接待客人方法 送走客人方法
    收银员:收钱方法
"""
# 厨师类
class Chef(object):
    # 炒菜的方法
    def stirfry(self):
        print("炒菜")
# 服务员类
class Waiter(object):
    # 接待客人
    def reception(self):
        print("接待客人")
    # 送走客人
    def goodbye(self):
        print("送走客人")
# 收银员
class Cashier(object):
    # 收钱
    def money(self):
        print("收钱")
# 来客
def guestcome():
    print("客人来")
# 点菜
def order():
    print("客人点菜")
# 客人吃完
def over():
    print("客人吃完")