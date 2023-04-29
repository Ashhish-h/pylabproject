# Guess the number:
# In this game, the computer will guess a random number and the player will try to guess what
# number it is. The game ends when the player manages to guess the number. Display the appropriate
# score also.

Code-
import random
number=random.randint(1,100) 
name=input("Hi! What is your name\n")
print('Okay '+name+ " Lets Start!")
Count=0 #count number of guesses
while(number):
       guess=int(input("Guess the number between 1 and 100!\n"))
       if (guess<number):
              count+=1
              print("Too low!")

       elif(guess>number):
              count+=1
              print("Too high!")
    
       elif (guess==number):
             count+=1
             break
if(guess==number):
       print("You guessed the number in "+str(count)+ " trials!")
