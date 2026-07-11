# Convert temp from Celsius to Fahrenheit. (C/5 = (F-32)/9)
cel = float(input('enter the temperature im celcius : '))

# c/5 = (f-32/9)
# (f-32/9)= c/5
#(f-32)= c9/5
#f = c9/5 + 32
fahrenheit = cel * 9/5 + 32

print(f'Temperature in fahrenheit is {fahrenheit}.')

