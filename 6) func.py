def countB(b,c):
    a=0
    for i in b:
        
        if i==c:
            a+=1
        else:
            continue
    return a

b=input()
c=input()
print(countB(b,c))
            

            