'''
AUTHOR:ABHIJITH P
DATE:08/10/2024
Python program that concatenates the users first and last name the print the final name and rist name
'''
string1=input('please enter your name')
string2=input('enter your last name')
length1=len(string1)
string3=string1+' '+string2
length=len(string3)
print(len(string3))
print(string3)
string4=string3[length1:]
firstname=string3[:length-1]
print(string4)
print(string1+string2)
print(firstname)
