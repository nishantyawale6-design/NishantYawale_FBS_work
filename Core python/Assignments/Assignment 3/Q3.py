# 3. Write a program to input angles of a triangle and check whether triangle is valid or not.

a = int(input("Enter the first angle: ")) 
b = int(input("Enter the second angle: ")) 
c = int(input("Enter the Third angle: ")) 

if(a + b + c == 180):
    print("Angle is valid. ")
else:
    print("Angle is not valid. ")