# 子类的方法__init__()
# class Car:
#     """一次模拟汽车的简单尝试"""
#
#     def __init__(self, make, model, year):  # 4个形参
#         """初始化描述汽车的属性"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0  # 给属性指定默认值
#
#     def get_descriptive_name(self):
#         """返回整洁的描述信息"""
#         long_name = f"{self.make} {self.model} {self.year}"
#         return long_name.title()
#
#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it")
#
#     def update_odometer(self, mileage):
#
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer")
#
#     def increment_odometer(self, miles):
#         self.odometer_reading += miles
#
#
# class ElectricCar(Car):  # 在圆括号内指定父类的名称
#     """电动汽车的独特之处"""
#
#     def __init__(self, make, model, year):  # 方法__init__()接受创建Car实例所需的信息
#         """初始化父类属性"""
#         super().__init__(make, model, year)   # 处的super()是一个特殊函数，让你能够调用父类的方法,父类也称为超类（superclass）
#
#
# my_tesla = ElectricCar("tesla", "models", 2019)
# print(my_tesla.get_descriptive_name())

'''
Tesla Models 2019
'''

# 给子类定义属性和方法

#
# class Car:
#     """一次模拟汽车的简单尝试"""
#
#     def __init__(self, make, model, year):  # 4个形参
#         """初始化描述汽车的属性"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0  # 给属性指定默认值
#
#     def get_descriptive_name(self):
#         """返回整洁的描述信息"""
#         long_name = f"{self.make} {self.model} {self.year}"
#         return long_name.title()
#
#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it")
#
#     def update_odometer(self, mileage):
#
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer")
#
#     def increment_odometer(self, miles):
#         self.odometer_reading += miles
#
#
# class ElectricCar(Car):  # 在圆括号内指定父类的名称
#     """电动汽车的独特之处"""
#
#     def __init__(self, make, model, year):  # 方法__init__()接受创建Car实例所需的信息
#         """
#         初始化父类属性
#         再初始化电动汽车特有属性
#         :param make:
#         :param model:
#         :param year:
#
#         """
#         super().__init__(make, model, year)   # 处的super()是一个特殊函数，让你能够调用父类的方法,父类也称为超类（superclass）
#         self.battery_size = 75
#
#     def describe_battery(self):
#         print(f"This car has a {self.battery_size} Kwh battery")
#
#
#
#
# my_tesla = ElectricCar("tesla", "models", 2019)
# print(my_tesla.get_descriptive_name())
# my_tesla.describe_battery()


#  重写父类的方法
#
# class Car:
#     """一次模拟汽车的简单尝试"""
#
#     def __init__(self, make, model, year):  # 4个形参
#         """初始化描述汽车的属性"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0  # 给属性指定默认值
#         self.gas_tank = 0
#
#     def get_descriptive_name(self):
#         """返回整洁的描述信息"""
#         long_name = f"{self.make} {self.model} {self.year}"
#         return long_name.title()
#
#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it")
#
#     def update_odometer(self, mileage):
#
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer")
#
#     def increment_odometer(self, miles):
#         self.odometer_reading += miles
#
#     def fill_gas_tank(self):
#         print(f"This car don't need a gas tank {self.gas_tank}")
#
#
#
# class ElectricCar(Car):  # 在圆括号内指定父类的名称
#     """电动汽车的独特之处"""
#
#     def __init__(self, make, model, year):  # 方法__init__()接受创建Car实例所需的信息
#         """
#         初始化父类属性
#         再初始化电动汽车特有属性
#         :param make:
#         :param model:
#         :param year:
#
#         """
#         super().__init__(make, model, year)   # 处的super()是一个特殊函数，让你能够调用父类的方法,父类也称为超类（superclass）
#         self.battery_size = 75
#
#     def describe_battery(self):
#         print(f"This car has a {self.battery_size} Kwh battery")
#
#     def fill_gas_tank(self):
#         print("This car don't need gas tank")
#
#
#
#
# my_tesla = ElectricCar("tesla", "models", 2019)
# print(my_tesla.get_descriptive_name())
# my_tesla.describe_battery()
# my_tesla.fill_gas_tank()

"""
Tesla Models 2019
This car has a 75 Kwh battery
This car don't need gas tank
"""


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
        self.battery = Battery()


my_tesla = ElectricCar("tesla", "models", 209)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()

'''
Tesla Models 209
This car has a 75 Kwh battery
'''