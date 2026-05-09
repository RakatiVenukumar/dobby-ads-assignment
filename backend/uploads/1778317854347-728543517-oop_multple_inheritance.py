# multiple inheritance

class Mother:
    def __init__(self,age):
        self.num_eyes = 2
        self.age = age
    def eat(self):
        print("i can eat")
    def work(self):
        print("i can code")

class Father:
    def __init__(self,name):
        self.name = name
    def sleep(self):
        print("i can sleep whole day")
    def work(self):
        print("i can test")
        
class Boy(Mother,Father):
    def __init__(self,name,age,section):
        Father.__init__(self,name)
        Mother.__init__(self,age)
        self.section = section
    def work(self):
        print("i can work")
        super().work()

boy_1 = Boy('venu',21,'B')
print(boy_1.num_eyes)
print(boy_1.name)
print(boy_1.section)