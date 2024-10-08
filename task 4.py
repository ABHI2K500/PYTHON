'''
Author: Abhijith P
Date:07-10-2024
Python program that uses function from math module to perform
the following operations on a number provided by the user
'''
import math
#imports the module called math
number=int(input('please enter a number:'))
root=math.sqrt(number)
factorial=math.factorial(number)
power=math.pow(number,2)
print('the square root of the number is:',root)
print('the factorial of the number is',factorial)
print('the power of the number is',power)