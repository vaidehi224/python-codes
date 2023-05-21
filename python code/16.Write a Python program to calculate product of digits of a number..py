x=int(input('Enter the number:'))
product=1
while(x>0):
    rem=x%10
    product=product*rem
    x//=10
print('The product of digits of a number is',product)
