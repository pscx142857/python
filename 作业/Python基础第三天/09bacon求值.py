'''
    对接下来的3个问题，假定bacon包含列表[3.14, 'cat', 11, 'cat', True]
    1) bacon.index('cat')求值为多少？
    2) bacon.append(99)让bacon中的列表值变成什么样？
	3) bacon.remove('cat')让bacon中的列表值变成什么样？
'''
bacon = [3.14, 'cat', 11, 'cat', True]
print(bacon.index('cat')) # 1
bacon.append(99)
print(bacon) # [3.14, 'cat', 11, 'cat', True, 99]
bacon.remove('cat')
print(bacon) # [3.14, 11, 'cat', True, 99]
