# Write a program to check whether the triangle is equilateral, isosceles or scalene
# triangle.

a = int(input("Enter the first side of triangle: "))
b = int(input("Enter the second side of triangle: "))
c = int(input("Enter the third side of triangle: "))

if((a + b > c) and (a + c > b) and (b + c > a)):
    if(a == b == c):
        print("Triangle is equilateral. ")
    
    elif(a == b or b == c or a == c):
        print("Triangle is isoscales. ")

    else:
         print("Triangle is Scalene. ")

else:
    print("invalid triangle. ")


