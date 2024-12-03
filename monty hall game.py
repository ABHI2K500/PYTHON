'''
Author:ABhijith P
Date:03/12/2024
Program to make a Monty Hall Game
'''
def monty():
    from random import randint
    choice=int(input("open a door(1,2 or 3):"))
    a=randint(1,4)
    if a==choice:
        secondchoice=input("Opens the door, revealing a car\nDo you want to switch your door(Y/N):")
        secondchoice.casefold()
        if secondchoice=='y':
            finalchoice=int(input("enter your final choice:"))
            if finalchoice==a:
                print("Congrats you won the car")
            else:
                print("Congrats you won a Goat")
        else:
            print("Congrats you won a car")
    else:
        secondchoice=input("Opens the door, revealing a Goat\nDo you want to switch your door(Y/N):")
        if secondchoice=='y':
            finalchoice=int(input("enter your final choice:"))
            if finalchoice==a:
                print("Congrats you won the car")
            else:
                print("Congrats you won a Goat")
        else:
            print("Congrats you won a GOAT")
monty()
