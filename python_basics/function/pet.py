def describe_pet(animal_type, animal_name):
    # Triple double-quoted strings should be used for docstrings.
    """
    描述动物的类型和名字
    :param animal_type:
    :param animal_name:
    :return:
    """
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {animal_name}.")


# 多次调用函数
describe_pet()  # TypeError: describe_pet() missing 2 required positional arguments: 'animal_type' and 'animal_name'
# describe_pet('dog', 'tim')   # 实参的顺序与函数定义中形参的顺序一致


# 关键字实参


# def describe_pet(animal_type, animal_name):
#
#     """
#     描述动物的类型和名字
#     :param animal_type:
#     :param animal_name:
#     :return:
#     """
#     print(f"I have a {animal_type}.")
#     print(f"My {animal_type}'s name is {animal_name}.")
#
#
#
# describe_pet(animal_type='hamster', animal_name='peer')
# describe_pet(animal_name='tim', animal_type='dog',)

# 默认值

# def describe_pet(pet_name, animal_type='dog'):
#     """
#
#     :param pet_name:
#     :param animal_type:
#     :return:
#     """
#
#     print(f"I have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name}.")
#
#
#
# describe_pet(pet_name='tom')  # 将使用形参的默认值,实参视为位置实参;
# describe_pet(pet_name='jim', animal_type='fish')  # 在调用函数中给形参提供了实参时，Python将使用指定的实参值;

# 8.3 等效的函数调用
# def describe_pet(pet_name, animal_type='dog'):
#     """
#
#     :param pet_name:
#     :param animal_type:
#     :return:
#     """
#
#     print(f"I have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name}.")
#
#
# describe_pet("willie")
# describe_pet(pet_name='willie')
# describe_pet('harry', 'hamster')
# describe_pet(animal_type='hamster', pet_name='harry')

'''
I have a dog.
My dog's name is willie.
I have a dog.
My dog's name is willie.
I have a hamster.
My hamster's name is harry.
I have a hamster.
My hamster's name is harry.
'''