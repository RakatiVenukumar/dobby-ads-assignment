#local and global scope

a = 10  # global scope
def show():
    a = 15   # local scope
    print(a)
show()
print(a)
