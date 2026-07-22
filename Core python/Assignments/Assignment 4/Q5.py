# 5. WAP to print Fibonacci series upto n.

num = int(input("Enter the fibonacci number yo want => "))

a = -1
b = 1

for i in range(1 , num+1):
    c = a + b
    a = b
    b = c
print("Your fibonacci number is", c )
