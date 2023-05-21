n=int(input("Enter the number:"))
k=int(input("Enter the n'th number:"))

if (n <= 2):
    print(n - 1)
else:
    a = 2
    b = 1
    c = 1
    while (c * k < n):
        c = a + b
        a = b
        b = c
    print(c * k)
