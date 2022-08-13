# *****  To build a calculator program   *******

# To display message to user and provide various options for calculation

print(" Hello! Please choose an option for calculation!\n")
print(" (1) Add(+)\n (2) Subtract(-)\n (3) Multiply(*)\n (4) Divide(/)\n (5) Find Remainder(%)\n (6) Find Quotient(//)\n (7) Find Square of a number(**)\n")

# Ask user to enter the option
Option_selected = int(input("Enter a number for selected option\n"))

# Use if else to check the option and perform calculations accordingly
if Option_selected == 7:
     x = int(input("Enter a number to be squared"))
     result = x * x
elif Option_selected >7:
     print("Please enter a valid option next time :) !")
     exit()
else:
# Ask user to enter first number
  a=int(input("Enter first number"))
# Ask user to enter second number
  b=int(input("Enter second number"))
  if Option_selected == 1:
    result= a+b
  elif Option_selected == 2:
    result=a -b
  elif Option_selected == 3:
    result=a*b
  elif Option_selected == 4:
    result=a/b
  elif Option_selected == 5:
    result= a%b
  elif Option_selected == 6:
    result=a//b

# Display the result
print("Output is\n1",result)