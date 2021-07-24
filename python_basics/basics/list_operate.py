# 遍历整个列表
# magicians = ['alice', 'cassie', 'peery']
# for magician in magicians:
#     # print(magician)
#     # 在for循环中执行更多操作
#     print(f'{magician} is a great people,')
#     print(f"I can't wait to see {magician}.")
# # 在for循环结束后执行一些操作
# print(f'thank your everyone.')


# 创建数值列表
# for value in range(1, 5):
#     print(value)

# 也可只指定一个参数n，这样它将从0开始，到n-1结束
# 指定2个参数，这样它将从left开始,到right-1结束

# 使用函数range()时，还可指定步长
# even_numbers = list(range(2, 11, 2))
# print(even_numbers)  # [2, 4, 6, 8, 10]
#
#
# squares = []
# for i in range(1, 11):
#     squares.append(i**2)
# print(squares)

# 对数字列表执行简单的统计计算
# digits = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# print(min(digits))
# print(max(digits))
# print(sum(digits))

# 列表解析 ：减少代码繁复
# squares = [value ** 2 for value in range(1, 11)]
# print(squares)
# 使用列表的一部分：切片

# players = ['charles', 'martina', 'even', 'cassie', 'peery']
# print(players[0:3])  # ['charles', 'martina', 'even']
# print(players[1:4])  # ['martina', 'even', 'cassie']
# print(players[:4])  # ['charles', 'martina', 'even', 'cassie']  从列表开头开始
# print(players[2:])  # ['even', 'cassie', 'peery']  要让切片终止于列表末尾
# print(players[-3:]) # ['even', 'cassie', 'peery'] 负数索引返回离列表末尾相应距离的元素


# players = ['charles', 'martina', 'even', 'cassie', 'peery']
#
# print('Here are the first three player on my team:')
# for player in players[0:3]:
#     print(player.title())
#
#
# """
# Here are the first three player on my team:
# Charles
# Martina
# Even
#
# """

# 4.4.3 复制列表
# 使用切片复制列表
#
# my_foods = ['pizza', 'falafel', 'cake']
# friend_foods = my_foods[:]
#
# my_foods.append('cannoli')
# friend_foods.append('ice cream')
# print('my favorite foods: ')
# print(my_foods)
# print("my friend's favorite foods: ")
# print(friend_foods)

"""
my favorite foods: 
['pizza', 'falafel', 'cake', 'cannoli']
my friend's favorite foods: 
['pizza', 'falafel', 'cake', 'ice cream']


"""

# 不使用切片复制列表
my_foods = ['pizza', 'falafel', 'cake']
friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print('my favorite foods: ')
print(my_foods)
print("my friend's favorite foods: ")
print(friend_foods)

"""
my favorite foods: 
['pizza', 'falafel', 'cake', 'cannoli', 'ice cream']
my friend's favorite foods: 
['pizza', 'falafel', 'cake', 'cannoli', 'ice cream']
"""