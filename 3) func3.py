def fact(num):
    factorial=1
    for i in range(1,num+1):
        factorial=factorial*i
    print("the factorial of",num,"is",factorial)
fact(6)
