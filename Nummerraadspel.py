import random

def nummerraadspel():
    line1 = 'Throw the dices'
    line2 = 'Pick a number between 2 and 13'
    line3 = ''
    print(line1)
    print(line3)


    random_number = random.randrange(2, 13)

    attempts = 3
    success = False

    while attempts > 0:
        guess = int(input(line2))

        if guess == random_number:
            print('You got it right!')
            success = True
            break  # Exit the loop if the guess is correct
        else:
            print('You got it wrong!')
            attempts -= 1
            print(f'You have {attempts} guesses left.')

    if not success:
        print(f'Sorry, you are out of guesses. The correct number was {random_number}.')
