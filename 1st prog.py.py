a=eval(input("Enter the value :- "))
if a%2==0:
    print("Number is even")

else:
    print("Number is odd")


E=int(input("Enter marks for English "))
M=int(input("Enter marks for Maths "))
S=int(input("Enter marks for Science "))
P=int(input("Enter marks for Physics "))
sum=E+M+S+P
percentage=((sum/400)*100)
if percentage>80:
    print("Grade A")
if percentage>70 and percentage<80:
    print("Grade B")
else:
    print("fail")




