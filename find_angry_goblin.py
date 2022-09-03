# To create a small game through programming
print(" Welcome To The Angry Goblin Hunt\n")
print('An Award Winning Game " Full Of Fun and Adventure "\n')
# Ask user to neter his/her name
name=input(" What is your name \n")
print(f" Welcome to the Game {name} !")
# Display the message to the user
print(f" {name}, Do you think you can find the Goblin hiding in the cupboard ? \n |_| |_| |_| |_| |_| ")
# To store the hiding cupboard number in a variable
correct_cupboard_no = 3
Guess=False
# Ask user input for guessed number and check if its right or not!
while (not Guess):
    guessed_cupboard_no=int(input("Can you guess where the goblin is hiding? "))
    if guessed_cupboard_no == correct_cupboard_no:
        print(" Well Done! You have found the goblin \n Thankyou for playing. Now get back to work! ")
        Guess =True
    else:
        print(" No,Sorry! The goblin is still hiding somewhere. ")