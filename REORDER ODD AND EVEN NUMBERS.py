'''
Author:Abhijith P
date:19/11/2024
Python program to get a list of odd numbers and even numbers combined, where odd are displayed first and both odd and even are in ascending order
'''
L1=[]
L2=[]
no_of_elements=int(input("enter number of elements in your list"))
for i in range(no_of_elements):
    digit=int(input("enter a number"))
    L1.append(digit)
no_of_elements2=int(input("enter number of elements in your list"))
for i in range(no_of_elements2):
    digit2=int(input("enter a number"))
    L2.append(digit2)
list_combined=L1+L2
L3=[]
L4=[]
for i in list_combined:
    if i%2==0:
        L3.append(i)
    else:
        L4.append(i)
L3.sort()
L4.sort()
final=L4+L3
print(final)