'''
AUTHOR:ABHIJITH P
DATE:08/10/2024
Python program that concatenates the users first and last name the print the final string
'''
string1="ABHIJITH "
string2='P'
string3=string1+string2
print(len(string3))
print(string3)
length=len(string3)
string4=string3[length:]
firstname=string3[:length-2]
print(string4)
print(string1+string2)
print(firstname)
