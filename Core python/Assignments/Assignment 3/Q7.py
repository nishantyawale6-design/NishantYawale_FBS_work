# Write a program to check if user has entered correct userid and password.

userid = input("Enter the User Id: ")
password = input("ENter the Password: ")

if(userid == "admin" and password == "Pass@123"):
    print("Login Successfully. ")
else:
    print("Invalid user. ")
