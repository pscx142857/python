"""
3.定义一个模块
    模块里面具有三个类
    厨师:炒菜方法
    服务员:接待客人方法 送走客人方法
    收银员:收钱方法

    客人来-->服务员接待-->客人点菜-->厨师炒菜-->客人吃完了-->收营员收钱-->服务员送菜
"""
# 导入模块
import restaurant
# 客人来
restaurant.guestcome()
# 服务员接待
restaurant.Waiter().reception()
# 客人点菜
restaurant.order()
# 厨师炒菜
restaurant.Chef().stirfry()
# 客人吃完了
restaurant.order()
# 收银员收钱
restaurant.Cashier().money()
# 服务员送客
restaurant.Waiter().goodbye()

