def is_pallindrome(n):
    original = n
    reverse = 0

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10

    if original == reverse:
        return True
    else:
        return False


n = int(input("Enter a number: "))

if is_pallindrome(n):
    print("Pallindrome")
else:
    print("Not pallindrome")