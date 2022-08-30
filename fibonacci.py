# To print required number of fibonacci numbers after a given number
# Ask user to enter a number after which program will print fibonacci numbers
num=int(input("Enter a number"))

# Display the entered number
print(f" You have entered number {num} ")

# Ask user to eneter how many fibonaci numbers to be printed
n= int(input("How many fibonacci numbers would you like to print? "))

# Display the given number with required number of fibonacci numbers to be printed
print(f" Printing {n} fibonacci numbers after {num} ")

num1=0
num2=1
i=0
if num==0:
     print(f"{num2}")
     i=i+1
while(i<n):
    num3=num2+num1
    if num<num3:
      print(f"{num3}")
      i=i+1
    num1=num2
    num2=num3