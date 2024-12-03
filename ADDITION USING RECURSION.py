'''
Author:Abhijith p
Date: 03/12/2024
Python program to add two numbers using recursion

'''
def addition(a,b):
    if b==0:
        return a
    else:
        return addition(a+1,b-1)
