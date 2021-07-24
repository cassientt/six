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