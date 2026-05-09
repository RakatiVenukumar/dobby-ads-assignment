a = [1,2,3,4,5]
squares = list(map((lambda x: x**2),a))
print(squares)

add = lambda a,b: a+b
print(add(23,12))

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  

data = [(1, 'one'), (2, 'two'), (3, 'three')]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data) 

