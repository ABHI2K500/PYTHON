'''
Author:Abhijith p
Date: 03/12/2024
Python program to find factorial of a number using recursion
'''
def factorial(n):
    if n==1:
        return n
    else:
        return n*factorial(n-1)
print(factorial(4))