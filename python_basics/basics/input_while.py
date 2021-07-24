# message = input('Tell me something ,and I will repeat it back to you:  ')
#
# print(f"Hello {message}")
# print(type(message))
# age = input('how old are you:')
# print(age + 1)  # TypeError: must be str, not int
#
# print(int(age) + 1)

# number = input('Input a number ,I will tell you even or odd: ')
# number = int(number)
# if number % 2 == 0:
#     print(f' {number} is even.')
# else:
#     print(f' {number} is odd.')



# while
# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     # current_number += 1
#     current_number = current_number + 1

# prompt = '\n Tell me something,I will repeat it back to you: '
# prompt += '\n Enter "quit" to end  the program.'
#
# message = ''
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)
# 使用标志


# prompt = '\n Tell me something,I will repeat it back to you: '
# prompt += '\n Enter "quit" to end  the program.'
#
# active = True
# while active:
#     message = input(prompt)
#     if message == 'quit':
#         active = False
#     else:
#         print(message)
#

# break
#
# prompt = '\n Please enter a city,you have visited:  '
# prompt += '\n Enter "quit" when you are finished.'
#
# while True:
#     city = input(prompt)
#     if city == 'quit':
#         break
#     else:
#         print(f"I'd love to go to {city.title()}.")
# 在循环中使用continue

# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#     print(current_number)


# x = 1
# while x < 5:
#     print(x)
# control + C :KeyboardInterrupt
# 确认程序至少有一个这样的地方能让循环条件为False，或者让break语句得以执行;


# 使用while循环处理列表和字典

# unconfirmed_user = ['cassie', 'peer', 'tom']
# confirmed_users = []
# while unconfirmed_user:
#     current_user = unconfirmed_user.pop()
#     print(f"Verifying user:{current_user.title()}")
#     confirmed_users.append(current_user)
# print("The following users have been confirmed")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())
# 删除为特定值的所有列表元素

# unconfirmed_users = ['cassie', 'peer','cassie', 'tom','cassie']
# print(unconfirmed_users)
# while 'cassie' in unconfirmed_users:
#     unconfirmed_users.remove('cassie')
# print(unconfirmed_users)


# 使用用户输入来填充字典


mountain_responses = {}

polling_active = True
while polling_active:
    name = input("\n what's you name? ")
    response = input("\n which mountain would you like to climb someday?")
    mountain_responses[name] = response
    repeat = input("would you like to let another person respond? (yes/no)")
    if repeat == 'no':
        polling_active = False
print("-----polling end -----")
for name,response in mountain_responses.items():
    print(f"{name} would like to climb {response}.")