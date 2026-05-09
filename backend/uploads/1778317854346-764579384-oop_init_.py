# __init__ method:

class Instructor:
    def __init__(self,name,address):
        self.a = name   
        self.b = address
        
    def display(self,sport_name):
        print(f"Hi, i am {self.a} and I play {sport_name}")

instructor_1 = Instructor('venu','kukatpally')
print(instructor_1.a)    
instructor_1.display('cricket')