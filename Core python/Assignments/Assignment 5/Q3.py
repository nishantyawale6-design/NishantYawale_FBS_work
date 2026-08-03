num = int(input("Enter the num of passenger => "))
ticket = float(input("Enter the ticket cost => "))
total = 0

for i in range(1, num+1):
    age = int(input(f"Enter the age of passenger {i} => "))
    
    if(age <= 12):
        amount = ticket - (ticket * 30/ 100)

    elif(age >= 59):
        amount = ticket - (ticket * 50/100)
    
    else:
        amount = ticket

    total = total + amount
    
print(f"total cost of ticket is {total}")