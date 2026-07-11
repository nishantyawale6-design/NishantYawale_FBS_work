gender = input('enter gender (m/f) ')
age = int(input('enter the age '))

if(gender == 'f'):
    if(age >= 18):
        print('the girl is eligible for marrige.')
    else:
        print('pehele padhai kro.')
else:    
    if(age >= 21):
        print('boy is eligible for marrige.')
    else:
        print('pehele kama lo.')