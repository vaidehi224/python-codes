f = open("file.txt","a")
str = input("\n\t\tEnter Data TO Append  In file.txt : ")
f.write(str)
f = open("file.txt","r")
print(f.read())
f.close()
