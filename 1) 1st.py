a=input()
print(a.upper())
for i in a:
    if i in ["a","e","i","o","u","A","E","I","O","U"]:
        print(i,end=",")
y=input()
if y in a:
    print(a.replace(y,''))