'''
Write a Python program to input marks of five subjects Physics, Chemistry, Biology,
Mathematics and Computer.Calculate percentage and grade according to following:
Percentage >= 90% : Grade A
Percentage >= 80% : Grade B
Percentage >= 70% : Grade C
Percentage >= 60% : Grade D
Percentage >= 40% : Grade E
Percentage < 40% : Grade F
'''

phy=float(input("Enter the marks of Physics:"))
math=float(input("Enter the marks of Mathematics:"))
chem=float(input("Enter the marks of Chemistry:"))
bio=float(input("Enter the marks of Biology:"))
comp=float(input("Enter the marks of Computer:"))
obt_marks=phy+math+chem+bio+comp
P=(obt_marks/500)*100
print('The percentage is',P)
if(P>=90):
    print ("Grade A")
elif(P>=80):
    print ("Grade B")
elif(P>=70):
    print ("Grade C")
elif(P>=60):
    print ("Grade D")
elif(P>=40):
    print ("Grade E")
else:
    print ("Grade F")
