n=int(input("Enter: "))
if n==2 or n==3 or n==5:
    print("Prime")
elif n%2==0 :
    print("not a prime")
elif n%3==0:
    print("not prime")
elif n%5==0:
    print("not prime")

else:
    print("prime")
