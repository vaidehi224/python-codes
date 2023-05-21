x=int(input("Enter the number:"))
count=1
for i in range(1,((x//2)+1)):
    if(x%i==0):
        count+=1
if(count==2):
    print("%d is Prime number"%x)
else:
    print("%d is not Prime number"%x)
