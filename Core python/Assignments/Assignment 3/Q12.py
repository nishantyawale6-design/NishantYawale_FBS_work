# Write a program to check if given 3 digit number is a palindrome or not. 
num = int(input("Enter the number you want palindrome => "))

temp = num
rev = 0

while(num > 0):
    d = num % 10
    rev = rev * 10 + d
    num = num // 10
if(temp == rev):
    print("Your number is palindrome. ")
else:
    print("Your number is not palindrome. ") 

