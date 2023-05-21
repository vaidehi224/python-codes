'''
Write a Python program to input electricity unit charges and calculate total electricity
bill according to the given condition:
For first 50 units Rs. 0.50/unit
For next 100 units Rs. 0.75/unit
For next 100 units Rs. 1.20/unit
For unit above 250 Rs. 1.50/unit
An additional surcharge of 20% is added to the bill.
'''

x=float(input("Enter the electricity unit"))
if(x<=50):
    bill=0.5*x
if(x>50 and x<=150):
    bill=50*0.5+(x-50)*0.75
if(x>150 and x<=250):
    bill=50*0.54+100*0.75+ (x-150)*1.20
if(x>250):
    bill=50*0.54+100*0.75+100*1.2+ (x-250)*1.5
Total=bill+0.2*bill
print ("Total bill after surcharge is", Total)
