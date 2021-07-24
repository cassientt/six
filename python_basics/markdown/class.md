### 9 类
- 在面向对象编程中，你编写表示现实世界中的事物和情景的类，并基于这些类来创建对象；
- 根据类来创建对象称为**实例化**；

####  9.1 创建Dog类
```python
class Dog:   # 首字母大写的名称指的是类。这个类定义中没有圆括号，因为要从空白创建这个类
    """"一次模拟小狗的简单尝试"""   # 文档字符串

    def __init__(self, name, age):   # 每当你根据Dog类创建新实例时，Python都会自动运行它
        """
        初始化属性name和age
        :param name:
        :param age:
        """
        self.name = name  # 以self为前缀的变量可供类中的所有方法使用，可以通过类的任何实例来访问
        self.age = age

    def sit(self):
        """模拟小狗收到命令时蹲下"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """模拟小狗收到命令时打滚"""
        print(f"{self.name} rolled over. ")


my_dog = Dog('willie', 6)  # 实例化类
print(f"My dog is {my_dog.name}.")  # my_dog.name:访问属性
print(f"My dog is {my_dog.age}.")

# 调用方法
my_dog.sit()
my_dog.roll_over()


'''
My dog is willie.
My dog is 6.
willie is now sitting.
willie rolled over. 
'''

```
####  9.2 使用类和实例，以及给属性指定默认值

```python
# 使用类和实例，以及给属性指定默认值

class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):  # 4个形参
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # 给属性指定默认值

    def get_descriptive_name(self):
        """返回整洁的描述信息"""
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")




my_new_car = Car("audi", "a4", 2019)  # 根据类创建实例
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

"""
Audi A4 2019
This car has 0 miles on it
"""


```
####  9.3  修改属性的值
#####   9.3.1直接修改属性的值:通过实例直接访问它
```python
class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):  # 4个形参
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # 给属性指定默认值

    def get_descriptive_name(self):
        """返回整洁的描述信息"""
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")




my_new_car = Car("audi", "a4", 2019)  # 根据类创建实例
my_new_car.odometer_reading = 23   # 通过实例直接访问它
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
```

#####   9.3.2 通过方法修改属性的值
```python
class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):  # 4个形参
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # 给属性指定默认值

    def get_descriptive_name(self):
        """返回整洁的描述信息"""
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):

        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")



my_new_car = Car("audi", "a4", 2019)  # 根据类创建实例
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()

"""
Audi A4 2019
This car has 23 miles on it
"""
```

#####   9.3.3 通过方法对属性的值进行递增
```python
class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):  # 4个形参
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # 给属性指定默认值

    def get_descriptive_name(self):
        """返回整洁的描述信息"""
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):

        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")

    def increment_odometer(self, miles):
        self.odometer_reading += miles




my_new_car = Car("audi", "a4", 2019)  # 根据类创建实例
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23_00)
my_new_car.increment_odometer(100)
my_new_car.read_odometer()

"""
Audi A4 2019
This car has 2400 miles on it
"""
```