# Rock Paper Scissor:
# try to solve with pseudocode:
#  a) Player vs. computer.
#  b) An interface with options.
#  c) Checking the player against the computer.
#  d) Returning the winner status.
#  e) Ask if the player wants to play again.

# code-

import random
name = input("Enter your Name: ")
print('Hello! '+name+' lets start the Game.')
print('Entered choice must be in lowercase')
while True:
    ls = ['rock', 'paper', 'scissor']
    guess = input("Enter your choice: ")
    choice = random.choice(ls)
    if (choice == guess):
        print('You Win')
    if (choice != guess):
        print("You lose")
    print('Press enter to exit game or Any other key from keyboard to play more!')
    play = input("Enter your choice: ")
    if (play == ""):
        print('You have exited the game')
        break
    else:
        print('Play new game!')
