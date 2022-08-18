# Ask user to enter a string

string1=input("Enter a string value:")
print("Your first string value is:", string1)

# Ask user to enter another string

string2=input("Enter another string value:")
print("Your second string value is:", string2)

# Ask user to enter a number
number=int(input("Enter a number (preferably less than 10)"))
print(" You entered number: ", number)

print("_____________________\n")
concat_string=string1+string2
print(string1," + ",string2,"is",concat_string)

product1= string1 * number

print("_____________________\n")
print(f"{string1} * {number} is {product1}")

product2= string2 * number

print("_____________________\n")
print(f"{string2} * {number} is {product2}")







