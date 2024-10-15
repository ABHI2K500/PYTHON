'''
Author: Abhijith P
Date:15-10-2024
To calculate the factorial of a number without using math module
'''
num=int(input("enter a number"))
sum=1
for i in range(1,num+1):
    sum=sum*i
print(sum)