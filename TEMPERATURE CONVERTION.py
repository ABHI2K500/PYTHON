'''
Author:Abhijtih P
Date:22/10/2024
a Python program to convert temperature values back and forth between Celsius and Fahrenheit
'''
temp=float(input("Enter the temperature"))
form=input("Is the provided temperature in Celsius(C) or Fahrenheit(F)")
a_form=form.capitalize()
fahrenheit=(9/5 *temp)+32
celsius=5/9*(temp-32)
if form=='F':
    print('Value of temperature in celsius=',celsius)
elif form=='C':
    print('Value of temperature in fahrenheit=',fahrenheit)
else:
    print("choose either (C) celsius of (F)Fahrenheit")
