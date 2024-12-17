'''
Author:ABHIJITH P
Date:17/12/2024
program to return the factorial of n numbers using recursion
'''
def factorial(n):
    if n==1:
        return 1
    else:
        return n* factorial(n-1)
