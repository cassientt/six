
# with open("../pi_digits.txt") as file_object:  # 使用相对路径获取
#     content = file_object.read()
#     print(content)
#     print(len(content))
#     print(len(content.rstrip()))
#     print(content.rstrip())
#
#
# # 使用绝对路径
# file_path = '/Users/cassie/six/python_basics/pi_digits.txt'
#
# with open(file_path) as file_object:
#     content = file_object.read()
#     print(content.rstrip())
    # print(content)


# file_name = "../pi_digits.txt"
# with open(file_name) as file_object:
#     lines = file_object.readlines()
# pi_strings = ""
# for line in lines:
#     pi_strings += line.strip()
# print(pi_strings)
# print(len(pi_strings))

"""
3.141592653589793238462643383279
32
"""

# 覆盖写文件，写完会覆盖
filename = '../programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I also love finding meaning  large datasets.\n")
    file_object.write("I love creating apps that can run in a browsers.\n")


# 附加模式（'a'）
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning  large datasets.\n")
    file_object.write("I love creating apps that can run in a browsers.\n")