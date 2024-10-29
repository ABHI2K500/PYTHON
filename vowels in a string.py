'''
Author:Abhijith P
Date: 29/10/2024
python program to print the vowels in an string
'''
input_string=input("Enter the string:")
vowels=('a','e','i','o','u','A','E','I','O','U')
vowel_count
for i in input_string:
    if i in vowels:
        vowel_count+=1
        print(i,end=" ")
print(vowel_count)
