# 7.名片管理系统文件版本的完成
import simplejson # 导入simplejson模块,可以使用字符串转字典(simplejson.loads)或者字典转字符串(simplejson.dumps)
# 添加
def add():
    """
    根据用户输入的信息添加名片
    :return:
    """
    # 调用加载函数,读取数据
    cards = load()
    # 让用户输入添加的信息
    name = input("请输入姓名:")
    tel = input("请输入电话:")
    company = input("请输入公司名称:")
    job = input("请输入公司职位:")
    address = input("请输入公司地址:")
    # 用一张名片将用户输入的信息存起来,这个名片是个字典
    card = {
        "name": name,
        "tel": tel,
        "company": company,
        "job": job,
        "address": address}
    # 将这张名片添加到名片盒子(cards)里面
    cards.append(card)
    # 调用保存函数,保存数据
    save(cards)
    # 提示添加成功
    print("恭喜你添加成功")
# 显示
def show():
    """
    将名片盒子里面的名片展示出来
    :return:
    """
    # 调用加载函数,读取数据
    cards = load()
    # 打印表头
    print("姓名\t\t电话\t\t\t\t公司\t\t\t职位\t\t地址")
    # 循环遍历名片盒子,获取到一张一张的名片
    for card in cards:
        # 遍历名片,获取字典里面的值,然后显示出来
        for v in card.values():
            print(f"{v}\t\t", end="")
        print()
# 修改
def reverse():
    """
    根据用户输入的姓名修改名片
    :return:
    """
    # 修改 根据用户输入的姓名修改名片
    # 调用加载函数,读取数据
    cards = load()
    # 让用户输入想修改的姓名
    name = input("请输入你要修改名片的姓名:")
    # 根据用户输入的姓名去找是否有这张名片,遍历名片盒子
    for card in cards:
        # 如果找到这张名片,就让用户输入新的信息,进行修改
        if card["name"] == name:
            name = input("请输入新的姓名:")
            tel = input("请输入新的电话:")
            company = input("请输入新的公司名称:")
            job = input("请输入新的公司职位:")
            address = input("请输入新的公司地址:")
            # 根据字典的键来修改
            card["name"] = name
            card["tel"] = tel
            card["company"] = company
            card["job"] = job
            card["address"] = address

            # 调用保存函数,保存数据
            save(cards)
            print("恭喜你修改成功")
            # 修改后直接结束遍历,跳出循环
            break
    else:
        # 没有找到,提示用户
        print("对不起,没有此人")
# 删除
def delete():
    """
    根据用户输入的姓名删除名片
    :return:
    """
    # 调用加载函数,读取数据
    cards = load()
    # 让用户输入想删除名片的姓名
    name = input("请输入你要删除名片的姓名:")
    # 根据用户输入的姓名去找是否有这张名片,遍历名片盒子
    for card in cards:
        # 如果找到这张名片,直接删除
        if card["name"] == name:
            cards.remove(card)
            # 调用保存函数,保存数据
            save(cards)
            print("恭喜你删除成功")
            # 删除后直接结束遍历,跳出循环
            break
    else:
        # 没有找到,提示用户
        print("对不起,没有此人")
# 保存数据
def save(cards):
    """
    保存名片盒子的数据到文本文档
    :param cards: 传入的是一个列表[字典]的类型
    :return:
    """
    # 格式化处理,将传入的列表里面的元素转成字符串类型,字典-->字符串(simplejson.dumps)
    new_cards = list()
    for i in cards:
        # 字典转字符串
        card = simplejson.dumps(i)
        new_cards.append(card)
    # 打开文件
    fp = open("data_7.txt","w",encoding="utf8")
    # 操作文件
    data = "\n".join(new_cards)
    fp.write(data)
    # 关闭文件
    fp.close()
# 读取数据
def load():
    """
    将data_7.txt里面的数据读取出来
    :return: 返回的是一个列表[字典]的样式数据
    """
    # 打开文件
    fp = open("data_7.txt", "r", encoding="utf8")
    # 操作文件
    data = fp.read()
    # print(data)
    cards = data.split("\n")
    # 格式化名片盒子数据,将列表里面的元素转成字典类型,字符串-->字典(simplejson.loads)
    new_cards = list()
    for i in cards:
        card = simplejson.loads(i)  # 转成字典
        new_cards.append(card)
    # print(cards)
    # 关闭文件
    fp.close()
    return new_cards

# 主程序,死循环,让程序一直运行
while True:
    # 根据用户的输入选择功能
    st = input("请输入数字选择功能(1-添加 2-显示 3-修改 4-删除 5-退出):")
    # 根据用户输入的信息判断执行哪个功能
    if st == "1":
        # 调用添加函数
        add()
    elif st == "2":
        # 调用显示函数
        show()
    elif st == "3":
        # 调用修改函数
        reverse()
    elif st == "4":
        # 调用删除函数
        delete()
    elif st == "5":
        # 退出
        exit("退出系统")
    else:
        print("对不起,输入错误,请重新输入")