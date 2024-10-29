'''
Author:Abhijith P
Date: 29/10/2024
python program to print the vowels in an string
'''
_string=input("Enter the string:")
vowels=('a','e','i','o','u','A','E','I','O','U')
for i in _string:
    if i in vowels:
        print(i,end=" ")