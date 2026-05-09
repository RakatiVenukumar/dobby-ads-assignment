# single inheritance

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
        # super().work()
        Human.work(male_1)
        
male_1 = Male('venu',21)
male_1.work()
print(male_1.num_eyes)

