# Write a program to swap two numbers without using third variable.

x = int(input('enter the first no.: '))
y = int(input('enter the second no.: '))

#before swapping
print(f'Before swapping x = {x} and y = {y}')

# After swapping
x,y = y,x

print(f'After swapping x = {x} and y = {y}')