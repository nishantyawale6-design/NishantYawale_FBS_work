# Write a program to prompt user to enter userid and password. After verifying userid and password display a 
# 4 digit random number and ask user to enter the same. If user enters the same number 
# then show him success message otherwise failed. (Something like captcha)

import random
userid = input("Enter the user id: ")
password = input("Enter the password: ")

if(userid == "admin" and password == "Pass@123"):
    captcha = random.randint(1000,9999)
    print(f"Your Captcha is {captcha}")
    chuser = int(input("Enter The Captcha: "))
    if(chuser == captcha):
        print("Login Successfully !!!. ")
    else:
        print("Captcha verification Failed. ")
else:
    print("user is invalid !!!. ")
    