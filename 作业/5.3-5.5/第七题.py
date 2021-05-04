"""
7. 编写一个选课系统,要求使用面向对象的方式编写（可以先使用函数实现在修改成面向对象的形式）。
	一共有以下学科可以选择：数学、英语、语文、化学、地理、生物、政治。
	功能：
	1.添加，根据学生姓名，给学生添加一个选择的学科，一个同学可以选择多个学科
	2.修改，根据学生姓名，修改学生选择的学科
	3.删除，根据学生姓名，删除学生选择的学科
	4.查询指定学生选择的学科，根据学生信息，查询到某个学生选择的所有学科
	5.根据学科名字，查询选择这个学科的学生有哪些
"""
# 保存数据函数
def save(ss):
    """
    传入一个选科对象,可以把学生的姓名和对应选的科保存到data.txt文件中
    :param ss: 选科对象
    :return:
    """
    # 打开文件
    fp = open("data.txt","w",encoding="utf8")
    # 操作文件
    for stu in ss.students:
        st1 = stu.name
        try:
            ls = stu.subjects
            ls.insert(0,st1)
            st2 = ",".join(ls)
            ls.pop(0)
        except AttributeError:
            fp.write(st1+"\n")
            print("异常:AttributeError")
        else:
            fp.write(st2+"\n")
    # 关闭文件
    fp.close()
# 定义一个学生类,属性有name,姓名,subjects,学科
class Student(object):
    # 初始化方法,创建对象的时候执行,添加属性name,subjects
    def __init__(self,name,subjects):
        self.name = name
        self.subjects = subjects
    # 打印对象时执行
    def __str__(self):
        return f"{self.name}\t\t{self.subjects}"
# 定义一个选科类
class SelectSubject(object):
    # 初始化方法,创建对象的时候执行,添加students属性
    def __init__(self,students):
        self.students = students
    # 添加
    def add(self):
        """
        根据学生姓名,添加选的科
        :return:
        """
        name = input("请输入学生姓名:")
        for stu in self.students:
            if stu.name == name:
                subject = input("请输入要添加的学科:")
                stu.subjects.append(subject)
                # 调用保存函数
                save(self)
                print("恭喜你添加成功")
                break
        else:
            print("对不起,没有找到此人")
    # 修改
    def reverse(self):
        """
        根据学生姓名,修改选的科
        :return:
        """
        name = input("请输入学生姓名:")
        for stu in self.students:
            if stu.name == name:
                subjects = input("请输入修改后的学科,以\",\"号隔开:")
                stu.subjects = subjects.split(",")
                # 调用保存函数
                save(self)
                print("恭喜你修改成功")
                break
        else:
            print("对不起,没有找到此人")
    # 删除
    def delete(self):
        """
        根据学生姓名,删除选的科
        :return:
        """
        name = input("请输入学生姓名:")
        for stu in self.students:
            if stu.name == name:
                del stu.subjects
                # 调用保存函数
                save(self)
                print("恭喜你删除成功")
                break
        else:
            print("对不起,没有找到此人")
    # 根据学生姓名,查询该学生所有的学科
    def show(self):
        """
        根据学生姓名,查询学生选的科
        :return:
        """
        name = input("请输入学生姓名:")
        for stu in self.students:
            if stu.name == name:
                try:
                    # 表头
                    print(f"{name}的学科有:", end="")
                    for v in stu.subjects:
                        print(f"{v}\t\t",end="")
                except AttributeError:
                    print(f"{name}没有选科")
                    break
                else:
                    print()
                    print("所有数据展示完毕")
                    break
        else:
            print("对不起,没有找到此人")
    # 根据学科查询有哪些学生
    def showname(self):
        """
        根据学科,展示学生姓名
        :return:
        """
        subject = input("请输入学科:")
        print(f"选择{subject}的人有:",end="")
        for stu in self.students:
            if subject in stu.subjects:
                print(f"{stu.name}\t\t", end="")
        print()
        print("所有数据展示完毕")
# 准备数据,读取data.txt文件,创建Student对象
students = list()  # 定义一个列表,用来装学生对象
# 打开文件
fp = open("data.txt","r",encoding="utf8")
# 操作文件
data = fp.read()
ls = data.strip("\n").split("\n")
for i in ls:
    ls1 = i.split(",")
    ls2 = ls1[1::]
    # 实例化学生对象
    stu = Student(ls1[0],ls2)
    students.append(stu)
# 关闭文件
fp.close()
# 创建一个选科对象
ss = SelectSubject(students)
# 主程序,死循环,一直执行
while True:
    # 让用户选择对应的功能
    st = input("输入数字选择你需要的功能(1-添加 2-修改 3-删除 4-查询学科 5-查询学生 6-退出):")
    # 调用添加方法
    if st == "1":
        ss.add()
    # 调用修改方法
    elif st == "2":
        ss.reverse()
    # 调用删除方法
    elif st == "3":
        ss.delete()
    # 调用查询学科方法
    elif st == "4":
        ss.show()
    # 调用查询学生姓名方法
    elif st == "5":
        ss.showname()
    # 退出系统
    elif st == "6":
        exit("退出系统")
    else:
        print("对不起,输入错误,请重新输入")