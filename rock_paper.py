import random

def rock_paper_scissors():
    list = ['rock', 'paper', 'scissors', 'lizard', 'spock']
    random_item = random.choice(list)
    
    choice = input('Make your choice')


    if choice == 'rock':
        if random_item == 'rock':
            print('AGAINN!')
            rock_paper_scissors()
        elif random_item == 'paper':
            print('YOU LOSE')
        elif random_item == 'scissors':
            print('YOU WIN!')
        elif random_item == 'lizard':
            print('YOU WIN!')
        elif random_item == 'spock':
            print('YOU LOSE!')
            
    elif choice == 'paper':
        if random_item == 'rock':
            print('YOU WIN!')
        elif random_item == 'scissors':
            print('YOU LOSE!')
        elif random_item == 'lizard':
            print('YOU LOSE!')
        elif random_item == 'spock':
            print('YOU WIN!')
        elif random_item == 'paper':
            print('AGAINN!')
            rock_paper_scissors()
    
    elif choice == 'scissors':
        if random_item == 'rock':
            print('YOU LOSE!')
        elif random_item == 'paper':
            print('YOU WIN!')
        elif random_item == 'lizard':
            print('YOU WIN!')
        elif random_item == 'spock':
            print('YOU LOSE!')
        elif random_item == 'scissors':
            print('AGAINN!')
            rock_paper_scissors()
        
    elif choice == 'spock':
        if random_item == 'rock':
            print('YOU WIN!')
        elif random_item == 'paper':
            print('YOU LOSE!')
        elif random_item == 'lizard':
            print('YOU LOSE!')
        elif random_item == 'scissors':
            print('YOU WIN!')
        elif random_item == 'spock':
            print('AGAINN!')
            rock_paper_scissors()
    
    elif choice == 'lizard':
        if random_item == 'rock':
            print('YOU LOSE!')
        elif random_item == 'paper':
            print('YOU WIN!')
        elif random_item == 'scissors':
            print('YOU LOSE!')
        elif random_item == 'spock':
            print('YOU WIN!')
        elif random_item == 'lizard':
            print('AGAINN!')
            rock_paper_scissors()
    