n = int(input("Enter the value of n: "))
a = 0
b = 1

if n < 0:
    print("Incorrect input")
 
elif n == 0:
    print(a)
 
elif n == 1 or n == 2:
    print(b)
 
else:
    for i in range(2,n):
        c = a + b
        a = b
        b = c
    print(b)
