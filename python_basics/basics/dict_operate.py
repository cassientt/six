# dict
# alien = {'color': 'green', 'point': 5}
# new_point = alien['point']
# print(f'Now you will get {new_point}.')


# 添加键值对
# alien = {'color': 'green', 'point': 5}
# # This dictionary creation could be rewritten as a dictionary literal
# alien['x_position'] = 0
# alien['y_position'] = 20
# print(alien)

# 先创建一个空字典
# alien = {}
# alien['color'] = 'green'
# alien['point'] = 50
# print(alien)

# # 修改字典中的值
# alien = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# print(f"alien origin position is {alien['x_position']}")
#
# if alien['speed'] == 'slow':
#     x_increment = 1
# elif alien['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3
# alien['x_position'] = alien['x_position'] + x_increment
# print(f"alien now location is {alien['x_position']}")


# alien = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
#
# del alien['speed']
# print(alien)  # {'x_position': 0, 'y_position': 25}



# # 类似对象组成的字典
# favorite_languages = {
#     'cassie': 'python',
#     'peer': 'js',
#     'tom': 'java',
# }
# language = favorite_languages['cassie'].title()
# print(f"Cassie favorite language is {language}")  # Cassie favorite language is Python
#
# alien = {'x_position': 0, 'y_position': 25}
# # speed = alien['speed'] # KeyError: 'speed'
# speed = alien.get('speed', 'no value')
# print(speed)  # no value

# alien = {
#     'x_position': 0,
#     'y_position': 25,
#     'speed': 'medium',
# }
#
# for key, value in alien.items():
#     print(f'\nkey:{key}')
#     print(f'value:{value}')

'''
key:x_position
value:0

key:y_position
value:25

key:speed
value:medium
'''

# 遍历字典中的所有键

# favorite_languages = {
#     'cassie': 'python',
#     'peer': 'js',
#     'tom': 'java',
# }
# friends = ['cassie', 'peer']
#
# for name in favorite_languages.keys():
#     print(f'hi ,{name.title()}')
#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f'\t{name.title()},I see you love {language}')

'''
hi ,Cassie
        Cassie,I see you love Python
hi ,Peer
        Peer,I see you love Js
hi ,Tom
'''

# 按特定顺序遍历字典中的所有键
# favorite_languages = {
#     'tom': 'java',
#     'cassie': 'python',
#     'peer': 'js',
#
# }
#
# for name in sorted(favorite_languages.keys()):
#     print(f'{name}')
#
# 按特定顺序遍历字典中的所有不同键
# favorite_languages = {
#     'tom': 'java',
#     'cassie': 'python',
#     'peer': 'js',
#     'dan': 'python'
#
# }
# for language in set(favorite_languages.values()):
#     print(language.title())


# favorite_languages = {'java', 'python', 'js', 'python'}
# print(type(favorite_languages))  # <class 'set'>


# 在列表中存储字典
# aliens = []
#
# # 创建30个外星人
# for alien_number in range(30):
#     new_aliens = {'color': 'green', 'point': 5, 'speed': 'slow'}
#     aliens.append(new_aliens)
# for alien in aliens[:5]:
#     print(alien)
#
# print(f'Total alien is {len(aliens)}')

# 在字典中存储列表

# pizza = {
#     'crust': 'thick',
#     'toppings': ['mushroom', 'extra cheese']
# }
#
# print(f"you ordered a pizza {pizza['crust']}-thick,with the following toppings:")
# for topping in pizza['toppings']:
#     print(f"\t{topping}")


# 在字典中存储字典


users = {
    'cassie': {
        'favorite': 'play',
        'location': 'china',
        'age': 18,

    },
    'peer': {
        'favorite': 'work',
        'location': 'china',
        'age': 19,

    }
}

for username, userinfo in users.items():
    print(f'{username}\n {userinfo}')
