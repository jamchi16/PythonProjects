import random

def guess(x):
    low = 1
    high = x
    feedback = ' '
    while feedback != 'C':
        guess = random.randint(low, high)
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?')
        if feedback == 'H':
            high = guess - 1
        elif feedback == 'L':
            low = guess + 1
    print ('The computer got it!')

guess(100)




