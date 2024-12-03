'''
Author:ABhijith P
Date:03/12/2024
Program to make a stick game
'''
num_of_sticks=16
chance1=0
chance2=0
print("Rules\n1.take maximum up to 3 sticks\n2.player who takes last stick looser")
while num_of_sticks>0:
    while num_of_sticks>=1:
        user1=int(input("player one takes:"))
        chance1+=1
        num_of_sticks-=user1
        print(f"num of sticks {num_of_sticks}")
        if num_of_sticks>0:
            user2=int(input("Player two takes:"))
            chance2+=1
            num_of_sticks-=user2
            print(f"num of sticks {num_of_sticks}")

    if num_of_sticks==0:
        if chance1==chance2:
            print("Player one lost")
        else:
            print("player two lost")
    else:
        print("there arent enough sticks")

