n,m = input().split()
n=int(n)
m=int(m)
c=".|."
k=1
for i in range(n//2):
    print((c*k).center(m,'-'))
    k=k+2
k=k-2
print('WELCOME'.center(m,'-'))
for i in range(n//2):
    print((c*k).center(m,'-'))
    k=k-2