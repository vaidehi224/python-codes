x=int(input("Enter the 1st number:"))
y=int(input("Enter the 2nd number:"))
if(x>y):
    small=y
else:
    small=x
for i in range(1,small+1):
    if(x%i==0 and y%i==0):
        hcf=i
print("THe HCF of %d and %d is %d "%(x,y,hcf))
