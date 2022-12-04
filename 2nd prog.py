E=int(input("Enter marks for English "))
M=int(input("Enter marks for Maths "))
S=int(input("Enter marks for Science "))
P=int(input("Enter marks for Physics "))
C=int(input("Enter marks for Computer Science "))
sum=E+M+S+P+C
percentage=((sum/500)*100)
print("Percentage is ",percentage)

if percentage > 90:
    print("Grade A")

elif percentage>80 and percentage<90:
    print("Grade B")

elif percentage>70 and percentage<80:
    print("Grade C")

elif percentage>60 and percentage<70:
    print("Grade D")

elif percentage>60 and percentage<50:
    print("Grade E")

else:
    print("fail")
