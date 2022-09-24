""" It's a good idea to design a game with Python """

# temp = input('Guess the number in my mind: ')
# guess = int(temp)

# if guess == 7:
#     print('Exactly!')
#     print('But nothing for reward~')

# while guess != 7:
#     if guess > 7:
#         print('The number is too big')
#         temp = input('Guess again: ')
#         guess = int(temp)
#     else:
#         print('The number is too small')
#         temp = input('Guess again: ')
#         guess = int(temp)

import random
key = random.randint(0, 9)
counts = 3
while counts > 0:
    temp = input('Guess the number in my mind (an integer between 0 to 9): ')
    guess = int(temp)

    if guess == key:
        print('''Exactly!
But nothing for reward~ See you next time~''')
        break
    else:
        if guess > key:
            print('The number is too big')
        else:
            print('The number is too small')
        counts = counts - 1
if counts == 0:
    print('''Sorry, game over~ 
The key is ''' + str(key))
