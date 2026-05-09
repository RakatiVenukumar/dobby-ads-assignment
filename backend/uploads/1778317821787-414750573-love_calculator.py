# love calculator 

name1 = input("enter your name :")
name2 = input("enter her name :")
a = name1 + name2
lower_case_string = a.lower()

t = lower_case_string.count('t')
r = lower_case_string.count('r')
u = lower_case_string.count('u')
e = lower_case_string.count('e')

true = t + r + u + e

l = lower_case_string.count('l')
o = lower_case_string.count('o')
v = lower_case_string.count('v')
e = lower_case_string.count('e')

love = l + o + v + e

love_score = int(str(true) + str(love))

if (love_score < 10 or love_score > 90):
    print(f"your love score is {love_score} and your relationship is not so good ")
elif ( love_score >= 40 and love_score <= 50):
    print(f"your love score is {love_score} and you both are alright ")
else:
    print(f"your love socre is {love_score} ")
    
