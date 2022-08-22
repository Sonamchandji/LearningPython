# A program to slice the string


# Ask user to enter a string
string_input= input("Enter a string please!\n")
print(f" The entered string is {string_input}")
print(" ___________________________________  ")

# To slice the string after removing first and last character
print(f" The string after removing first and last character from '{string_input}' is {string_input[1:-1]}")
print(" ___________________________________  ")

# To slice the string after removing first two characters
print(f" The string after removing first two characters of '{string_input}' is {string_input[2:]}")
print(" ___________________________________  ")

# To slice the string after removing last two characters
print(f" The string after removing last two characters of '{string_input}' is {string_input[:-2]}")
print(" ___________________________________  ")

# To find length of the string and middle index
index=len(string_input)//2
print(f" The  middle index is { index}")
print(" ___________________________________  ")

# To find first half of the string
print(f" The first half of the string '{string_input}' is {string_input[:index]}")
print(" ___________________________________  ")

# To find second half of the string
print(f" The second half of the string '{string_input}' is {string_input[index:]}")
print(" ___________________________________  ")
