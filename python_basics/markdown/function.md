### 8 函数
- 函数是带名字的代码块；
```python
def greeter_user():  # 函数定义，函数名，在圆括号内指出函数为完成任务需要什么样的信息；
    # 函数名为greet_user()，它不需要任何信息就能完成工作，因此括号是空的（即便如此，括号也必不可少）；
    # 定义以冒号结尾；

    # 所有缩进行构成了函数体
    """
    显示简单的问候语(文档字符串注释，指明函数功能)
    :return:
    """
    print('Hello world!')


if __name__ == '__main__':
    greeter_user()  # 函数调用让Python执行函数的代码;
```

####  8.1 向函数传递信息:形参和实参
```python
def greeter_user(username):  # username:形参（parameter）,即函数完成工作所需的信息
    """
    显示简单的问候语
    :return:
    """
    print(f'Hello {username.title()} ')


# if __name__ == '__main__':
greeter_user('cassie')  # cassie:实参（argument），即调用函数时传递给函数的信息
```
####  8.2 传递实参
#####  8.2.1 位置实参
```python
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
describe_pet('hamster', 'peer')
describe_pet('dog', 'tim')   # 实参的顺序与函数定义中形参的顺序一致
```
#####  8.2.2 关键字实参
- 关键字实参的顺序无关紧要，因为Python知道各个值该赋给哪个形参；
- 使用关键字实参时，务必准确指定函数定义中的形参名。
```python
def describe_pet(animal_type, animal_name):

    """
    描述动物的类型和名字
    :param animal_type:
    :param animal_name:
    :return:
    """
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {animal_name}.")



describe_pet(animal_type='hamster', animal_name='peer')
describe_pet(animal_name='tim', animal_type='dog',)
```
#####  8.2.3 默认值
- 使用默认值时，必须先在形参列表中列出没有默认值的形参，再列出有默认值的实参。
-  这让Python依然能够正确地解读位置实参;
```python
def describe_pet(pet_name, animal_type='dog'):
    """

    :param pet_name:
    :param animal_type:
    :return:
    """

    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}.")



describe_pet(pet_name='tom')  # 将使用形参的默认值,实参视为位置实参;
describe_pet(pet_name='jim', animal_type='fish')  # 在调用函数中给形参提供了实参时，Python将使用指定的实参值;
```
####  8.3 等效的函数调用
```python
def describe_pet(pet_name, animal_type='dog'):
    """

    :param pet_name:
    :param animal_type:
    :return:
    """

    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}.")


describe_pet("willie")
describe_pet(pet_name='willie')
describe_pet('harry', 'hamster')
describe_pet(animal_type='hamster', pet_name='harry')

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
```
####  8.4 避免实参错误
```python
def describe_pet(animal_type, animal_name):
    """
    描述动物的类型和名字
    :param animal_type:
    :param animal_name:
    :return:
    """
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {animal_name}.")



describe_pet()  # TypeError: describe_pet() missing 2 required positional arguments: 'animal_type' and 'animal_name'
```

####  8.5 返回简单值
- 函数返回的值称为返回值。在函数中，可使用return语句将值返回到调用函数的代码行;
```python
def get_formatted_name(first_name, last_name):
    """
    返回完整的名字
    :param first_name:
    :param last_name:
    :return:
    """
    full_name = f'{first_name} {last_name}'
    return full_name.title()


musician = get_formatted_name('tingting', 'nie')
print(musician)

```

####  8.6 让实参变成可选的
- 首先列出了这两个形参;
- 中间名是可选的，因此在函数定义中最后列出该形参，并将其默认值设置为空字符串;
```python
def get_formatted_name(first_name, last_name, middle_name=''):
    """
    返回完整的名字
    :param middle_name:
    :param first_name:
    :param last_name:
    :return:
    """
    if middle_name:
        full_name = f'{first_name} {middle_name} {last_name}'
    else:
        full_name = f'{first_name} {last_name}'

    return full_name.title()



musician = get_formatted_name('tingting', 'nie')
print(musician)
musician = get_formatted_name('tingting', 'xiao', 'nie')
print(musician)




```

####  8.7返回字典
```python
def get_formatted_name(first_name, last_name, middle_name=''):
    """
    返回完整的名字
    :param middle_name:
    :param first_name:
    :param last_name:
    :return:
    """
    if middle_name:
        full_name = f'{first_name} {middle_name} {last_name}'
    else:
        full_name = f'{first_name} {last_name}'
    person = {'first': first_name, 'last': last_name, 'middle': middle_name}

    return person



musician = get_formatted_name('tingting', 'nie')
print(musician)
musician = get_formatted_name('tingting', 'xiao', 'nie')
print(musician)

'''
{'first': 'tingting', 'last': 'nie', 'middle': ''}
{'first': 'tingting', 'last': 'xiao', 'middle': 'nie'}
'''



def get_formatted_name(first_name, last_name, age=None):


    person = {'first': first_name, 'last': last_name, }
    if age:
        person['age'] = age
    return person


musician = get_formatted_name('ting', 'nie', 27)
print(musician)
```

####  8.8 结合使用函数和while循环
```python
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

```

####  8.9 传递列表

```python
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
```

####  8.10 在函数中修改列表

```python
unprinted_designs = ['phone case', 'robot pendant', 'document']

completed_models = []

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f'Printing {current_design.title()}: ')
    completed_models.append(current_design)
print(f'The following models have been printed:')
for completed_model in completed_models:
    print(completed_model.title())

# 方法抽象为函数
def print_models(unprinted_design, completed_model):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f'Printing {current_design.title()}: ')
        completed_models.append(current_design)


def show_completed_models(completed_model):
    print(f'The following models have been printed:')
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['phone case', 'robot pendant', 'document']
completed_models = []

# print_models(unprinted_designs, completed_models)
print_models(unprinted_designs[:], completed_models)  
# 禁止函数修改列表

show_completed_models(completed_models)


```
####  8.11 传递任意数量的实参
```python
def make_pizza(*toppings):
    """
    打印顾客点的配料
    :param toppings:
    :return:
    """
    print(f'Making a pizza with the following toppings:')
    for topping in toppings:
        print(f'-{topping}')



make_pizza('pepperoni')
make_pizza('extra cheese', 'mushroom ')

```
 ####  8.12 结合使用位置实参和任意数量实参
````python
def make_pizza(size, *toppings):

    print(f'Making a {size} pizza with the following toppings:')
    for topping in toppings:
        print(f'-{topping}')



make_pizza(6, 'pepperoni')
make_pizza(7, 'extra cheese', 'mushroom ')

````
####  8.13 使用任意数量的关键字实参

```python
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('cassie', 'nie', locatoin='beijing', field='physics')
print(user_profile)

# {'locatoin': 'beijing', 'field': 'physics', 'first_name': 'cassie', 'last_name': 'nie'}
```

###  9 将函数存储在模块中
- 将函数存储在称为模块的独立文件中，再将模块导入到主程序中;
- import语句允许在当前运行的程序文件中使用模块中的代码;

```python
# 创建模块
def make_pizza(size, *toppings):

    print(f'Making a {size} pizza with the following toppings:')
    for topping in toppings:
        print(f'-{topping}')

        
# 导入刚创建的模块,并调用：        
        
from function import pizza
# model_name.function()
pizza.make_pizza(8, 'mushroom')

```

