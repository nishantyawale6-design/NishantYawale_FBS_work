# Write a program to swap two numbers using third variable.

x = int(input('enter the first no.: '))
y = int(input('enter the second no.: '))

# Before swapping
print(f'before swapping: x = {x} and y = {y}')

# After Swapping
temp = x
x = y
y = temp

print(f'After swapping: x = {x} and y = {y}' )