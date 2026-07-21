# Accept age of five people and also per person ticket amount and then calculate total 
# amount to ticket to travel for all of them based on following condition : 
# a. Children below 12 = 30% discount 
# b. Senior citizen (above 59) = 50% discount 
# c. Others need to pay full. 

i = 1
while(i<= 5):
    ag1 = int(input("Enter the age of Person: "))
    tkprice1 = float(input("Enter the ticket price: "))
    totalprice = 0
    if(ag1 <= 12):
        totalprice=totalprice+(tkprice1*0.30)
    elif(ag1 > 59):
        totalprice=totalprice+(tkprice1*0.50)
    else:
       totalprice=totalprice+tkprice1
    i+=1
print("total price of ticket is => ", totalprice)