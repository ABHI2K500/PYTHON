'''
Author:Abhijtih P
Date:22/10/2024
A Python program to find the largest of three numbers. 
'''



num1=int(input("enter number 1:"))
num2=int(input("enter number 2:"))
num3=int(input("enter number 3:"))
if num1<num2 and num3<num2:
    print(num2,"is the greatest")
elif num2<num1 and num3<num1:
    print(num1,"is the greatest")
elif num2<num3 and num2<num3:
    print(num3,"is the greatest")
elif num1==num2:
    print("num 1 and 2 are equal")
elif num1==num3:
    print("num3 and num1 are equal")
else:
    print("num3 and num2 are equal")
