x=int(input('Enter the number:'))
sum=0
while(x>0):
    rem=x%10
    sum=sum+rem
    x//=10
print('The sum of digit of a number is',sum)
