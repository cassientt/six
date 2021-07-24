def greeter_user(username):  # 函数定义，函数名，在圆括号内指出函数为完成任务需要什么样的信息；
    # 函数名为greet_user()，它不需要任何信息就能完成工作，因此括号是空的（即便如此，括号也必不可少）；
    # 定义以冒号结尾；

    # 所有缩进行构成了函数体
    """
    显示简单的问候语(文档字符串注释，指明函数功能)
    :return:
    """
    print(f'Hello {username.title()} ')


# if __name__ == '__main__':
greeter_user('cassie')  # 函数调用让Python执行函数的代码;