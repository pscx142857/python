# 导入随机数模块
import random
# 导入GUI模块
from tkinter import *
# 定义列表数据
ls = ["顾客/会员","商品展示","购买流程","商品管理"]
# 随机选择函数
def choise():
     res = random.choice(ls)
     ft = f"恭喜{inp1.get()}被 {res} 模块砸中了!!!\n"
     txt.insert(END, ft)   # 追加显示结果
     inp1.delete(0, END)  # 清空输入
     ls.remove(res)

# 绘制主窗口
root = Tk()
root.geometry('520x320')
root.title('听天由命')
# 文本显示
lb1 = Label(root, text='请输入姓名选择模块:')
lb1.place(relx=0.1, rely=0.1, relwidth=0.25, relheight=0.1)
# 输入框
inp1 = Entry(root)
inp1.place(relx=0.38, rely=0.1, relwidth=0.4, relheight=0.1)

# 确定按钮,方法-直接调用 choise()
btn1 = Button(root, text='确定', command=choise)
btn1.place(relx=0.3, rely=0.4, relwidth=0.3, relheight=0.1)


# 在窗体垂直自上而下位置60%处起，布局相对窗体高度40%高的文本框
txt = Text(root,font=("黑体",20))
txt.place(rely=0.6, relheight=0.4)

root.mainloop()