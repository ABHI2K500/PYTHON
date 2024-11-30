'''
Name:Abhijith P
Date:30/11/2024
A python program to check whether the given string can be used as a variable or not
'''
def variable():
    var=input("enter the variable")
    count=0
    if var[0].isalpha() or var[0]=="_":
        for i in var:
            if i.isalnum() or i=="_":
                count=count
            else:
                count+=1
        if count>0:
            print("not a variable")
        else:
            print("a variable")
    else:
        print("not a variable")
variable()