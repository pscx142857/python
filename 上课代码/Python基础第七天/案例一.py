#     1.程序启动，提示用户登录或者注册
#     2.选择注册->要求输入用户名和密码->返回注册提示信息
#     3.选择登录->要求输入用户和密码->判断是否登录成功
# 分析
#     1.根据录入的1,2 判断用户为登录和注册
#     2.注册: 将用户录入的用户名和密码以下面的格式写入到文件中
#     用户名1|密码1
#     用户名2|密码2
#     3.登录: 读取出每一行并且通过|分割出来用户名和密码与用户录入的用户名和密码进行比对
# 注册
def register():
    """
    根据用户输入的账号和密码注册,保存在user.txt中
    :return:
    """
    # 用户输入账号密码
    username = input("请输入用户名:")
    password = input("请输入密码:")
    # 打开文件
    fp = open("user.txt","a",encoding="utf8")
    # 操作文件
    ls = [username,"|",password]
    fp.writelines(ls)
    fp.write("\n")
    # 关闭文件
    fp.close()
    print("恭喜你注册成功")
    print("您的账号是:",username)
    print("您的密码是:",password)
 # 登录
def login():
    """
    根据用户输入的账号密码登录
    :return:
    """
    # 用户输入账号密码
    username = input("请输入用户名:")
    password = input("请输入密码:")

    # 打开文件
    fp = open("user.txt","r",encoding="utf8")
    # 操作文件
    st = fp.read()
    ls = st.split("\n")
    ls.pop()

    for user in ls:
        ls_new = user.split("|")
        if ls_new[0] == username and ls_new[1] == password:
            print("恭喜你登录成功")
            break
    else:
        print("对不起,登录失败")

    # 关闭文件
    fp.close()

while True:
    st = input("请选择需要的功能(1-注册 2-登录 3-退出):")
    if st == "1":
        register()
    elif st == "2":
        login()
    elif st == "3":
        exit("退出系统")
    else:
        print("对不起输入错误,请重新输入")