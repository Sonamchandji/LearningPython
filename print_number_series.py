# *****  consolidate the 3 different number series
# 1. Even numbers
# 2. Odd numbers
# 3. Fibonacci numbers  *******

# Function for even number

def even_numbers(num,n):
  print(f" Printing{n} even numbers from number {num}\n")

  i=0
  if (num % 2) != 0:
    num=num+1
  while(i<n):
    print(num)
    num = num + 2
    i=i+1

# Function for odd numbers

def odd_numbers(num,n):
  print(f" Printing{n} odd numbers from number {num}\n")

  i = 0
  if (num % 2) == 0:
    num = num + 1
  while (i < n):
    print(num)
    num = num + 2
    i = i + 1
# Function for fibonacci number
def fibonacci(num,n):
  # Display the given number with required number of fibonacci numbers to be printed
  print(f" Printing {n} fibonacci numbers after {num} ")

  num1 = 0
  num2 = 1
  i = 0

  if num == 0:
    print(f"{num2}")
    i = i + 1
  while (i < n):
    num3 = num2 + num1
    if num < num3:
      print(f"{num3}")
      i = i + 1
    num1 = num2
    num2 = num3


choice ='yes'
while (choice.lower()=='yes'):

  # To display message to user and provide various options for number series

  print(" Please choose an option for number series !\n")
  print(" (1) Even numbers \n (2) Odd numbers \n (3) Fibonacci numbers\n")

  # Ask user to enter the option
  Option_selected = int(input("Enter a number for selected option\n"))

  # Display the option selected by the user
  if Option_selected == 1:
    print(f"You have selected option {Option_selected}  : To print Even numbers")
  elif Option_selected == 2:
    print(f"You have selected option {Option_selected}  : To print Odd numbers")
  elif Option_selected == 3:
    print(f"You have selected option {Option_selected}  : To print Fibonacci numbers")
  else:
     print("You entered Invalid input so bye, Please enter option 1, 2 or 3 next time :)")
     exit()

# Ask user to enter a number after which program will print required series
  num=int(input("Enter a number"))

# Ask user to enter how many numbers to be printed
  n= int(input("How many numbers would you like to print in series ? "))

# To check option and call corresponding function
  if Option_selected == 1:
     even_numbers(num,n)
  elif Option_selected == 2:
     odd_numbers(num,n)
  else:
     fibonacci(num,n)

  choice=input("Would you like to print another series?\n Enter yes or no ")

