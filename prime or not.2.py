'''
Author:Abhijith P
Date: 29/10/2024
python program to get prime numbers until a certain number
'''
num=int(input("enter a number:"))
for f in range(2,num+1):
    sum=0
    for i in range(1,f+1):
        if f%i==0:
            sum=sum+1
        else:
            sum=sum
    if sum==2:
        print(f,end=' ')
    else:
        pass
