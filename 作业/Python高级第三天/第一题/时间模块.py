"""
time:
    基础模块,只能表示1970年-2038年
    time.time() 获取当前时间戳
    time.sleep(秒数) 让程序休眠指定的秒数
datetime:
    高级模块,可以表示0001-9999
    datetime类
        datetime(年,月,日) 创建时间对象
        datetime.now() 获取当前时间对象
        时间对象.strftime() 时间对象-->字符串
        datetime.strptime(转换格式) 字符串-->时间对象
    timedelta类
        时间跨度对象 = timedelta()
        时间跨度对象 = 时间对象 - 时间对象
"""
# 从时间模块导入time,sleep
from time import time, sleep

# 获取时间戳
print(time())
# 让程序休眠1秒
sleep(1)

# 从datetime导入datetime类和timedelta类
from datetime import datetime ,timedelta
# 创建datetime对象
time_1 = datetime(2021,5,10)
print(time_1)
# 创建当前时间对象
time_2 = datetime.now()
print(time_2)
# 时间对象-->字符串对象
st = time_2.strftime("%H-%M-%S %d-%m-%Y") # "%H:%M %Y/%m/%d"
print(st)
# 字符串-->时间对象
st1 = datetime.strptime("08:08:08 2021.08.08","%H:%M:%S %Y.%m.%d")
print(st1) # 2021-08-08 08:08:08
delta = time_2-time_1 # 时间跨度对象 = 时间对象-时间对象
print(delta)
print(type(delta)) # <class 'datetime.timedelta'>
# 创建一个时间跨度对象
delta1 = timedelta(99)
time_3 = time_2 + delta1 # 时间对象 = 时间对象+时间跨度对象
print(time_3)
print(type(time_3)) # <class 'datetime.datetime'>