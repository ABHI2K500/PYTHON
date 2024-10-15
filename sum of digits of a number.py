'''
Author: Abhijith P
Date:15-10-2024
to add the digits of a number
'''
num=int(input("enter a number:"))
str_num=str(num)
sum=0
for i in str_num:
    sum+=int(i)
print(sum)