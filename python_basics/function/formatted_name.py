# def get_formatted_name(first_name, last_name):
#     """
#     返回完整的名字
#     :param first_name:
#     :param last_name:
#     :return:
#     """
#     full_name = f'{first_name} {last_name}'
#     return full_name.title()
#
#
# musician = get_formatted_name('tingting', 'nie')
# print(musician)


# def get_formatted_name(first_name, last_name, middle_name=''):
#     """
#     返回完整的名字
#     :param middle_name:
#     :param first_name:
#     :param last_name:
#     :return:
#     """
#     if middle_name:
#         full_name = f'{first_name} {middle_name} {last_name}'
#     else:
#         full_name = f'{first_name} {last_name}'
#
#     return full_name.title()
#
#
#
# musician = get_formatted_name('tingting', 'nie')
# print(musician)
# musician = get_formatted_name('tingting', 'xiao', 'nie')
# print(musician)
#


# def get_formatted_name(first_name, last_name, middle_name=''):
#     """
#     返回完整的名字
#     :param middle_name:
#     :param first_name:
#     :param last_name:
#     :return:
#     """
#     if middle_name:
#         full_name = f'{first_name} {middle_name} {last_name}'
#     else:
#         full_name = f'{first_name} {last_name}'
#     person = {'first': first_name, 'last': last_name, 'middle': middle_name}
#
#     return person
#
#
#
# musician = get_formatted_name('tingting', 'nie')
# print(musician)
# musician = get_formatted_name('tingting', 'xiao', 'nie')
# print(musician)

'''
{'first': 'tingting', 'last': 'nie', 'middle': ''}
{'first': 'tingting', 'last': 'xiao', 'middle': 'nie'}
'''


# def get_formatted_name(first_name, last_name, age=None):
#
#
#     person = {'first': first_name, 'last': last_name, }
#     if age:
#         person['age'] = age
#     return person
#
#
# musician = get_formatted_name('ting', 'nie', 27)
# print(musician)


def get_formatted_name(first_name, last_name):
    full_name = f'{first_name} {last_name}'
    return full_name.title()


while True:
    print("Please tell you name :")
    print("(Enter 'q' to quite at anytime)")
    f_name = input('first_name: ')
    if f_name == 'q':
        break
    l_name = input('last_name: ')
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"Hello,{formatted_name}")
