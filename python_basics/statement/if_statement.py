# cars = ['audi', 'bMw', 'subaru', 'toyota']
# for car in cars:
#     if car.lower() == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())

# # 检查是否不相等
#
# requested_topping = 'mushrooms'
# if requested_topping != 'anchovies':
#     print('hold the anchovies!')

# 数值比较
# age = 19
# if age != 42:
#     print('try again')
#
# if age < 21:
#     print('ture')
# if age <= 21:
#     print('true 2')
# if age >= 21:
#     print('false')
# if age > 21:
#     print('false 2')
# '''
# try again
# ture
# true 2
# '''

# 1．使用and检查多个条件
# age1 = 22
# age2 = 18
# if age1 >= 21 and age2 >= 21:
#     print('false')
# if age1 >= 21 and age2 >= 17:
#     print('true')

# # or
# age1 = 22
# age2 = 18
# if age1 >= 21 or age2 >= 21:
#     print('true')
# if age1 >= 22 or age2 >= 45:
#     print('false')

# 检查特定值是否包含在列表中

# cars = ['audi', 'bMw', 'subaru', 'toyota']
# user = 'cassie'
# if 'toyota' in cars:
#     print('true')
# if user not in cars:
#     print(f'{user.title()} not in cars,you can make')

# 根据年龄段收费的游乐场：❏ 4岁以下免费；❏ 4～18岁收费25美元；❏ 18岁（含）以上收费40美元。

# age = 17
#
# if age < 4:
#     print('your admission coast is $0.')
# elif age < 18:
#     print('your admission coast is $25.')
# else:
#     print('your admission coast is $40.')

# age = 30
#
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 25
# else:
#     price = 40
# print(f'your admission coast is {price}.')

# 使用更多elif
# age = 66
#
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 25
# elif age < 65:
#     price = 40
# else:
#     price = 20
# print(f'your admission coast is {price}.')

# 5.9 省略else代码块
# age = 3
#
# if age < 4:
#     price = 0
#
# elif age >= 65:
#     price = 40
#
# print(f'your admission coast is {price}.')

# 如果顾客点了两种配料，就需要确保在其比萨中包含这些配料：

# requested_toppings = ['mushroom', 'extra cheese']
# if 'mushroom' in requested_toppings:
#     print(f'adding mushroom.')
# if 'extra cheese' in requested_toppings:
#     print(f'adding extra cheese.')
# print('Taking your pizza.')


# requested_toppings = ['mushroom','green peppers', 'extra cheese']
#
# for requested_topping in requested_toppings:
#     if requested_topping == 'green peppers':
#         print('sorry,green peppers is gone')
#     print(f'adding {requested_topping}')
#
# print('Taking your pizza.')

# requested_toppings = []
# if requested_toppings: # 判断列表是否为空
#     for requested_topping in requested_toppings:
#         print(f'adding {requested_topping}')
#     print('Taking your pizza.')
# else:
#     print('Are you sure want a plain pizza.')


# 使用多个列表
available_topping = ['mushroom', 'green peppers', 'olives']
requested_toppings = ['mushroom', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_topping:
        print(f'adding {requested_topping}')
else:
    print(f"sorry,we don't have {requested_topping} ")

print('Taking your pizza.')