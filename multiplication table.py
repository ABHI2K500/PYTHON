'''
Author:Abhijith P
Date: 29/10/2024
python program to display the multiplication table of a certain number
'''
num=int(input("enter a number"))
if num<0:
    print("please enter a positive number")
else:
    for i in range(1,13):
        print(num*i)