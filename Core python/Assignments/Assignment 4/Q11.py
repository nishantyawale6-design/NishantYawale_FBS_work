num = int(input("Enter the Number => "))

temp = num
sum = 0

while(temp > 0):
    d = temp % 10

    fact = 1
    for i in range(1, d+1):
        fact = fact * i

    sum = sum + fact
    temp = temp // 10
if(sum == num):
    print("strong Number. ")
else:
    print("Not a strong number. ")