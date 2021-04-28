"""
    使用对象上的方法:
        对象.方法名()
        self不用自己传,python.exe的解释器会自动帮你传递
        我们只需要关注其余的形参即可
"""
class GirlFriend:
    age = 18
    name = "张三"

    def speak(self):
        print("么么哒")
gl = GirlFriend()
gl.speak()