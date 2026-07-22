# 12. Write a program to check if given number is Armstrong number or not.
# (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 + 4*4*4*4)

num = int(input("Enter the number => "))
count = len(str(num))
temp = num
total = 0
while(num > 0):
    d = num % 10
    total = total + (d ** count)
    num = num // 10
    print(total)

if(total == temp):
    print("The number is armstrong. ")
else:
    print("the number is not armstrong. ")
