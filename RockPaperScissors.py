import random

def play():
    user = input("Please play Rock (R), Paper (P), or Scissors (S): ")
    cpu = random.choice(['R', 'P', 'S'])
    if user == cpu:
        return 'Tie!'
    if win(user, cpu):
        return 'You won!'
    return 'You Lost!'

def win(player, opponent):
    if (player == 'R' and opponent == 'S') or (player == 'S' and opponent == 'P') or (player == 'P' and opponent == 'R'):
        return True

print (play())


