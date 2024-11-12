
'''
Author:ABHIJTIH P
DATE:12/11/2024
PYTHON PROGRAM TO GET A LIST OF NUMBERS AND PRINT THE GREATEST AND SMALLEST'''
greatest=0
smallest=0
n=int(input("hwo much numbers would you like to enter"))
number_1 = int(input("enter the number"))
number_2 = int(input("enter the number"))
if number_1>number_2:
    greatest = number_1
    smallest=number_2
else:
    smallest=number_1
    greatest=number_2
for i in range(2,n):
    number_3=int(input("enter the number"))
    if number_3>greatest:
        greatest=number_3
    elif number_3<smallest:
        smallest=number_3
print(greatest,smallest)