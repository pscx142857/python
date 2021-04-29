import simplejson
def save(cards):
    # 打开文件
    fp = open("data.txt","w",encoding="utf8")
    # 操作文件
    data = "\n".join(cards)
    fp.write(data)
    # 关闭文件
    fp.close()
# 读取数据
def load():
    new_cards = list()
    # 打开文件
    fp = open("data.txt","r",encoding="utf8")
    # 操作文件
    data = fp.read()
    # print(data)
    cards = data.split("\n")
    for i in cards:
        card = simplejson.loads(i) # 转成字典
        new_cards.append(card)
    # print(cards)
    # 关闭文件
    fp.close()
    return new_cards

new_cards = list()
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

        # 列表[字典]转列表[字符串]
        for i in cards:
            card_st = simplejson.dumps(i)
            new_cards.append(card_st)
        # 调用保存函数,保存数据
        save(new_cards)
        print("恭喜你修改成功")
        # 修改后直接结束遍历,跳出循环
        break
else:
    # 没有找到,提示用户
    print("对不起,没有此人")