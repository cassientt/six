# names = ["cassie", 1, 'tom']
# print(names)
# # 让Python将列表打印出来，Python将打印列表的内部表示
# # 访问列表元素(便于用户观察)
# print(names[0])  # 索引从0而不是1开始,要访问列表的任何元素，都可将其位置减1，并将结果作为索引
# print(names[0].title())
#
# print(names[-1])  # 知道列表长度的情况下访问最后的元素,或倒数第2（-2）

# 使用列表中的各个值
# messages = f'My first name is  {names[0]}'
#
# print(messages)

# 要修改列表元素
# names[0] = 'ntt cassie'
# print(names)


# 在列表中添加元素：添加在尾部,常用建空列表收集数据；
# names.append('perry')
# print(names)  # ['cassie', 1, 'tom', 'perry']
# # 在列表中插入
# names.insert(0, 'dandan')
# print(names)  # ['dandan', 'cassie', 1, 'tom']
# # 从列表中删除元素
# del names[1]
# print(names)  # ['cassie', 'tom']

# pop()
# education_experience = ['primary school', 'senior high school', 'university']

# print(f'My highest degree is {education_experience.pop()}')
# # My highest degree is university
#
# # 弹出列表中任何位置处的元素
#
# print(f'my first education is {education_experience.pop(0)};')  # my first education is primary school;


# 你不知道要从列表中删除的值所处的位置可使用 remove() 。 使用remove()从列表中删除元素时，也可接着使用它的值
# course = ['python', 'C', 'Java']
# print(course)
# easy = 'python'
# course.remove(easy)
# print(course)
# print(f'{easy} is easy for me.')


# sort() 对列表永久排序
# cars = ['bmt', 'atm', 'yui']
# cars.sort()  # 按字母顺序顺序排列
# print(cars)  # ['atm', 'bmt', 'yui']
# cars.sort(reverse=True)  # 字母顺序相反的顺序排列
# print(cars)  # ['yui', 'bmt', 'atm']
# sorted()对列表临时排序
# cars = ['bmt', 'atm', 'yui']
# print('没有排序')
# print(cars)
#
# print('排序后')
# print(sorted(cars))
#
# print('再次打印')
# print(cars)

'''
没有排序
['bmt', 'atm', 'yui']
排序后
['atm', 'bmt', 'yui']
再次打印
['bmt', 'atm', 'yui']
'''

cars = ['bmt', 'atm', 'yui']
cars.reverse()
print(cars)  # ['yui', 'atm', 'bmt']

print(len(cars))