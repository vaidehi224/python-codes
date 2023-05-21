a=input("Enter the string:")
freq=()
for i in a:
    if i in frq:
        freq[i]+=1
    else:
        freq[i]=1
res=max(freq,key=freq.get)
print("The maximum of all characters in string is:"+str(res))
