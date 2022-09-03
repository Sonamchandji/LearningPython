# A program to convert string character to corresponding alphabet number

# Ask user to enter a string to be converted in to numbers

string1 = input(" Enter a string plaese! ")

# To display the entered string

print(f"You have entered '{string1}' as a input string")

# To display the message before converting char into positional number

print(f"Corresponding alphabet place number for each character in {string1} is :")

# To find the lower c ase strung then convert to corresponding ASCII using ord() method for each character

for char in string1.lower():
    print(ord(char)-96)