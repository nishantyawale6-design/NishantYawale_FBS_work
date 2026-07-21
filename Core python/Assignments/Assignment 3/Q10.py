# Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)

gender = input("Enter the gender (m/f): ")
age = int(input("Enter the age: "))

if(gender == "f"):
    if(age >= 18):
        print("Girl is Eligible to marrige. ")
    else:
        print("Not Eligible to marrige. ")
else:
    if(age >= 21):
        print("Boy is Eligible for marrige. ")
    else:
        print("Boy is not Eligible for marrige. ")

