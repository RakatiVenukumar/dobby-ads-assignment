def convert(n):
    
    if n == '0':
        print('zero',end = ' ')
    elif n == '1':
        print('one',end = ' ')
    elif n == '2':
        print("two",end = ' ')
    elif n == '3':
        print("three",end = ' ')
    elif n == '4': 
        print("four",end = ' ')
    elif n == '5':
        print("five",end = ' ')
    elif n == '6':
        print("six",end = ' ')
    elif n == '7':
        print("seven",end = ' ')
    elif n == '8':
        print("eight",end = ' ')
    elif n == '9':
        print("nine",end = ' ')
        
def PrintWord(N):
    for i in range(len(N)):
        convert(N[i])
    # i = 0
    # length = len(N)
    # while i < length:
    #     convert(N[i])
    #     i = i + 1


N = input()
PrintWord(N)
        



