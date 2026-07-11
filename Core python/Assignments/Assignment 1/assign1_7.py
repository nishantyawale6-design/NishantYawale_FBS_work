import cmath 

a = int(input('enter a: '))
b = int(input('enter b: '))
c = int(input('enter c: '))

#calculate D(discreminant)
D = (b**2) - 4*a*c

#calculate the roots 
root1 = ((-b) - cmath.sqrt(D)) / (2*a)
root2 = ((-b) + cmath.sqrt(D)) / (2*a)

print(f'Root1 is {root1} and Root2 is {root2}.')

