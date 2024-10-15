'''
Author: Abhijith P
Date:15-10-2024
to determine the smallest of 3 numbers'''
num1=int(input("enter a number"))
num2=int(input("enter a number"))
num3=int(input("enter a number"))
if num1>num2 and num3>num2:
    print("number 2 is the smallest")
elif num2>num1 and num3>num1:
    print("number 1 is the smallest")
elif num2>num3 and num1>num3:
    print("number 3 is the smallest")
else:
    print("some of the given numbers are equal, please provide different values")
