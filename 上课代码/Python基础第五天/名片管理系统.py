"""
名片管理 系统

# 名片盒子  列表中存放字典,为什么要这样存放?为什么不是字典中存放列表?
name姓名,tel电话,company公司名称,job公司职位,address公司地址
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
# 初始化名片盒子
cards = [
    {"name":"兮兮","tel":"13156781234","company":"源码时代","job":"前台","address":"天府新谷"},
    {"name":"丫丫","tel":"13256781234","company":"美圣天使","job":"经理","address":"高新西区"},
    {"name":"美美","tel":"13356781234","company":"时代科技","job":"测试","address":"四川德阳"}
]
# 添加函数
def add():
    # 定义要输入的名片信息
    name = input("请输入姓名:")
    tel = input("请输入电话:")
    company = input("请输入公司名称:")
    job = input("请输入公司职位:")
    address = input("请输入公司地址:")

    # 定义一张空名片
    card = {"name":"","tel":"","company":"","job":"","address":""}
    # 保存到一张名片中
    card["name"] = name
    card["tel"] = tel
    card["company"] = company
    card["job"] = job
    card["address"] = address
    # 添加到名片盒子里面
    cards.append(card)
    print("恭喜你添加成功")
# 显示函数
def show():
    # 表头
    print("姓名\t\t电话\t\t\t\t公司\t\t\t职位\t\t地址")
    for i in cards:
        for v in i.values():
            print(v+"\t\t",end="")
        print()
    print("所有数据展示完毕")
# 修改函数
def reverse():
    name = input("请输入你要修改名片的姓名:")
    # 根据姓名找到这张名片
    for card in cards:
        if card["name"] == name:
            # 进行修改
            name = input("请输入新的姓名:")
            tel = input("请输入新的电话:")
            company = input("请输入新的公司名称:")
            job = input("请输入新的公司职位:")
            address = input("请输入新的公司地址:")

            card["name"] = name
            card["tel"] = tel
            card["company"] = company
            card["job"] = job
            card["address"] = address
            print("恭喜你修改成功")
            break
    else:
        print("对不起,没有找到此人")
# 删除函数
def delete():
    name = input("请输入你要删除名片的姓名:")
    # 根据姓名找到这张名片
    for card in cards:
        if card["name"] == name:
            index = cards.index(card)
            del cards[index]
            print("恭喜你删除成功")
            break
    else:
        print("对不起,没有找到此人")
# 主程序
while True:
    str = input("请选择你需要的功能(1-添加 2-显示 3-修改 4-删除 5-退出):")
    if str == "1":
        # 调用添加函数
        add()
    elif str == "2":
        # 调用显示函数
        show()
    elif str == "3":
        # 调用修改函数
        reverse()
    elif str == "4":
        # 调用删除函数
        delete()
    elif str == "5":
        break
    else:
        print("对不起,输入错误,请重新输入")


