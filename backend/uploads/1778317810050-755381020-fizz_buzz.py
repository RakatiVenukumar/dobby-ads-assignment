#fizzbuzz

num = range(1,101)
for i in num:
    if(i%3==0 and i%5==0):
        num ='fizzbuzz'
        print(num)
    elif(i%3==0):
        num = 'fizz'
        print(num)
    elif(i%5==0):
        num ='buzz'
        print(num)
    else:
        print(i)  