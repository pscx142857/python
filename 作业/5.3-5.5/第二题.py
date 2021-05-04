"""
2. 编写一个接受句子的程序，并计算大写字母和小写字母的数量。
	输入提供给程序：Hello world!
	输出结果:
		大写字母 1
		小写字母 9
"""
def cn():
    """
    根据用户输入的话,打印出大写字母的个数和小写字母的个数
    :return:
    """
    # 让用户输入要说的话
    st = input("请输入你要说的话")
    # num用来小写字母计数
    num = 0
    # num2用来大写字母计数
    num2 = 0
    # 遍历字符串,分别判断是否是大小写的字母
    for i in st:
        if i.islower():
            num += 1
        elif i.isupper():
            num2 += 1
    # 将结果打印出来
    print(f"大写字母 {num2}")
    print(f"小写字母 {num}")
# 调用函数
cn()