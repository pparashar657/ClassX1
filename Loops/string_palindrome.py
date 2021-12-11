str = input("Enter any string : ")

rev_str = str[::-1]

if (str == rev_str):
    print(str, "is palindrome")
else:
    print(str, "is not palindrome")
