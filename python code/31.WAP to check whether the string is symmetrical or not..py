input_str = input("Enter a string: ")
flag = 0

if len(input_str) % 2 == 0:
    mid = len(input_str)//2
else:
    mid = len(input_str)//2 + 1

for i in range(mid):
    if input_str[i] != input_str[len(input_str)-i-1]:
        flag = 1
        break

if flag == 0:
    print("The entered string is symmetrical")
else:
    print("The entered string is not symmetrical")
