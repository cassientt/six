# 字符串
# message = " this is a string."
# messages = ' this is also a string.'
# print(messages)
# print(message)
# print(type(message))

# 交叉使用
# messages2 = "I told my friend,'python 'is my favorite language!"
# print(messages2)
# messages3 = 'I told my friend,"python "is my favorite language!'
# print(messages3)
#
# messages4 = "I told my friend,python's my favorite language!"
# print(messages4)



# 修改字符串大小方法(方法是可对数据执行的操作)
# name = "nie tingting"
# 首字母大写
# print(name.title())
# name ='Nie Tingting'
# 全部大写
# print(name.upper())
# 全部小写
# print(name.lower())


# 在字符串中使用变量
#
# first_name = 'nie'
# last_name = 'tingting'
# full_name1 = f"{first_name} {last_name}"
# full_name = f"{first_name}{last_name}"
#
# print(full_name1)  # nie tingting
# print(full_name)  # nietingting
#
# print(f'hello {full_name1.title()}')  # hello Nie Tingting


# 使用制表符或换行符来添加空白

# print(" python ")
# print("\tpython")
# print("\npython")
# print("Languages:\npython\njava\nc")
#
# print("Languages:\n\tpython\n\tjava\n\tc")

# 删除空白

favorite_language = ' python '

print(favorite_language.rstrip())
