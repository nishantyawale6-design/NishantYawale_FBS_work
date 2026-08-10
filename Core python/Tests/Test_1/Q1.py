
l = float(input("Enter the length => ")) 
b = float(input("Enter the breadth => ")) 
r = float(input("Enter the radius => ")) 

area = l * b + 3.14* r**2/2

print(f"Area = {area}")

perimeter = 2*l + b + 3.14*r

print(f"Perimeter = {perimeter}")