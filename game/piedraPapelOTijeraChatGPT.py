import random

options = ['piedra', 'papel', 'tijera']
user_wins = 0
computer_wins = 0

while user_wins < 2 and computer_wins < 2:
    user_option = input('piedra, papel o tijera => ').lower()
    computer_option = random.choice(options)

    if user_option == computer_option:
        print('Empate!')
    elif (user_option == 'piedra' and computer_option == 'tijera') or \
         (user_option == 'papel' and computer_option == 'piedra') or \
         (user_option == 'tijera' and computer_option == 'papel'):
        print(f'User gana! {user_option} vence a {computer_option}')
        user_wins += 1
    else:
        print(f'Computer gana! {computer_option} vence a {user_option}')
        computer_wins += 1

    print(f'Puntaje: User {user_wins} - {computer_wins} Computer')

print('El ganador es la computadora' if computer_wins > user_wins else 'El ganador es el usuario')
