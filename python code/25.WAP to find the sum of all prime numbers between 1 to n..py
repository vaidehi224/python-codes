k=int(input("Enter the number:"))
sum=0
for n in range(1,k+1):
    count=0
    for i in range(2,(n//2+1)):
        if(n%i==0):
            count+=1
            break
    if(count==0 and n!=1):
        print("%d"%n,end=",")
        sum+=n
print("\nThe sum of prime number in range 1 to %d is %d"%(k,sum))
