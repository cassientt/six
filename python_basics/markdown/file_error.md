#### 10 从文件中读取数据

#####  10.1 读取文件
- 你只管打开文件，并在需要时使用它，Python自会在合适的时候自动将其关闭;
- Windows系统使用反斜杠（\）而不是斜杠（/），但在代码中依然可以使用斜杠;
- 对于路径"C:\path\to\file.txt"，其中的\t将被解读为制表符。
- 如果一定要使用反斜杠，可对路径中的每个反斜杠都进行转义，如"C:\\path\\to\\file.txt"。
````python
with open("../pi_digits.txt") as file_object:  # 使用相对路径获取
    content = file_object.read()
    print(content)
    print(len(content))
    print(len(content.rstrip()))


# 使用绝对路径
file_path = '/Users/cassie/six/python_basics/pi_digits.txt'

with open(file_path) as file_object:
    content = file_object.read()
    print(content)
# 逐行读取
file_name = "../pi_digits.txt"
with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())

````

#####  10.2 创建一个包含文件各行内容的列表
```python
file_name = "../pi_digits.txt"
with open(file_name) as file_object:
    lines = file_object.readlines() # 从文件中读取每一行，并将其存储在一个列表中;
for line in lines:
    print(line.rstrip())

```
#####  10.3 使用文件的内容
- 将文件读取到内存中后，就能以任何方式使用这些数据了;
```python
file_name = "../pi_digits.txt"
with open(file_name) as file_object:
    lines = file_object.readlines()
pi_strings = ""
for line in lines:
    pi_strings += line.strip()
print(pi_strings)
print(len(pi_strings))

"""
3.141592653589793238462643383279
32
"""
```

#####  10.4 写入空文件
- 打开文件时，可指定读取模式（'r'）、写入模式（'w'）、附加模式（'a'）或读写模式（'r+'）
-  如果省略了模式实参，Python将以默认的只读模式打开文件。
- 函数write()不会在写入的文本末尾添加换行符;
```python
# 覆盖写文件，写完会覆盖
filename = '../programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I also love finding meaning  large datasets.\n")
    file_object.write("I love creating apps that can run in a browsers.\n")


# 附加模式（'a'）
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning  large datasets.\n")
    file_object.write("I love creating apps that can run in a browsers.\n")
```
- Python只能将字符串写入文本文件。
- 要将数值数据存储到文本文件中，必须先使用函数str()将其转换为字符串格式

####  10.5 异常
- Python使用称为异常的特殊对象来管理程序执行期间发生的错误;
- 每当发生让Python不知所措的错误时，它都会创建一个异常对象。如果你编写了处理该异常的代码，程序将继续运行;
- 如果未对异常进行处理，程序将停止并显示traceback，其中包含有关异常的报告;
##### 10.5.1 处理ZeroDivisionError异常
```python
print(5/0)  # ZeroDivisionError: division by zero

try:
    print(5/0)  # 如果try代码块中的代码运行起来没有问题，Python将跳过except代码块;
except ZeroDivisionError:
    print("you can't divide by zero.")
```

##### 10.5.2 使用异常避免崩溃
```python
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)
# try-except-else代码块的工作原理大致如下:
"""
Python尝试执行try代码块中的代码，只有可能引发异常的代码才需要放在try语句中。
有时候，有一些仅在try代码块成功执行时才需要运行的代码，这些代码应放在else代码块中。
except代码块告诉Python，如果尝试运行try代码块中的代码时引发了指定的异常该怎么办.
"""
```

##### 10.5.3 处理FileNotFoundError异常 
```python
filename = '../alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        # 二是给参数encoding指定了值，在系统的默认编码与要读取文件使用的编码不一致时，必须这样做
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    # Count the approximate number of words in the file.
    words = contents.split()  # 方法split()以空格为分隔符将字符串分拆成多个部分，并将这些部分都存储到一个列表中
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")

```
##### 10.5.4 使用函数处理多个文件
```python
def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        # pass  # 静默失败
        print(f"Sorry,the file {filename} does not find")

    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)

```