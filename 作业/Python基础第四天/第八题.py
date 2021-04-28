"""
名片管理 系统

# 名片盒子  列表中存放字典,为什么要这样存放?为什么不是字典中存放列表?
cards = [
    {名片信息1},  # 字典
    {名片信息2},
    {名片信息3}
]
需要完成的功能 就是对 名片盒子 进行增删改查
1. 添加名片: 根据用户录入的信息, 组装成字典 追加到名片盒子里面  cards.append(一个人的名片字典)
2. 显示所有名片: 遍历名片盒子输出名片信息
3. 修改名片:  录入需要修改名片的姓名, 根据名字到名片合子查找对应的哪一张名片,
    如果找到 , 重写录入新的名片信息, 完成修改操作
4. 删除名片: 录入需要删除名片的姓名, 根据名字到名片盒子中查到对应的名片并删除.
"""
# 定义个名片盒子name姓名,tel电话,company公司名称,job公司职位,address公司地址
# 初始化名片盒子数据
cards = [
    {"name": "莉莉", "tel": "13125018132", "company": "源码时代", "job": "秘书", "address": "天府新谷"},
    {"name": "丫丫", "tel": "13725488117", "company": "盛唐广告", "job": "经理", "address": "高新西区"},
    {"name": "霏霏", "tel": "18169471248", "company": "蚂蚁金服", "job": "测试", "address": "软件园D区"}
]

# 功能选择函数
def choose():
    # 根据用户输入选择功能:1-增加;2-显示;3-修改;4-删除
    str = input("请输入序号选择需要的功能(1-增加 2-显示 3-修改 4-删除):")
    return str
# 增加函数
def add():
    # 定义一个字典接收输入的名片数据
    in_dic = {"name": "", "tel": "", "company": "", "job": "", "address": ""}
    name = input("请输入姓名:")
    tel = input("请输入电话:")
    company = input("请输入公司名称:")
    job = input("请输入公司职位:")
    address = input("请输入公司地址:")
    # 将输入的数据添加到名片保存
    in_dic["name"] = name
    in_dic["tel"] = tel
    in_dic["company"] = company
    in_dic["job"] = job
    in_dic["address"] = address
    # 将名片放入名片盒子
    cards.append(in_dic)
    print("恭喜你添加成功")
    #print(cards)
# 显示函数
def show():
    # 表头
    print("姓名\t","电话\t"," \t\t 公司名称\t","职位\t","公司地址\t")
    # 遍历名片盒子
    for i in  cards:
        # 遍历名片
        for v in list(i.values()):
            print(v+"\t",end=" ")
        print()
    print("所有数据展示完毕")
# 修改函数
def reverse():
    in_name = input("请输入要修改的姓名:")
    # 遍历名片盒,找到要修改的这张名片
    for i in cards:
        if in_name == i.get("name"):
            print("找到这个人了")
            print("姓名\t", "电话\t", " \t\t 公司名称\t", "职位\t", "公司地址\t")
            for v in i.values():
                print(v+"\t",end=" ")
            print()
            name = input("请输入新的姓名:")
            tel = input("请输入新的电话:")
            company = input("请输入新的公司名称:")
            job = input("请输入新的公司职位:")
            address = input("请输入新的公司地址:")

            i["name"] = name
            i["tel"] = tel
            i["company"] = company
            i["job"] = job
            i["address"] = address
            print("恭喜你修改成功")
            #print(cards)
            break
    else:
        print("没有找到此人")
# 删除函数
def delete():
    in_name = input("请输入要删除的姓名:")
    # 用来记遍历到了第几次,好确定要删除名片的索引
    cont = 0
    for i in cards:
        cont += 1
        if in_name == i.get("name"):
            # 根据索引来删除该名片
            del cards[cont - 1]
            print("恭喜你删除成功")
            break
    else:
        print("没有找到此人")

while True:
    str = input("请输入序号选择需要的功能(1-增加 2-显示 3-修改 4-删除 5-退出):")
    # 执行增加函数
    if str == "1":
        add()
    # 执行显示函数
    elif str == "2":
        show()
    # 执行修改函数
    elif str == "3":
        reverse()
    # 执行删除函数
    elif str == "4":
        delete()
    elif str == "5":
        break
    # 提示重新输入
    else:
        print("输入错误,请重新输入")
