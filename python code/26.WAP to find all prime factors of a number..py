num = int(input("Enter a number: "))
i = 2
while(i <= num):
    if(num % i == 0):
        print(i)
        num //= i
    else:
        i += 1
