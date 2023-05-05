import random

def guess(x):
    randnum = random.randint(1, 100)
    guess = 0
    while guess != randnum:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < randnum:
            print('Too low!')
        elif guess > randnum:
            print('Too high!')

    print('Spot on!')
guess(100)