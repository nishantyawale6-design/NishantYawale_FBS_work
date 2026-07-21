a = int(input("Enter the First Side = "))
b = int(input("Enter the Second Side = "))
c = int(input("Enter the Third Side = "))

if(a + b > c) and (a + c > b) and (b + c > a):
    print("Valid triangle. ")
else:
    print("Invalid Triangle. ")