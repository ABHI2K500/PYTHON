'''
Name:Abhijith P
Date:30/11/2024
A python program to count upper ands lower numbers
'''
user_string = str(input("enter a string"))
def upper():
    upper_count=0
    for i in user_string:
        if i.isupper():
            upper_count+=1
    print(upper_count)

def lower():
    lower_count = 0
    for f in user_string:
        if f.islower():
            lower_count += 1
    print(lower_count)
upper()
lower()


