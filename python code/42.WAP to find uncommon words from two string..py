a=input("Enter the first string")
b=input("Enter the second string")
c=a.split()
d=b.split()
print("The uncommon word in string are\n")
for i in c:
    if(i not in d):
        print(i,end=',')
for i in d:
    if(i not in c):
        print(i)
