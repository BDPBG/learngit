class Animal(object):
    def __init__(self, color):
        self.color = color #颜色
    def call(self):
        print("动物叫")
class Fish(Animal):
    def __init__(self, color):
        super().__init__(color)
        self.tail = True
    def call(self):
        print("-%s的鱼在吐泡泡-"%self.color)
fish = Fish("蓝色")
fish.call()