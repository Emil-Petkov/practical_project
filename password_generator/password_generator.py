import random

rock = 'Rock'
scissors = 'Scissors'
paper = 'Paper'

print()
player_move = input('Choose [r]ock, [s]cissors or [p]aper: ')
print()

if player_move == 'r':
    player_move = rock
elif player_move == 's':
    player_move = scissors
elif player_move == 'p':
    player_move = paper
else:
    raise SystemExit('Invalid Input. Try again...')

computer_random_number = random.randint(1, 3)

computer_move = ''

if computer_random_number == 1:
    computer_move = rock
elif computer_random_number == 2:
    computer_move = scissors
elif computer_random_number == 3:
    computer_move = paper

print(f'The computer choose {computer_move}.')

if (player_move == rock and computer_move == scissors) or \
        (player_move == scissors and computer_move == paper) or \
        (player_move == paper and computer_move == rock):
    print('You win!')
elif player_move == computer_move:
    print('Draw!')
else:
    print('You lose!')