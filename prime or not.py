'''
Author:Abhijith P
Date: 29/10/2024
python program to check whether a given number is prime or not
'''
num=int(input("enter a number:"))
sum=0
for i in range(2,num):
    if num%i==0:
        sum=sum+1
    else:
        sum=sum
if sum==0:
    print("the given number is prime number")
else:
    print(f"The given number, is not prime number")