# 1. WAP to print all even numbers until n.

num = int(input("Enter the Number => "))
for i in range(1 , num):
    if(i % 2 == 0):
        print(i)