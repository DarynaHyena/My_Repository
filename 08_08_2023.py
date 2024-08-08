from random import randint
class Randomizer ():
    def __init__(self, begin_num, end_num):
        self.begin_num = begin_num
        self.end_num = end_num
    def generate (self, begin_num, end_num):
        print(randint(begin_num, end_num))

a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
obj1 = Randomizer(a, b)
obj1.generate(a, b)