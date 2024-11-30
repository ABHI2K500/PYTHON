'''
Name:Abhijith P
Date:30/11/2024
A python program to check whether the given mobile numbe ris validor not 
'''
def mobile_number_checker():
    mobile_number=str(input("enter your mobile number:"))
    if mobile_number[0]=="7" or "8" or "9":
        if len(int(mobile_number))==10:
            print("it is a valid number")
        else:
            print("mobile number is not valid")

    else:
        print("given is not an mobile number")
mobile_number_checker()



