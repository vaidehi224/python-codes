x=int(input('Enter the number:'))
rem=x%10
while(x>10):
    R=x//10
    x/=10
print('Last digit',rem)
print("First digit",R)
