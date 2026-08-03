# Write a program to prompt user to enter userid and password. If Id and
# password is incorrect give him chance to re-enter the credentials. Let him try 3
# times. After that program to terminate.

correct_userid = "admin"
correct_password = 'Nishant@123'
for i in range(1, 4):
    
    userid = input("ENter the userid => ")
    password = input("ENter the password => ")

    if(correct_userid == userid and correct_password == password):
        print("Login Successful ")
        break
    else:
        print("Invalid userid or password .")

    if(i==3):
        print("Login failed. ")