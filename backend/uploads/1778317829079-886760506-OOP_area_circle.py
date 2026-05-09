class Circle:
    # pi = 3.14
    def __init__(self,radius=5,pi = 3.14):
        self.r = radius
        self.pi = pi
    def values(self,circumference):
        circum = 2 * self.pi * self.r
        print(circum)
    def display(self,area):
        return self.pi * self.r ** 2
        
circle_1 = Circle()
circle_1.values('circum')
print(circle_1.display('area'))