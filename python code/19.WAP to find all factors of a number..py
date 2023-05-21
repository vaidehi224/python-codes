x=int(input('Enter the number:'))
i=1
print("the factors of %d are"%x,end=" ")
while(i<x):
    if(x%i==0):
        print(i,end=" ")
    i+=1
