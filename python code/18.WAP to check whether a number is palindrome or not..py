x=int(input('enter the number:'))
t=0
num=x
while(x>0):
    rem=x%10
    t=t*10+rem
    x//=10
print('the reverse of %d is %d'%(num, t))
if(t==num):
    print("The number is palindrome")
else:
    print("The number is not palindrome")
