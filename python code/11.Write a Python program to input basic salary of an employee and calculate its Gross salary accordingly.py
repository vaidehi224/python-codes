'''
Write a Python program to input basic salary of an employee and calculate its Gross salary
according to following:
Basic Salary <= 10000 : HRA = 20%, DA = 80%
Basic Salary <= 20000 : HRA = 25%, DA = 90%
Basic Salary > 20000 : HRA = 30%, DA = 95%.
'''

sal=float(input('Enter the basic salary:'))
if(sal<=10000):
    hra=0.2*sal
    da=0.8*sal
    Salary=sal+hra+da
elif(sal<=20000):
    hra=0.25*sal
    da=0.9*sal
    Salary=hra+da+sal
else:
    hra=0.3*sal
    da=0.95*sal
    Salary=hra+da+sal
print ('The gross salary is',Salary)
