students = int(input("enter the number of students: "))
subjects = int(input("enter no of subjects: "))

marks_1= input(" marks of subject1: ")
marks_2 = input("marks of subject2: ")
marks_3 = input("marks of subject3: ")

a = marks_1.split(",")
b = marks_2.split(",")
c = marks_3.split(",")

d = " ".join(map(str,a))
print(d)

e = " ".join(map(str,b))
print(e)

f = " ".join(map(str,c))
print(f)

i = 0
while i < len(a) and i < len(b) and i < len(c):
    add_1 = (int(a[i])+int(b[i])+int(c[i]))
    add_2 = (add_1/3)
    i = i+1
    print(round(add_2,1))