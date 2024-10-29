'''
Author:Abhijith P
Date: 29/10/2024
python program to dipsplay factorial of a number using for loop
'''
number=int(input("enter a number:"))
factorial=1
for i in range(1,number+1):
    factorial=factorial*i
print(factorial)
