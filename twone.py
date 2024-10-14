import random


line1 = '__ OPPONENT\'S HAND __'
line2 = '____ YOUR HAND ____'
line4 = '________________'
line3 = 'MAKE YOUR CHOICE'


def twenty_one():

    opponent_hand = random.randrange(2, 21)
    your_hand = random.randrange(2, 21)

    print(f'{line1} \n ______ {opponent_hand} ______')
    print(f'\n \n \n \n{line2} \n ______ {your_hand} ______')
    print(f'{line4}')

    while True:
        print(line3)
        print('1: Stay')
        print('2: Draw')
        print('3: Quit')
        player_choice = input()

        if player_choice == '1':

            while opponent_hand < 17:
                opponent_hand += random.randrange(1, 11)
            break

        elif player_choice == '2':

            your_hand += random.randrange(1, 11)
            print(f'{line1} \n ______ {opponent_hand} ______')
            print(f'\n \n \n \n{line2} \n ______ {your_hand} ______')
            if your_hand > 21:
                print('You went over 21! You lose!')
                return  # Game ends if player goes over 21
        else:
            print("Invalid choice! Please choose 1 or 2.")



    print(f'\nFinal Hands:')
    print(f'{line1} \n ______ {opponent_hand} ______')
    print(f'{line2} \n ______ {your_hand} ______')


    if your_hand > 21:
        print('You went over 21! You lose!')
    elif opponent_hand > 21:
        print('Opponent went over 21! You win!')
    elif your_hand > opponent_hand:
        print('You win!')
    elif your_hand == opponent_hand:
        print('It\'s a draw!')
    else:
        print('You lose!')
    return



