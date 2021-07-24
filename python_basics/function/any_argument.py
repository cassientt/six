# def make_pizza(*toppings):
#     """
#     打印顾客点的配料
#     :param toppings:
#     :return:
#     """
#     print(f'Making a pizza with the following toppings:')
#     for topping in toppings:
#         print(f'-{topping}')
#
#
#
# make_pizza('pepperoni')
# make_pizza('extra cheese', 'mushroom ')



# def make_pizza(size, *toppings):
#
#     print(f'Making a {size} pizza with the following toppings:')
#     for topping in toppings:
#         print(f'-{topping}')
#
#
#
# make_pizza(6, 'pepperoni')
# make_pizza(7, 'extra cheese', 'mushroom ')



def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('cassie', 'nie', locatoin='beijing', field='physics')
print(user_profile)