"""
    必传参数
    默认参数
"""
def show(name,age,sex="女"): #sex=女,给形参设置默认值,实参不传的时候,就默认是这个
    """
    自我介绍函数
    :param name:姓名
    :param age: 年龄
    :param sex: 性别
    :return: 没有返回值
    """
    print(f"我的名字是:{name},我的年龄是:{age},我的性别是:{sex}")

show("丫丫",20,"男")
show("美美",29) # 我的名字是:美美,我的年龄是:29,我的性别是:女

"""
    位置参数
    关键字参数
"""

show("兮兮",66,"女") #依次传入,位置参数
show(age=66,name="兮兮") # 关键字传入,关键字参数
# 位置参数必须在关键字参数前面
#show(sex="男",21,"袋子") # SyntaxError: positional argument follows keyword argument
