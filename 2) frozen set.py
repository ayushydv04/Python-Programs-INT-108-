d={}
print(d)
k=list(input("keys: ").split(","))
v=list(map(int,input("values: ").split(",")))
d=dict(zip(k,v))
print(d)
a=list(input().split(","))
d[a[0]]=int(a[1])
print(d)