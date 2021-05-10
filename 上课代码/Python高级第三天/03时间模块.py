"""
时间戳: 英国的格林威志 1970年1月1日 00:00:00 到现在的一个秒数
时区:一共24个时区 中国:东区 --> +8:00

time 基础模块:只能表示1970年--2037年
    import time

    time.time() # 获取当前时间戳
    time.sleep(秒数)  # 让程序休眠指定的秒数

datetime 高级模块:0001-9999
"""

# 导入时间模块
import time

print(time.time()) # 获取当前时间戳
time.sleep(2) # 延迟两秒执行
print(time.time())

from datetime import datetime

# 创建指定时间对象
time_obj = datetime(2021,5,21)
print(time_obj)

# 获取当前时间对象
time_now = datetime.now()
print(time_now)

res = time.strftime("%H:%M %Y/%m/%d") # 时间对象装成字符串
print(res)
print(type(res))

time_1 = datetime.strptime("2021-01-05 12:30:01","%Y-%m-%d %H:%M:%S") # 字符串转成时间对象
print(time_1)
print(time_1.second)
print(time_1.year)

# 导入时间跨度类
from datetime import timedelta
# 创建一个指定日期时间对象
time1 = datetime(2021,6,14)
# 创建当前时间对象
time2 = datetime.now()
# 两个时间对象相减,得到一个时间跨度对象
print(time1 - time2) # 34 days, 9:39:54.270065

# 创建一个时间跨度对象
time3 = timedelta(100)
# 计算一百天后的日期
print(time2 + time3) # 2021-08-18 14:21:30.872988 ,时间跨度对象+时间对象=时间对象