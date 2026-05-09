# heirarchical inheritance

class Human:
    def __init__(self,age):
        self.num_eyes = 2
        self.age = age
    def eat(self):
        print("i can eat")
    def work(self):
        print('i can code')
        
class Male(Human):
    def __init__(self,name,age):
        self.name = name
        super().__init__(age)
    def work(self):
        print("i can work")
        super().work()
        
class Female(Human):
    def sleep():
        print("i can sleep whole day")
    def __init__(self,name,age):
        self.name = name
        super().__init__(age)
    def work(self):
        print("i can work")
        super().work()
        
male_1 = Male('venu',21)
male_1.work()
female_1 = Female('venu',21)
female_1.work()
print(female_1.name)
print(male_1.name)
