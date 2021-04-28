"""
需求：
    1.程序启动，提示用户登录或者注册
    2.选择注册->要求输入用户名和密码->返回注册提示信息
    3.选择登录->要求输入用户和密码->判断是否登录成功
分析
    1.根据录入的1,2 判断用户为登录和注册
    2.注册: 将用户录入的用户名和密码以下面的格式写入到文件中
     用户名1|密码1
     用户名2|密码2
    3.登录: 读取出每一行并且通过|分割出来用户名和密码与用户录入的用户名和密码进行比对
"""

# 注册
def register():
    """
    根据用户输入的用户名和密码进行注册,保存在user.txt文件中
    :return:
    """
    # 接收用户输入的用户名和密码
    username = input("请输入账号:")
    password = input("请输入密码:")

    # 打开文件
    fp = open("user.txt","a",encoding="utf8")
    # 操作文件
    fp.write(f"{username}|{password}\n")
    # 关闭文件
    fp.close()
    print("恭喜你注册成功")
# 登录
def login():
    """
    根据用户输入的用户名和密码判断是否登录成功
    :return: True表示登录成功,False表示登录失败
    """
    # 接收用户输入的用户名和密码
    username = input("请输入账号:")
    password = input("请输入密码:")

    # 打开文件
    fp = open("user.txt","r",encoding="utf8")
    # 操作文件
    """
        处理存好的数据后做对比:
        data = fp.read()
    ls = data.strip("\n").split("\n")
    for user in ls:
        ls_new = user.split("|")
        if ls_new[0] == username and ls_new[1] == password:
            return True
    else:
        return False
    """
    """
        处理输入的数据后,做对比
    """
    data = fp.readlines()
    # 关闭文件
    fp.close()
    for user in data:
        string = f"{username}|{password}\n"
        if user == string:
            return True
    else:
        return False
while True:
    # 让用户选择功能
    st = input("请选择你需要的功能(1-注册 2-登录 3-退出)")

    if st == "1":
        # 调用注册函数
        register()
    elif st == "2":
        # 调用登录函数
        flag = login()
        if flag:
            print("登录成功")
        else:
            print("登录失败")
    elif st == "3":
        exit("退出系统")
    else:
        print("对不起,输入错误,请重新输入")