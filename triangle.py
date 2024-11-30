'''
Name:Abhijith P
Date:30/11/2024
A python program to check a triangle is right angle or not
'''
def right_angled_triangle(side1,side2,side3):
    import math
    sides=[side1,side2,side3]
    sides.sort()
    print(sides)
    if sides[2]== math.sqrt(sides[0]**2 + sides[1]**2):
        print("the given is a right angled triangle")
    else:
        print("the given is not a right angled triangle")
right_angled_triangle()