# for i in range(1,7):
#     for j in range(1,6):
#         if(i == 0 or i == 7-1 or j == 0 or j == 6-1):
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()

# n = int(input("Enter size: "))

for i in range(1,6):
    for j in range(1,6):
        if i == 0 and i == 6-1 and j == 0 and j == 6-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()