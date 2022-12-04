e=float(input("Enter marks for english :"))
m=float(input("Enter marks for maths :"))
s=float(input("Enter marks for chemistry :"))
p=float(input("Enter marks for physics :"))
q=float(input("Enter marks for computer :"))
sum=e+m+s+p+q
print("Sum of marks is :",sum)
per=sum/500
percent=per*100
print("percentage is :",percent)
if percent==90 :
    print("Grade A")
elif percent>=80 and percent<90:
    print("Grade B")
elif percent>=70 and percent<80:
    print("Grade C")
elif percent>=60 and percent<70:
    print("Grade D")
elif percent>=50 and percent<60:
    print("Grade E")
else:
    print("Fail")