# function: basic building block of statements that perform a special task

# sum of numbers from 1 to 25, 50 to 70, 90 to 100


def sum(x,y):
    s=0
    for i in range(x,y+1):    #for i in range (1, 26)
        s=s+i                 #s=s+i --> s=0+1
    print("sum of integers:",s)
sum(1,25)
sum(50,75)
sum(90,100)
