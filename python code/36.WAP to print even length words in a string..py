s=input("Enter the string:")
n=s.split()
print("Words of even length:")
for i in n:
    if(len(i)%2==0):
        print(i)
