with open("file1.txt","r") as f:
    with open("file2.txt","w") as f1:
        f1.write(f.read())
