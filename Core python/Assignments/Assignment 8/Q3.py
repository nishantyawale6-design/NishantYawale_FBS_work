# # a)
def sum_series(n):
    sum = 0

    for i in range(1, n + 1):
        sum = sum + i

    return sum


n = int(input("Enter n: "))

print("Sum =", sum_series(n))

# b)
def factorial_sum(n):
    fact = 1
    sum = 0

    for i in range(1, n + 1):
        fact = fact * i
        sum = sum + fact

    return sum


n = int(input("Enter n: "))

print("Sum =", factorial_sum(n))

# c)
def power_sum(n):
    sum = 0

    for i in range(1, n + 1):
        sum = sum + (i ** i)

    return sum


n = int(input("Enter n: "))

print("Sum =", power_sum(n))