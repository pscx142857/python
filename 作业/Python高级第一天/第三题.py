"""
3.使用模块化和面向对象的思想完成名片管理系统.
"""
# 导入文件管理系统模块
from package import filesys
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
    card = filesys.Card(name, tel, company, job, address)
    ls.append(card)
# 创建一个名片盒子类
cards = filesys.Cards(ls)
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