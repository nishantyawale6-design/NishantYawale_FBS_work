# Convert the time entered in hh,min and sec into seconds.
hours = int(input('enter the hours: '))
min = int(input('enter the min: '))
sec = int(input('enter the sec: '))


total_seconds = (hours * 3600) + (min * 60) + (sec)

print(f'The total sec is {total_seconds}.')

