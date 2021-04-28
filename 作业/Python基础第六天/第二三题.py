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
# 定义一个名片盒子,初始化数据
cards = [
    {"name": "莉莉", "tel": "13125018132", "company": "源码时代", "job": "秘书", "address": "天府新谷"},
    {"name": "丫丫", "tel": "13725488117", "company": "盛唐广告", "job": "经理", "address": "高新西区"},
    {"name": "霏霏", "tel": "18169471248", "company": "蚂蚁金服", "job": "测试", "address": "软件园D区"}
]
# 添加
def add():
    """
    添加名片的函数
    :return:
    """
    # 定义一个名片,用来储存输入的信息
    card = {"name": "", "tel": "", "company": "", "job": "", "address": ""}
    name = input("请输入姓名:")
    tel = input("请输入电话:")
    company = input("请输入公司:")
    job = input("请输入职位:")
    address = input("请输入地址:")

    # 将输入的信息存储到名片上面
    card["name"] = name
    card["tel"] = tel
    card["company"] = company
    card["job"] = job
    card["address"] = address
    # 将这个名片添加到名片盒子里面
    cards.append(card)
    print("恭喜你添加成功")
# 显示
def show():
    """
    显示所有的名片
    :return:
    """
    # 显示表头
    print("姓名\t\t电话\t\t\t\t公司\t\t\t职位\t\t地址\t\t")
    # 遍历名片盒子,显示名片信息
    for card in cards:
        for v in card.values():
            print(v+"\t\t",end="")
        print()
    print("所有数据已经显示完毕")
# 修改
def reverse():
    """
    修改名片信息
    :return:
    """
    # 接收用户输入的姓名
    name = input("请输入你要修改名片的姓名:")
    # 遍历名片盒子,判断是否有这个姓名的名片
    for card in cards:
        # 找到这个姓名的名片并修改
        if card["name"] == name:
            name = input("请输入新的姓名:")
            tel = input("请输入新的电话:")
            company = input("请输入新的公司:")
            job = input("请输入新的职位:")
            address = input("请输入新的地址:")

            card["name"] = name
            card["tel"] = tel
            card["company"] = company
            card["job"] = job
            card["address"] = address
            print("恭喜你修改成功")
            break
    else:
        print("对不起,没有找到此人")

# 删除
def delete():
    """
    删除名片
    :return:
    """
    name = input("请输入你要删除的名片的姓名:")
    # 找到对应的名片并删除
    for card in cards:
        if card["name"] == name:
            cards.remove(card)
            print("恭喜你,删除成功")
            break
    else:
        print("对不起,没有找到此人")

# 主程序,一直执行
while True:
    # 让用户选择功能
    st = input("请输入数字选择对应的功能(1-增加 2-显示 3-修改 4-删除 5-退出):")
    if st == "1":
        add()
    elif st == "2":
        show()
    elif st == "3":
        reverse()
    elif st == "4":
        delete()
    elif st == "5":
        break
    else:
        print("对不起输入错误,请重新输入")