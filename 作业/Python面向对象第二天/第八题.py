# 8.将名片管理系统 使用面向对象的方式实现一遍 (在函数的基础上)
# 定义一个名片盒子的类
class Cards(object):
    # 初始化方法给名片盒子对象添加属性
    def __init__(self, cards):
        self.cards = cards

    # 添加

    def add(self):
        """
        根据用户输入的信息添加名片
        :return:
        """
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
        self.cards.append(card)
        # 提示添加成功
        print("恭喜你添加成功")

    # 显示

    def show(self):
        """
        将名片盒子里面的名片展示出来
        :return:
        """
        # 打印表头
        print("姓名\t\t电话\t\t\t\t公司\t\t\t职位\t\t地址")
        # 循环遍历名片盒子,获取到一张一张的名片
        for card in self.cards:
            # 遍历名片,获取字典里面的值,然后显示出来
            for v in card.values():
                print(f"{v}\t\t", end="")
            print()

    # 修改

    def reverse(self):
        """
        根据用户输入的姓名修改名片
        :return:
        """
        # 让用户输入想修改的姓名
        name = input("请输入你要修改名片的姓名:")
        # 根据用户输入的姓名去找是否有这张名片,遍历名片盒子
        for card in self.cards:
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
                print("恭喜你修改成功")
                # 修改后直接结束遍历,跳出循环
                break
        else:
            # 没有找到,提示用户
            print("对不起,没有此人")

    # 删除

    def delete(self):
        """
        根据用户输入的姓名删除名片
        :return:
        """
        # 让用户输入想删除名片的姓名
        name = input("请输入你要删除名片的姓名:")
        # 根据用户输入的姓名去找是否有这张名片,遍历名片盒子
        for card in self.cards:
            # 如果找到这张名片,直接删除
            if card["name"] == name:
                self.cards.remove(card)
                print("恭喜你删除成功")
                # 删除后直接结束遍历,跳出循环
                break
        else:
            # 没有找到,提示用户
            print("对不起,没有此人")


# 实例化一个名片盒子,传入盒子数据
c = Cards([{"name": "莉莉",
          "tel": "13125018132",
            "company": "源码时代",
            "job": "秘书",
            "address": "天府新谷"},
           {"name": "丫丫",
            "tel": "13725488117",
            "company": "盛唐广告",
            "job": "经理",
            "address": "高新西区"},
           {"name": "霏霏",
            "tel": "18169471248",
            "company": "蚂蚁金服",
            "job": "测试",
            "address": "软件园D区"}])
# 主程序,死循环,让程序一直运行
while True:
    # 根据用户的输入选择功能
    st = input("请输入数字选择功能(1-添加 2-显示 3-修改 4-删除 5-退出):")

    # 根据用户输入的信息判断执行哪个功能
    if st == "1":
        # 调用添加方法
        c.add()
    elif st == "2":
        # 调用显示方法
        c.show()
    elif st == "3":
        # 调用修改方法
        c.reverse()
    elif st == "4":
        # 调用删除方法
        c.delete()
    elif st == "5":
        # 退出
        exit("退出系统")
    else:
        print("对不起,输入错误,请重新输入")
