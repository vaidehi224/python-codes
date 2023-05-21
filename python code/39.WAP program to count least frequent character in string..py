a=input("Enter the string:")
freq=()
for i in a:
    if i in frq:
        freq[i]+=1
    else:
        freq[i]=1
res=min(freq,key=freq.get)
print("The minimum of all characters in string is:"+str(res))
