# Write a program to calculate profit or loss.

cp = float(input("Enter the Cost Price: "))
sp = float(input("Enter the Selling Price: "))

if(cp < sp):
    profit = sp - cp
    print("Profit is ", profit)
elif(sp < cp):
    Loss = cp - sp
    print("Loss is ", Loss)
else:
    print("No Profit, No Loss")
