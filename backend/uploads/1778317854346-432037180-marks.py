a = int(input("enter the marks of subject 1: "))
b = int(input("enter the marks of subject 2: "))
c = int(input("enter the marks of subject 3: "))

if(a<33 or b<33 or c<33):
    print("you have failed due to percentage less than 33% in any one of the subject")

elif((a+b+c)/3 < 40):
    print("you have failed due to total percentage less than 40%")

else:
    print("you have passed")              



        