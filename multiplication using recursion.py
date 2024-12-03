'''
Author:Abhijith p
Date: 03/12/2024
Python program to multiply two numbers using recursion
'''
def multiplication(n1,n2):
    if n2==1:
        return n1
    else:
        return n1+multiplication(n1,n2-1)
print(multiplication(3,5))