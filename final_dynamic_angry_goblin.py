# To create a small dynamic game through programming
import random

print(" Welcome To The Angry Goblin Hunt\n")
print('An Award Winning Game " Full Of Fun and Adventure "\n')
# Ask user to neter his/her name
name=input(" What is your name \n")
print(f" Welcome to the Game {name} !")
# Ask user no. of cupboards
total_cupboards=int(input("How many cupboards would you like to have in your game ?"))
# Display the message to the user
print(f" {name}, Do you think you can find the Goblin hiding in the cupboards ? \n ")
for i in range(0,total_cupboards):
    print("|_|")
# To store the hiding cupboard number in a variable
correct_cupboard_no=random.randint(0,total_cupboards)
#print(correct_cupboard_no)

Guess=False
# Ask user input for guessed number and check if its right or not!
while (not Guess) :
    guessed_cupboard_no=int(input("Can you guess where the goblin is hiding? "))
    if guessed_cupboard_no < total_cupboards :
        if guessed_cupboard_no == correct_cupboard_no:
            print(" Well Done! You have found the goblin \n Thankyou for playing. Now get back to work! ")
            Guess =True
    else:
        print(f"Please enter hiding cupboard number less than or equal to {total_cupboards}")