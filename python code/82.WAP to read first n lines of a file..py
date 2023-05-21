n = int(input("Enter Lines To Read :"))
f = open("file.txt","r")
for i in range(n):
	print(f.readline(),end='')
