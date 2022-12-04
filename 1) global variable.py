# function:
# local and global Variable

p=20   #global variable
def num():
    q=10
    print("the value of q",q)
    print("the value of p",p)
num()
print("the value of p",p)

p=20
def sum():
    q=10
    print("the value of q",q)
    print("the value of p",p)
sum()
print("the value of p",p)