from twentyone import twenty_one
from Nummerraadspel import nummerraadspel
from rock_paper import rock_paper_scissors



def diary():
    print(f"\n""1: Read")
    print("2: Write")
    print("3: Change")
    print("5: Exit")
    choice2 = input("Enter your choice: ")
    if choice2 == "1":
        read()
    elif choice2 == "2":

        date = (input(f"\n""Enter the date(DD-MM-YYYY): "))

        with open("diary.txt", "r") as file:
            lines = file.read()

            if date in lines:
                print(f"\n"'There is already a diary for {date}. Do you want to overwrite it? Or add something? ')
                print('1: Add to text')
                print("2: Write it again")

                choice2 = input(f"\n""Enter your choice: ")

                if choice2 == "1":
                    addition = input(f"\n"'Addition to diary')
                    with open('diary.txt', "a") as file:
                        file.write(addition)
                    print(f"\n"'added successfully')
                    diary()
                elif choice2 == "2":
                    print(f"\n"'it is not working currently ;-( but u can use the change in menu files')   #im noob ;(

            if not date in lines:
                diary1 = (input("Diary: "))
                with open('diary.txt', "a") as file:
                    file.write(f'\n {date} {diary1} \n')
                    file.close()
                    diary()
    elif choice2 == "3":
        change()
    elif choice2 == "5":
        files()
    else:
        print(f"\n""Invalid choice")
        diary()
    return


def read():
    print(f"\n""1: Read All")
    print("2: Read Specific Date")
    print("5: Exit")
    choice5 = input("Enter your choice: ")

    with open("diary.txt", "r") as file:
        lines = file.read()

    if choice5 == "1":
        print("\nAll Diary Entries:")
        print(lines)

    elif choice5 == "2":
        date = input(f"\n""Enter the date (YYYY-MM-DD): ")
        if date in lines:

            sections = lines.split(date)

            print(f"\nEntry for {date}:")

            entry_sections = sections[1].split()
            entry_text = entry_sections[0]
            entry_clean = entry_text.strip()
            print(entry_clean)
        elif choice5 == "3":
            diary()
        else:
            print(f"\n""No entry found for {date}.")

    else:
        print(f"\n""Invalid choice.")
    diary()


def change():
    date = input(f"\n""Enter the date of the diary entry you want to change (DD-MM-YYYY): ")


    with open("diary.txt", "r") as file:
        lines = file.readlines()


    entry_found = False                 #THIs parts from CHAT
    for i, line in enumerate(lines):    #GPT
        if line.startswith(date):
            entry_found = True
            print(f"Current entry for {date}: {line.strip()}")
            new_entry = input(f"\n""Enter the new diary entry (or press Enter to delete this entry): ")

            if new_entry:
                lines[i] = f"{date} {new_entry}\n"
                print(f"\n""Diary entry updated successfully.")
            else:
                lines.pop(i)
                print(f"\n""Diary entry deleted successfully.")
            break

    if not entry_found:
        print(f"\n""No diary entry found for that date.")


    with open("diary.txt", "w") as file:
        file.writelines(lines)

    diary()


def to_do_list():
    print(f"\n""1: Add")
    print("2: Remove")
    print("3: Read")
    print("5: Exit ")

    choice3 = input(f"\n""Enter your choice (type exit to exit): ")
    if choice3 == "1":
        while True:
            file2 = open("list.txt", "a")
            add = input(f"\n""What are you going to add\n")
            if add == 'exit':
                print(f"\n"'Going back to menu')
                to_do_list()
                break
            file2.write(f'{add}\n')
            print(f"\n"'Task added successfully!')

    elif choice3 == "2":
        remove_todo_list()
    elif choice3 == "3":
        tasks = open("list.txt", "r")
        print(f"\n {tasks.read()}")
        tasks.close()
    elif choice3 == "5":
        files()
    else:
        print(f"\n""Invalid choice.")
        to_do_list()


def remove_todo_list():
    input(f"\n"'Which line do you want to remove?')

    with open('list.txt', 'r') as file:
        tasks = file.readlines()

    if not tasks:
        print('Your to do list is empty, you can not remove anything')
        return

    print(f"\n"'Here is your current tasks {tasks}')

    line_to_remove = int(input(f"\n"'What line do you want to remove? Enter a number'))

    if 1 <= int(line_to_remove) <= len(tasks):
        tasks.pop(line_to_remove - 1)  # bc of first object in a list fkn [0]
    with open('list.txt', 'w') as file:
        for task in tasks:
            file.write(task)
    print(f"\n"'Task removed {line_to_remove} successfully!')
    to_do_list()


def books():
    print(f"\n""1: The books I have read")
    print("2: The books I want to read")
    print('5: Exit')
    input1 = input(f"\n""Enter your choice: ")
    if input1 == "1":
        print(f"\n""1: Add a book")
        print("2: View the books")
        input2 = input(f"\n""Enter your choice: ")
        if input2 == "1":
            add_book = input(f"\n""Enter the name of the book: ")
            author = input("Enter the name of the author: ")
            points = float(input("Enter the number of points(1-10): "))
            with open('books.txt', 'a') as file:
                file.write(f"{add_book}, {author}, {points}" '\n')
                print(f"\n""Book added successfully.")
                books()
        elif input2 == "2":
                with open('books.txt', 'r') as file:
                    lines = file.readlines()
                for line in lines:
                    print(f"\n"'___ Your Books ___')
                    print(line)

        books()
    elif input1 == "2":
        print(f"\n""1: Add a book")
        print("2: View the books")
        input2 = input(f"\n""Enter your choice: ")
        if input2 == "1":
            add_book = input("Enter the name of the book: ")
            author = input("Enter the name of the author: ")
            with open('books_want_to_read.txt', 'a') as file:
                file.write(f"{add_book}, {author}" '\n')
                print(f"\n""Book added successfully.")
                books()
        elif input2 == "2":
            with open('books_want_to_read.txt', 'r') as file:
                lines = file.readlines()
            for line in lines:
                print(f"\n"'___ Your Books ___')
                print(line)
    elif input1 == "5":
        files()
    else:
        print('invalid choice.)')
        books()

def files():
    print("\n--- Files ---")
    print("1. Diary ")
    print("2. To do list")
    print("3. Books ")
    print('5: Exit')

    choice1 = input("Enter your choice: ")

    if choice1 == "1":
        diary()
    elif choice1 == "2":
        to_do_list()
    elif choice1 == "3":
        books()
    elif choice1 == '5':
        menu2()
    else:
        print(f"\n""Invalid choice. Please choose 1, 2, or 3.")
        files()


def user_exists(username):
    try:
        with open('../users.txt', 'r') as file:
            for line in file:
                stored_username, _ = line.strip().split(", ")
                if stored_username == username:
                    return True
    except FileNotFoundError:

        return False
    return False


def register_user():
    username = input("Enter a username: ")
    if user_exists(username):
        print("Username already exists. Please choose another.")
        return

    password = input("Enter a password: ")

    with open('../users.txt', 'a') as file:
        file.write(f"{username}, {password}\n")
    print("User registered successfully!")


def login_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    try:
        with open('../users.txt', 'r') as file:
            for line in file:
                stored_username, stored_password = line.strip().split(", ")
                if stored_username == username and stored_password == password:
                    print("Login successful!")
                    menu2()
                    return
    except FileNotFoundError:
        print("No users registered yet.")
        return

    print("Invalid username or password.")

def games():
    print("\n--- Games ---")
    print('1: Guess the number')
    print('2: Rock, paper, scissors, lizard and Spock')
    print('3: 21')
    print('5: Exit')

    choice1 = input("Enter your choice: ")
    if choice1 == "1":
        nummerraadspel()
        games()
    elif choice1 == "2":
        print(f'\n''___ RULES ___')
        print('Rock >>> scissors, lizard')
        print('Scissors >>> paper , lizard')
        print('paper >>> spock, rock')
        print('Spock >>> rock, scissors')
        print('lizard >>> spock, paper')
        rock_paper_scissors()
        games()
    elif choice1 == "3":
        twenty_one()
        games()
    elif choice1 == "5":
        menu2()
    else:
        print('invalid choice.)')
        games()



# Main Menu
def main():
    while True:
        print("\n--- Main Menu ---")
        print("1. Register")
        print("2. Login")
        print("5. Exit")
        choice = input(f"\n""Enter your choice: ")

        if choice == "1":
            register_user()
        elif choice == "2":
            login_user()
        elif choice == "5":
            print('Goodbye')
            break
        else:
            print(f"\n""Invalid choice. Please choose 1, 2, or 3.")


def menu2():
    print("\n--- Menu ---")
    print("1. Files")
    print("2. Games")
    print("5. Exit")
    choice3 = input(f"\n""Enter your choice: ")

    if choice3 == "1":
        files()
    elif choice3 == "5":
        main()
    elif choice3 == "2":
        games()
    else:
        print(f"\n"'Invalid choice')
        menu2()

main()

