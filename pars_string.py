# To print each character of string using while loop
string1=input("Enter a string please1 ")
# To display the string to the user
print(f"You have entered {string1} \n")
# To print the characters of the string
length=len(string1)
i=0
while(i<length):
    print(f"The character at {i}th index is {string1[i]}")
    i= i+1