c=int(input("Enter Cost: "))
CGST=9/100*c
SGST=9/100*c
total=c+CGST+SGST
print("CGST on Products @9%: ",CGST)
print("SGST on Products @9%: ",SGST)
print("Total Cost is",total)