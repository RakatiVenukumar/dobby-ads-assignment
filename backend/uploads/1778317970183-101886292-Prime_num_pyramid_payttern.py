# prime numbers left pyramid pattern

count = 2
for i in range(4):
    for j in range(i+1):
        while True:
            is_prime = True
            if count <= 1:
                is_prime = False
            for k in range(2,count):  # for k in range(2,int(count ** 0.5)+ 1)
                if count % k == 0:
                    is_prime = False
                    break
            if is_prime:
                print(count,end = " ")
                count += 1
                break
            count += 1
print()