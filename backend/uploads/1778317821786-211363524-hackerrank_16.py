n = 15
for i in range(1,n+1):
    print(i, oct(i)[2:], hex(i)[2:].upper(), bin(i)[2:])
    
# w = len(bin(number)[2:])
    
#     for i in range(1, number+1):
#         d = str(i)
#         o = oct(i)[2:]
#         h = hex(i)[2:].upper()
#         b = bin(i)[2:]
        
#         print(d.rjust(w), o.rjust(w), h.rjust(w), b.rjust(w))