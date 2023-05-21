with open("file.txt","r") as f:
    print(f.closed)
f.close()
print(f.closed)
