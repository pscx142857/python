"""
3. 编写一个程序，以给定的数字作为a的值来计算a + aa + aaa + aaaa的值。
	假设将以下输入提供给程序：9
	输出结果为:11106
"""
def calculate(num):
    """
    根据输入的a计算a+aa+aaa+aaaa
    :param num: 传入的数字
    :return:
    """
    # 转成字符串类型
    a = str(num)
    # 计算a+aa+aaa+aaaa
    count = int(a)+int(a*2)+int(a*3)+int(a*4)
    print(count)
# 传入实参调用函数
calculate(9)