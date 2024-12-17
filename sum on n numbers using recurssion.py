'''
Author:ABHIJITH P
Date:17/12/2024
program to return the sum of n numbers using recursion
'''
def sum(n):
    if n==1:
        return 1
    else:
        return n+ sum(n-1)
