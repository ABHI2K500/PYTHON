'''
AUTHOR:ABHIJITH P
DATE:08/10/2024
Python program that displays date and time is different formats
'''
from datetime import datetime
current=datetime.now()
print(current)
format_1=current.strftime("%Y-%m-%d %H:%M:%S")
print(format_1)
format_2=current.strftime("%m/%d/%Y")
format_3=current.strftime("%A,%m %d,%Y")
format_4=current.strftime("%A,%m %d,%Y %H:%M:%S %p")
format_5=current.strftime("%a-%b-%d %H:%M:%S %Z %Y")
format_6=current.strftime("%Y-%m-%d")
format_7=current.strftime('%d')
format_8=current.strftime('%H:%M:%S')
format_9=current.strftime('%M')
format_10=current.strftime('%Y')
print(format_2)
print(format_3)
print(format_4)
print(format_5)
print(format_6)
print(format_7)
print(format_8)
print(format_9)
print(format_10)