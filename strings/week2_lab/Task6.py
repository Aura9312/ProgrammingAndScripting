#Task 6

inputstr = input("Please input any word: ").lower()

if inputstr == inputstr[::-1]:
    print("This word is a palindrome.")
else:
    print("This word is not a palindrome")