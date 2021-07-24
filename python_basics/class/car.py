# 使用类和实例，以及给属性指定默认值
# 修改属性的值
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
#
#
#
# my_new_car = Car("audi", "a4", 2019)  # 根据类创建实例
# my_new_car.odometer_reading = 23   # 通过实例直接访问它
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()


# 通过方法修改属性的值

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




# 通过方法对属性的值进行递增