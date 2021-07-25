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
 ####  9.4继承
- 如果要编写的类是另一个现成类的特殊版本，可使用继承;
- 一个类继承另一个类时，将自动获得另一个类的所有属性和方法。原有的类称为父类，而新类称为子类;
- 子类继承了父类的所有属性和方法，同时还可以定义自己的属性和方法;
#####   9.4.1 子类的方法__init__()
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


class ElectricCar(Car):  # 在圆括号内指定父类的名称
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):  # 方法__init__()接受创建Car实例所需的信息
        """初始化父类属性"""
        super().__init__(make, model, year)   # 处的super()是一个特殊函数，让你能够调用父类的方法,父类也称为超类（superclass）


my_tesla = ElectricCar("tesla", "models", 2019)
print(my_tesla.get_descriptive_name())

'''
Tesla Models 2019
'''
```
#####   9.4.2 给子类定义属性和方法
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


class ElectricCar(Car):  # 在圆括号内指定父类的名称
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):  # 方法__init__()接受创建Car实例所需的信息
        """
        初始化父类属性
        再初始化电动汽车特有属性
        :param make:
        :param model:
        :param year:

        """
        super().__init__(make, model, year)   # 处的super()是一个特殊函数，让你能够调用父类的方法,父类也称为超类（superclass）
        self.battery_size = 75

    def describe_battery(self):
        print(f"This car has a {self.battery_size} Kwh battery")




my_tesla = ElectricCar("tesla", "models", 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
```

#####   9.4.3 重写父类的方法
- 对于父类的方法，只要它不符合子类模拟的实物的行为，都可以进行重写;
- 不会考虑这个父类方法，而只关注你在子类中定义的相应方法;

```python
#  重写父类的方法

class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):  # 4个形参
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # 给属性指定默认值
        self.gas_tank = 0

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

    def fill_gas_tank(self):
        print(f"This car don't need a gas tank {self.gas_tank}")



class ElectricCar(Car):  # 在圆括号内指定父类的名称
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):  # 方法__init__()接受创建Car实例所需的信息
        """
        初始化父类属性
        再初始化电动汽车特有属性
        :param make:
        :param model:
        :param year:

        """
        super().__init__(make, model, year)   # 处的super()是一个特殊函数，让你能够调用父类的方法,父类也称为超类（superclass）
        self.battery_size = 75

    def describe_battery(self):
        print(f"This car has a {self.battery_size} Kwh battery")

    def fill_gas_tank(self):
        print("This car don't need gas tank")




my_tesla = ElectricCar("tesla", "models", 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()

"""
Tesla Models 2019
This car has a 75 Kwh battery
This car don't need gas tank
"""
```


#####   9.4.4 将实例用作属性

```python
class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):  # 4个形参
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # 给属性指定默认值
        self.gas_tank = 0

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

    def fill_gas_tank(self):
        print(f"This car don't need a gas tank {self.gas_tank}")


class Battery:
    """
    模拟电动汽车电瓶的简单尝试
    """

    def __init__(self, battery_size=75):
        """初始化电瓶属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size} Kwh battery")


class ElectricCar(Car):  # 在圆括号内指定父类的名称
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):  # 方法__init__()接受创建Car实例所需的信息
        """
        初始化父类属性
        再初始化电动汽车特有属性
        :param make:
        :param model:
        :param year:

        """
        super().__init__(make, model, year)  # 处的super()是一个特殊函数，让你能够调用父类的方法,父类也称为超类（superclass）
        self.battery = Battery()  #添加了一个名为self.battery的属性


my_tesla = ElectricCar("tesla", "models", 209)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()

'''
Tesla Models 209
This car has a 75 Kwh battery
'''
```
####   9.5 导入类
- 应让文件尽可能整洁;
- 允许将类存储在模块中（文件夹），然后在主程序中导入所需的模块;
#####    9.5.1 导入单个类
#####    9.5.2 在一个模块中存储多个类(类同级)
#####    9.5.3 从一个模块中导入多个类,用逗号分隔了各个类；
#####    9.5.4 导入整个模块
- 使用语法module_name.ClassName访问需要的类，进行实例化；
#####    9.5.4  导入模块中的所有类(不推荐使用)
- 语法： from module_name import *  
#####    9.5.5 在一个模块中导入另一个模块（比如父类）
- 以免模块太大或在同一个模块中存储不相关的类；
- 将类存储在多个模块中时，你可能会发现一个模块中的类依赖于另一个模块中的类；
- 在这种情况下，可在前一个模块中导入必要的类；

#####    9.5.6 使用别名
- 多次调用书写复杂的类，可以如；

- from electric_car import ElectricCar as EC

