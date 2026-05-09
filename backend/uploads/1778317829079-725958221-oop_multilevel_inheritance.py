# multilevel inheritance

class Human:
    def __init__(self,age):
        self.num_eyes = 2
        self.age = age
    def eat(self):
        print("i can eat")
    def work(self):
        print("i can code")

class Male(Human):
    def __init__(self,name):
        self.name = name
    def sleep(self):
        print("i can sleep whole day")
    def work(self):
        print("i can test")
        super().work()
        
class Female(Male):
    def __init__(self,age,name,section):
        Human.__init__(self,age)
        Male.__init__(self,name)
        self.section = section
    def work(self):
        print("i can work")
        super().work()
        
female_1 = Female(21,'venu','B')
print(female_1.num_eyes)
print(female_1.name)
print(female_1.section)