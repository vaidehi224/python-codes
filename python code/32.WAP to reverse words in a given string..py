a=input("Enter the string:")
n=len(a)
last=n-1
print("The reverse of the string",a,"is")
while(last>=0):
    print(a[last],end="")
    last-=1
    
