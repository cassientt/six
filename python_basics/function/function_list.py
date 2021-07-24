def greet_users(names):
    """
    问候列表中的每一个人
    :param names:
    :return:
    """
    for name in names:
        msg = f'hello, {name.title()}!'
        print(msg)



usernames = ['cassie', 'tim', 'jim']
greet_users(usernames)