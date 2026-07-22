# 9. WAP to print all numbers in a range divisible by a given number.

start = int(input("Enter the starting number => "))
end = int(input("Enter the ending number => "))
num = int(input("Enter the divisor => "))

for i in range(start , end,  num+1):
    if(i % num == 0):
        print(i)