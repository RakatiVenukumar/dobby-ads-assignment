a = input().split(" ")
a = list(map(int,a))
print(a)
if len(a)>=2:
    max = 0
    for i in range(0,len(a)):
        if a[i] > max:
            max = a[i]
    print(max)
    a.remove(max)
    print(a)

    max = 0
    for i in range(0,len(a)):
        if a[i] > max:
            max = a[i]
    print(f"The second largest number is {max}")

elif len(a) < 2:
    print("No second largest number")