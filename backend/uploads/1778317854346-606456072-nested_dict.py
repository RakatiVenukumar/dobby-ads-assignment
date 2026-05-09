# nested dictionaries

def add_details(name,roll_no,age):
   list1 = [
        {           
          'name':name,
          'roll_no':roll_no,
          'age':age
        }
           ]
   return list1

data = [ 
        { 
         'name':'venu',
         'roll_no':1,
         'age':20
        },
        {
          'name':'girish',
         'roll_no':2,
         'age':21
        }
        ]

a = add_details('sravya',3,21)
b = add_details('deepu',4,21)
data = data + a + b
print(data)

