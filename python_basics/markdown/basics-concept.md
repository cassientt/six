### 1 起步
####  设置代码格式  Python EnhancementProposal,PEP
```shell
PEP8
1. 缩进:每级缩进都使用四个空格/tab制表符;
2. 行长:建议每行不超过80字符;注释的行长不应超过72字符;
3. 不要在程序文件中过多使用空行;
4. 诸如==、>=和<=等比较运算符两边各添加一个空格;


```

#### 1.1 解释器及退出
Python自带一个在终端窗口中运行的解释器，提示符>>>表明正在使用终端窗口，而加粗的文本表示需要你输入之后按回车键来执行的代码。

#### 1.2 解释器执行函数

```
．py指出这是一个Python程序，因此编辑器将使用Python解释器来运行它。
Python解释器读取整个程序，确定其中每个单词的含义 

1. 直接到对应存储代码的位置执行
cd six
cd python_basics
python hello_python.py


2. 使用绝对路径   /(root开头绝对路径)
python /Users/cassie/six/python_basics/hello_python.py  

3. 使用相对路径   ../(相对路径)
python ./six/python_basics/hello_python.py 

cd cd Developer/demo 
python ../../six/python_basics/hello_python.py
```
#### 1.3 python 文件夹和文件夹名字命名规范

- 最好使用小写字母，并使用下划线代替空格；

### 2 变量和简单数据类型
- 变量是可以赋给值的标签，也可以说变量指向特定的值。
- 每个变量都指向一个值——与该变量相关联的信息
- 在程序中可随时修改变量的值，而Python将始终记录变量的最新值.
#### 2.1 变量的命名和使用
1. 变量名只能包含字母、数字和下划线;
1. 变量名能以字母或下划线打头，但不能以数字打头;
1. 变量名不能包含空格，但能使用下划线来分隔其中的单词;
1. 不要将Python关键字和函数名用作变量名;
1. 变量名应既简短又具有描述性;
1. 慎用小写字母l和大写字母O，因为它们可能被人错看成数字1和0;

> 应使用小写的Python变量名。虽然在变量名中使用大写字母不会导致错误，但是大写字母在变量名中有特殊含义.
#### 2.2 字符串
- 用引号括起的都是字符串，其中的引号可以是单引号，也可以是双引号;
> 注意：不可重复使用，引号是按对读取的。

#### 2.3 字符串方法
```
方法是Python可对数据执行的操作。
在name.title()中，name后面的句点（.）让Python对变量name执行方法title()指定的操作。
每个方法后面都跟着一对圆括号，这是因为方法通常需要额外的信息来完成其工作。
这种信息是在圆括号内提供的。函数title()不需要额外的信息，因此它后面的圆括号是空的。
```
#### 2.4  在字符串中使用变量

```python
first_name = 'nie'
last_name = 'tingting'
full_name1 = f"{first_name} {last_name}"
full_name = f"{first_name}{last_name}"

print(full_name1)  # nie tingting
print(full_name)  # nietingting

print(f'hello {full_name1.title()}')  # hello Nie Tingting

# f字符串是Python 3.6引入的

```
#### 2.5 使用制表符或换行符来添加空白
- 在字符串中添加制表符:\t,换行符:\n,空白：空格

 #### 2.6 删除空白
- 这些剥除函数最常用于在存储用户输入前对其进行清理;
```shell

>>> favorite = ' python '
>>> favorite
' python '
>>> favorite.rstrip()
' python'
>>> favorite.lstrip()
'python '
>>> favorite.strip()
'python'
>>> 

```
#### 2.7 数
- 空格不影响Python计算表达式的方式。4/2它们的存在旨在让你在阅读代码时能迅速确定先执行哪些运算
```shell
>>> 2 + 3
5
>>> 2 * 3
6

>>> 3 / 2
1.5
# 求模运算符将两个数相除并返回余数：如可被整除则为0
>>> 3 % 2
1
>>> 2 ** 3
8
```
#### 2.8 整数和浮点数
- 将任意两个数相除时，结果总是浮点数，即便这两个数都是整数且能整除;
- 无论是哪种运算，只要有操作数是浮点数，Python默认得到的总是浮点数，即便结果原本为整数也是如此
```shell
>>> 4/2
2.0
>>> 1 + 2.0
3.0
>>> 2 * 3.0
6.0
>>> 

```
#### 2.9 数中的下划线
- 书写很大的数时，可使用下划线将其中的数字分组;(Python 3.6和更高的版本支持)
```shell
>>> price = 14_000_00_0
>>> price
14000000
>>> name = 0.3_000
>>> name
0.3
>>> 

```

#### 2.10 同时给多个变量赋值
```shell
>>> x,y ,z = 1,2,3
>>> x
1
>>> z
3
```

#### 2.11 常量
- 常量类似于变量，但其值在程序的整个生命周期内保持不变;
- Python没有内置的常量类型;
- 在代码中，要指出应将特定的变量视为常量，可将其字母全部大写;

### 3 列表简介
#### 3.1 列表概念
- 列表由一系列按特定顺序排列的元素组； 
- 用方括号（[]）表示列表，并用逗号分隔其中的元素；
- 可以创建包含字母表中所有字母、数字0～9或所有家庭成员姓名的列表；
### 3.2 访问列表元素
- 列表是有序集合，因此要访问列表的任意元素，只需将该元素的位置（索引）；
- 索引从0而不是1开始,要访问列表的任何元素，都可将其位置减1，并将结果作为索引;

### 3.2  使用列表中的各个值
```python
names = ["cassie", 1, 'tom']
messages = f'My first name is  {names[0]}'
print(messages)  # My first name is  cassie

```
### 3.3  修改、添加和删除元素
- 要修改列表元素，可指定列表名和要修改的元素的索引，再指定该元素的新值;
### 3.4 在列表中添加元素
```python
# 要修改列表元素
names = ["cassie", 1, 'tom']
names[0] = 'ntt cassie'
print(names) # ['ntt cassie', 1, 'tom']
 

# 在列表中添加元素：添加在尾部,常用建空列表收集数据；
names.append('perry')
print(names)  # ['cassie', 1, 'tom', 'perry']
# 在列表中插入
names.insert(0, 'dandan')
print(names)  # ['dandan', 'cassie', 1, 'tom']
# 从列表中删除元素
del names[1]
print(names)  # ['cassie', 'tom']

```
### 3.5 使用方法pop()删除元素
- 列表就像一个栈，而删除列表末尾的元素相当于弹出栈顶元素;
````python
# 入学是按时间存储的，就可使用方法pop()打印一条消息，指出最后学校
education_experience = ['primary school', 'senior high school', 'university']

print(f'My highest degree is {education_experience.pop()}')
# My highest degree is university

# 弹出列表中任何位置处的元素

print(f'my first education is {education_experience.pop(0)};')  # my first education is primary school;
````
> 每当你使用pop()时，被弹出的元素就不再在列表中了
> 你不确定该使用del语句还是pop()方法,下面是一个简单的判断标准：如果你要从列表中删除一个元素，且不再以任何方式使用它，就使用del语句；如果你要在删除元素后还能继续使用它，就使用方法pop()。

### 3.6 根据值删除元素remove()  
- 不知道要从列表中删除的值所处的位置; 
-   使用remove()从列表中删除元素时，也可接着使用它的值

```python

course = ['python', 'C', 'Java']
print(course)
easy = 'python'
course.remove(easy)
print(course)
print(f'{easy} is easy for me.')
"""
['python', 'C', 'Java']
['C', 'Java']
python is easy for me.
"""
```
### 3.7 组织列表:使用方法sort()对列表永久排序
```python
# sort() 对列表永久排序
cars = ['bmt', 'atm', 'yui']
cars.sort()  # 按字母顺序顺序排列
print(cars)  # ['atm', 'bmt', 'yui']
cars.sort(reverse=True)  # 字母顺序相反的顺序排列
print(cars) # ['yui', 'bmt', 'atm']
```

 ### 3.8 使用函数sorted()对列表临时排序
```python
# sorted()对列表临时排序
cars = ['bmt', 'atm', 'yui']
print('没有排序')
print(cars)

print('排序后')
print(sorted(cars))

print('再次打印')
print(cars)

'''
没有排序
['bmt', 'atm', 'yui']
排序后
['atm', 'bmt', 'yui']
再次打印
['bmt', 'atm', 'yui']
'''
```
### 3.8 倒着打印列表:反转列表元素的排列顺序
```python
cars = ['bmt', 'atm', 'yui']
cars.reverse()
print(cars)  # ['yui', 'atm', 'bmt']

```

### 3.9 确定列表的长度
- 使用函数len()可快速获悉列表的长度,Python计算列表元素数时从1开始


### 3.10  使用列表时避免索引错误


### 4 列表操作 
####  4.1  遍历整个列表(可通过debug，打断点，看程序的执行顺序)
```python
magicians = ['alice', 'cassie', 'peery']
for magician in magicians:
    # print(magician)
    # 在for循环中执行更多操作
    print(f'{magician} is a great people,')
    print(f"I can't wait to see {magician}.")
# 在for循环结束后执行一些操作
print(f'thank your everyone.')

```
常见错误：
1. 遗漏了冒号;
1. 循环后不必要的缩进；
1. 忘记缩进；
####  4.2 创建数值列表
```python
# 创建数值列表
for value in range(1, 5):
    print(value)

# 也可只指定一个参数n，这样它将从0开始，到n-1结束
# 指定2个参数，这样它将从left开始,到right-1结束

# 使用函数range()时，还可指定步长
even_numbers = list(range(2, 11, 2))
print(even_numbers)  # [2, 4, 6, 8, 10]


squares = []
for i in range(1, 11):
    squares.append(i**2)
print(squares)

# 对数字列表执行简单的统计计算
digits = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(min(digits))
print(max(digits))
print(sum(digits))

# 列表解析 ：减少代码繁复
squares = [value ** 2 for value in range(1, 11)]
print(squares)

```

####  4.3 使用列表的一部分：切片
- 要创建切片，可指定要使用的第一个元素和最后一个元素的索引；
- 与函数range()一样，Python在到达第二个索引之前的元素后停止；
```python
players = ['charles', 'martina', 'even', 'cassie', 'peery']
print(players[0:3])  # ['charles', 'martina', 'even']
print(players[1:4])  # ['martina', 'even', 'cassie']
print(players[:4])  # ['charles', 'martina', 'even', 'cassie']  从列表开头开始
print(players[2:])  # ['even', 'cassie', 'peery']  要让切片终止于列表末尾
print(players[-3:]) # ['even', 'cassie', 'peery'] 负数索引返回离列表末尾相应距离的元素
# 备注：可在表示切片的方括号内指定第三个值。这个值告诉Python在指定范围内每隔多少元素提取一个。


# 取出前三位

players = ['charles', 'martina', 'even', 'cassie', 'peery']

print('Here are the first three player on my team:')
for player in players[0:3]:
    print(player.title())


"""
Here are the first three player on my team:
Charles
Martina
Even

"""

```

####  4.4 复制列表 
```python
# 使用切片复制列表

my_foods = ['pizza', 'falafel', 'cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')
print('my favorite foods: ')
print(my_foods)
print("my friend's favorite foods: ")
print(friend_foods)

"""
my favorite foods: 
['pizza', 'falafel', 'cake', 'cannoli']
my friend's favorite foods: 
['pizza', 'falafel', 'cake', 'ice cream']


"""

# 不使用切片复制列表

my_foods = ['pizza', 'falafel', 'cake']
friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print('my favorite foods: ')
print(my_foods)
print("my friend's favorite foods: ")
print(friend_foods)

"""
my favorite foods: 
['pizza', 'falafel', 'cake', 'cannoli', 'ice cream']
my friend's favorite foods: 
['pizza', 'falafel', 'cake', 'cannoli', 'ice cream']
"""


```

### 5 元组
####  5.1 元组与列表区别
- 列表非常适合用于存储在程序运行期间可能变化的数据集；
- 列表是可以修改的；
- Python将不能修改的值称为不可变的，而不可变的列表被称为元组
####  5.2 元组概念
- 但使用圆括号而非中括号来标识；
- 可使用索引来访问其元素，就像访问列表元素一样；
```python
dimensions = (220, 50)
print(dimensions[0])  # 220

dimensions[0] = 250  # TypeError: 'tuple' object does not support item assignment
print(dimensions)

# 元组是由逗号标识的,如果你要定义只包含一个元素的元组，必须在这个元素后面加上逗号;
a = (3)    #去掉多余的括弧  Remove redundant parentheses

b = 4
c = (5,)

# 遍历元组
dimensions = (5, 6, 7)
for i in dimensions:
    print(i)


```

####  5.3修改元组变量
- 虽然不能修改元组的元素，但可以给存储元组的变量赋值;
```python
dimensions = (220, 50)
for dimension in dimensions:
    print(dimension)
dimensions = (400, 100)
for dimension in dimensions:
    print(dimension)

```
### 6 字典
- 字典是一系列键值对;
- 每个键都与一个值相关联，你可使用键来访问相关联的值;
- 与键相关联的值可以是数、字符串、列表乃至字典;可将任何Python对象用作字典中的值
- 键和值之间用冒号分隔，而键值对之间用逗号分隔;
  
####  6.1一个简单的字典
```python
alien = {'color': 'green', 'point': 5}
print(alien['color'])
print(alien['point'])

# 访问字典中的值

alien = {'color': 'green', 'point': 5}
new_point = alien['point']
print(f'Now you will get {new_point}.')
```
####  6.2 添加键值对
```python
# 添加键值对
alien = {'color': 'green', 'point': 5} 
# This dictionary creation could be rewritten as a dictionary literal
alien['x_position'] = 0
alien['y_position'] = 20
print(alien)

```
####  6.3 先创建一个空字典
```python

alien = {}
alien['color'] = 'green'
alien['point'] = 50
print(alien)
```
####  6.4 修改字典中的值
```python

alien = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"alien origin position is {alien['x_position']}")

if alien['speed'] == 'slow':
    x_increment = 1
elif alien['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien['x_position'] = alien['x_position'] + x_increment
print(f"alien now location is {alien['x_position']}")
```
####  6.4 删除键值对 
```python
alien = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}

del alien['speed']
print(alien)  # {'x_position': 0, 'y_position': 25}
# 删除的键值对会永远消失
```

####  6.5由类似对象组成的字典
```python

favorite_languages = {
    'cassie': 'python',
    'peer': 'js',
    'tom': 'java',
}
language = favorite_languages['cassie'].title()
print(f"Cassie favorite language is {language}")  
# Cassie favorite language is Python
```

####  6.6使用get()来访问值
- 调用get()时，如果没有指定第二个参数且指定的键不存在，Python将返回值None,有是第二个值；
```python
alien = {'x_position': 0, 'y_position': 25}
# speed = alien['speed'] # KeyError: 'speed'
speed = alien.get('speed', 'no value')
print(speed)  # no value

```
####  6.7 遍历字典
- 可遍历字典的所有键值对，也可仅遍历键或值；
 
```python

# 遍历所有键值对
alien = {
    'x_position': 0,
    'y_position': 25,
    'speed': 'medium',
}

for key, value in alien.items():
    print(f'\nkey:{key}')
    print(f'value:{value}')

'''
key:x_position
value:0

key:y_position
value:25

key:speed
value:medium
'''

# 遍历字典中的所有键

favorite_languages = {
    'cassie': 'python',
    'peer': 'js',
    'tom': 'java',
}
friends = ['cassie', 'peer']

for name in favorite_languages.keys():
    print(f'hi ,{name.title()}')
    if name in friends:
        language = favorite_languages[name].title()
        print(f'\t{name.title()},I see you love {language}')
        
'''
hi ,Cassie
        Cassie,I see you love Python
hi ,Peer
        Peer,I see you love Js
hi ,Tom
'''

# 按特定顺序遍历字典中的所有键
favorite_languages = {
    'tom': 'java',
    'cassie': 'python',
    'peer': 'js',

}

for name in sorted(favorite_languages.keys()):
    print(f'{name}')


# 按特定顺序遍历字典中的所有不同值
favorite_languages = {
    'tom': 'java',
    'cassie': 'python',
    'peer': 'js',
    'dan': 'python'

}
for language in set(favorite_languages.values()):
    print(language.title())
```


####  6.8嵌套
 ```python
# 列表中存储字典
aliens = []

# 创建30个外星人
for alien_number in range(30):
    new_aliens = {'color': 'green', 'point': 5, 'speed': 'slow'}
    aliens.append(new_aliens)
for alien in aliens[:5]:
    print(alien)

print(f'Total alien is {len(aliens)}')


# 在字典中存储列表

pizza = {
    'crust': 'thick',
    'toppings': ['mushroom', 'extra cheese']
}

print(f"you ordered a pizza {pizza['crust']}-thick,with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping}")



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
```


###  7 集合
- 可使用一对花括号直接创建集合，并在其中用逗号分隔元素
```python
favorite_languages = {'java', 'python', 'js', 'python'}
print(type(favorite_languages))  # <class 'set'>
```

