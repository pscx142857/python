"""
    分析:
    从文件读取数据,创建名片对象,将这些数据添加到名片对象的属性上面
    创建一个名片盒子对象
    是否需要读取数据,保存数据的函数或者方法,如果是方法写在哪个类里面

"""


def save(cards):
    ls2 = list()
    # 打开文件
    fp = open("data.txt", "w", encoding="utf8")
    # 操作文件
    for card in cards.ls:
        ls2.append(
            f"{card.name},{card.tel},{card.company},{card.job},{card.address}\n")
    fp.writelines(ls2)
    # 关闭文件
    fp.close()
# 定义一个名片类


class Card(object):
    # 初始化方法里面写名片的属性,添加属性
    def __init__(self, name, tel, company, job, address):
        self.name = name
        self.tel = tel
        self.company = company
        self.job = job
        self.address = address
    # 打印对象的时候执行的方法,可以写展示名片的信息

    def __str__(self):
        return f"{self.name}\t\t{self.tel}\t\t{self.company}\t\t{self.job}\t\t{self.address}"
# 定义一个名片盒子类


class Cards(object):
    # 初始化方法里面写添加属性,这个ls是个列表,可以装多个名片对象
    def __init__(self, ls):
        self.ls = ls
    # 添加名片的方法

    def add(self, ls):
        # 让用户输入要添加的信息
        name = input("请输入姓名:")
        tel = input("请输入姓名:")
        company = input("请输入姓名:")
        job = input("请输入姓名:")
        address = input("请输入姓名:")

        # 创建一个新的名片对象,把这些信息添加到名片对象上
        new_card = Card(name, tel, company, job, address)
        # 如何把这个名片对象添加进名片盒子对象,就是self
        ls.append(new_card)
        self.ls = ls
        print("恭喜你添加成功")
        save(self)
    # 展示名片的方法
    def show(self):
        # 表头
        print("姓名\t\t电话\t\t\t\t公司\t\t\t职位\t\t地址")
        for card in self.ls:
            print(card)

    # 修改名片的方法
    def reverse(self):
        # 让用户输入要修改名片的姓名
        name = input("请输入要修改名片的姓名:")
        # 根据这个姓名去匹配是否有这张名片,有-->修改,没有-->提示没有此人
        for card in self.ls:
            if card.name == name:
                name = input("请输入新的姓名:")
                tel = input("请输入新的电话:")
                company = input("请输入新的公司:")
                job = input("请输入新的职位:")
                address = input("请输入新的地址:")
                # 更新名片对象的属性
                card.name = name
                card.tel = tel
                card.company = company
                card.job = job
                card.address = address
                print("恭喜你修改成功")
                save(self)
                break
        else:
            print("对不起,没有找到此人")

    # 删除名片的方法
    def delete(self, ls):
        # 让用户输入要删除名片的姓名
        name = input("请输入要删除名片的姓名:")
        # 根据这个姓名去匹配是否有这张名片,有-->删除;没有-->提示没有此人
        for card in self.ls:
            if card.name == name:
                # 匹配到就删除
                ls.remove(card)
                self.ls = ls
                print("恭喜你删除成功!")
                save(self)
                break
        else:
            print("对不起,没有此人")
# 保存数据的函数


"""
    数据准备
"""
ls = list()
# 打开文件
fp = open("data.txt", "r", encoding="utf8")
# 操作文件
st = fp.read()
# 关闭文件
fp.close()
# 根据读取出来的数据,创建名片对象,并添加上属性
new_st = st.strip("\n")
for i in new_st.split("\n"):
    new_ls = i.split(",")
    name = new_ls[0]
    tel = new_ls[1]
    company = new_ls[2]
    job = new_ls[3]
    address = new_ls[4]
    card = Card(name, tel, company, job, address)
    ls.append(card)
# 创建一个名片盒子类
cards = Cards(ls)

# 主程序,死循环,一直执行
while True:
    # 根据用户选择的功能执行对应的方法
    st = input("请选择你要执行的功能(1-添加 2-展示 3-修改 4-删除 5-退出):")
    if st == "1":
        cards.add(ls)
    elif st == "2":
        cards.show()
    elif st == "3":
        cards.reverse()
    elif st == "4":
        cards.delete(ls)
    elif st == "5":
        exit("退出系统")
    else:
        print("对不起,输入错误,请重新输入")