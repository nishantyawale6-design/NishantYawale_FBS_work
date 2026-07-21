# 2. Write a program to input any alphabet and check whether it is vowel or consonant.
ch = input("Enter the alphabet: ")

if ch in ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U"):
    print("it is Vowel." )
else:
    print("it is consonant. ")