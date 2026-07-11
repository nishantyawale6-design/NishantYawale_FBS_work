# Wap to calculate the percentage of student based on marks of any 5 subjects.
sub1 = int(input('enter the marks: '))
sub2 = int(input('enter the marks: '))
sub3 = int(input('enter the marks: '))
sub4 = int(input('enter the marks: '))
sub5 = int(input('enter the marks: '))

totalmarks = sub1+sub2+sub3+sub4+sub5
percentage = totalmarks/500 * 100

print(f'The percent of 5 subject is {percentage}')