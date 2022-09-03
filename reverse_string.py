# To ask user to enter a string

string1=input("Enter a string please")

# To display the entered string
print(f"You entered string {string1} \n Each Character of Reverse of {string1} using Reverse method is:\n")

# To print each character using for loop
string2 = ""
for i in reversed(string1):
    print(i)

# To print without using Reversed method
print(f"Each Character of Reverse of {string1} using indexing is:\n")

for i in string1[::-1]:
    print(i)
