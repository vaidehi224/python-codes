x=input("Please Enter Your Own Character : ")
if(ord(x)>=48 and ord(x)<=57):
    print ("The Given Character",x,"is a Digit")
elif ((ord(x)>=65 and ord(x)<=90) or (ord(x)>=97 and ord(x)<=122)):
    print ("The Given Character",x,"is an Alphabet")
else:
    print ("The Given Character",x,"is a Special Character")
