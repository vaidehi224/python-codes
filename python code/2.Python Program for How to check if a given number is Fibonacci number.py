n=int (input ("Enter the number: "))
a=0
b=1
c=1
if n==0 or n==1:
    print ("Yes")
else:
    while a<n:
    a=b+c
    c=b
    b=a
    if a==n:
        print ("Yes")
    else:
        print ("No")
