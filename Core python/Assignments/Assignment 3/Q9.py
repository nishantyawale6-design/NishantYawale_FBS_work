# Input 5 subject marks from user and display grade(eg.First class,Second class ..)

s1 = float(input("Enter the marks of english: "))
s2 = float(input("Enter the marks of Hindi: "))
s3 = float(input("Enter the marks of Marathi: "))
s4 = float(input("Enter the marks of Math: "))
s5 = float(input("Enter the marks of Science: "))

total = s1 + s2 + s3 + s4 + s5
percentage = total / 5
print(f"total marks is {total}." )
print(f"percentage is {percentage}." )

if(percentage >= 75 ):
    print(" Grade A ")
elif(percentage >= 65):
    print("Grade B, second class")
elif(percentage >= 45):    
    print("Grade c, third class")
else:
    print("Student is fail. ")
