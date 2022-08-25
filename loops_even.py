# Ask user to enter a number
num=int(input("Enter a number please!\n"))
# Ask user to enter a limit number
n=int(input("Enter how many even numbers you want to print?\n"))

print(f"You have entered a number{num} and you want {n} even numbers \n")

i=0
num1=num
while(i<n):
    if (num% 2 )== 0:
        num=num+2
        print(num)
    else:
        print(num+1)
        num=num+1
    i=i+1

# using for loop
print(f"Using for loop result is \n")

for i in range(0,n):
    if (num1 % 2 )== 0:
        num1=num1+2
        print(num1)
    else:
        print(num1+1)
        num1=num1+1
