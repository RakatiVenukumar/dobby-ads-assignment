class Add:
    def __init__(self,num1,num2):
        self.a = num1
        self.b = num2
    def result(self,sum):
        return self.a + self.b
     
add_1 = Add(4,3)    
print(add_1.result(sum))
# print(type(Add))