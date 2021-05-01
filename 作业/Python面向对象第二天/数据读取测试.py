"""
    读取数据出来之后,创建对象,给对象添加属性
"""
class Card(object):
    # 初始化方法里面写名片的属性,添加属性
    def __init__(self,name,tel,company,job,address):
        self.name = name
        self.tel = tel
        self.company = company
        self.job = job
        self.address = address
    # 打印对象的时候执行的方法,可以写展示名片的信息
    def __str__(self):
        return f"{self.name}\t\t{self.tel}\t\t{self.company}\t\t{self.job}\t\t{self.address}"
# 打开文件
fp = open("data.txt","r",encoding="utf8")
# 操作文件
data = fp.read()
ls = data.split("\n")
# 关闭文件
fp.close()
cards = list()
for i in ls:
    new_ls = i.split(",")
    name = new_ls[0]
    tel = new_ls[1]
    company = new_ls[2]
    job = new_ls[3]
    address = new_ls[4]
    card = Card(name,tel,company,job,address)
    cards.append(card)
print(cards)
for i in cards:
    print(i.name)


