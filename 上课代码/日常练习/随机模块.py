"""
用户输入姓名,选取自己的模块
1.顾客/会员
2.商品展示
3.购买流程
4.商品管理
"""
# 导入随机数模块
import random
ls = ["顾客/会员","商品展示","购买流程","商品管理"]
def choise(ls):
    res = random.choice(ls)
    print(f"恭喜你,你的模块是:  {res}!")
    print()
    ls.remove(res)
i = len(ls)
while i >= 1:
    st = input("请输入姓名选择自己的模块:")
    choise(ls)
    i -= 1
print("选择完毕,fighting!!!")
print("选择完毕,fighting!!!")
print("选择完毕,fighting!!!")
while True:
    pass
