'''
Author: Abhijith P
Date:15-10-2024
python program to follow n number of odd numbers
'''
num=int(input("how many off numbers do u need"))
odd=1
a=0
while a<=num:
    print(odd,end="._.")
    odd+=2
    a+=1