# 4.编写1个python程序，完成以下要求：
#     1.1 设计一个功能从键盘获取用户的姓名、性别、家庭地址
#     1.2 打印从该功能中获取的信息
def info():
    """
    输入姓名,性别,家庭住址后打印出来
    :return:  没有返回值
    """
    name = input("请输入姓名:")
    sex = input("请输入性别:")
    address = input("请输入家庭地址:")
    print(f"我的姓名是:{name},我的性别是:{sex},我的家庭住址是:{address}")

info()