# In this project, we will look at how you can emulate a player throwing a set of dice. Then we
# will look at how you can store these dice in a pile the player wants to keep. you write a game where
# you throw dice to determine the outcome, this is one way to store the results for later use. example,
# normal dice with six eyes. The program will work no matter how many eyes your dice have.

import random
print('-'*125)
print(('DICE ROLL').center(125))
print('-'*125)
ls = []
print(('Welcome to our Dice Roll Program').center(125),('So Basically what you will have to do is just press V to roll the dice and we will show your roll history').center(125),('To end the game just press Q').center(125),sep='\n')
while (input().upper())!='Q':
    c = random.randint(1,6)
    print(c)
    ls.append(c)
    print('The History of guesses till now')
    print(*ls)
