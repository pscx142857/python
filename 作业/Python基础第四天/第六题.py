# 写一个后期网络聊天项目的模块，用户不断从键盘输入，每次输入回车后，将打印用户输入的字符个数和内容，当用户输入'quit'后，退出该功能
while True:
    str = input("请输入您想说的话:")
    if str == "quiet":
        break
    print("本次总共说了",len(str),"个字")
    print(str)
