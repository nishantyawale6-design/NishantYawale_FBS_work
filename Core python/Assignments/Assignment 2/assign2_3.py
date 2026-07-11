# Convert distant given in feet and inches into meter and centimeter 
feet = float(input('enter the distance in feet: '))
inches = float(input('enter the distance in inches'))

meter = (feet * 0.35) + (inches * 0.0254)

centimeter = meter * 100

print(f'the meter of distance is {meter} and centimeter of distance is {centimeter}.')
