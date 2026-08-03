# 2. Enter number of students from user. For those many students accept marks of 5
# subject marks from user and calculate percentage. Display all percentage and
# average percentage of students.

num = int(input("ENter the number of students => "))

total_percentage = 0
for i in range(1,num+1):
    print("\nEnter the marks of student", i)
    
    total = 0
    
    for j in range(1,6):
        marks = int(input(f"Enter the marks of sub {j} => "))
        total = total + marks

    percentage = total / 500 * 100
    print("Percentage of student is", i,"=", percentage)

    total_percentage = total_percentage + percentage

average = total_percentage / num
print("\nAverage Percentage of all Students =", average)

    
