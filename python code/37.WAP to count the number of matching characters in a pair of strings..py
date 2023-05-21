a=input("Enter the first string")
b=input("Enter the second string")
c=set(a)
d=set(b)
m=c&d
print("The number of matching characters are",len(m))
