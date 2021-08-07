#FUNCTIONS
def display_intro():
    print("Welcome to Tic-tac-toe v1")
    print("Developed by: Jemuel Bryan Vergara\n")

def initialize_list_input():
    global list_input
    list_input = []
    for num in range(1,10):
        list_input.append(str(num))

def start_game():
    ans = 'N'
    while ans != 'Y':
        ans = input("Start (Y or N): ")
        if ans == 'N':
            print("Bye!")
            quit()
        elif ans != 'Y':
            print("Invalid Input!")

def clear_board():
    global r1, r2, r3 
    r1 = [' ',' ',' ']
    r2 = [' ',' ',' ']
    r3 = [' ',' ',' ']

def player_names():
    global p1, p2
    print("\nPlease enter your name")
    p1 = input("Player 1: ")
    p2 = input("Player 2: ")
    print(f'\nWelcome {p1} and {p2}!\n')
    print(f'{p1} is X')
    print(f'{p2} is O')

def display_board(row1, row2, row3):
    print(f'\n     {row1[0]} | {row1[1]} | {row1[2]}')
    print('     ---------')
    print(f'     {row2[0]} | {row2[1]} | {row2[2]}')
    print('     ---------')
    print(f'     {row3[0]} | {row3[1]} | {row3[2]}\n')

def update_board(ans, px):
    global r1,r2,r3

    if px == 1:
        letter = 'X'
    if px == 2:
        letter = 'O'

    if ans in range(1,4):
        r3[ans-1] = letter
    
    if ans in range(4,7):
        r2[ans-4] = letter

    if ans in range(7,10):
        r1[ans-7] = letter

def display_keypad():
    print('\n      KEYPAD')
    print('     7 | 8 | 9')
    print('     ---------')
    print('     4 | 5 | 6')
    print('     ---------')
    print('     1 | 2 | 3\n')

def accept_input(px):
    global list_input
    def clean_update(ans,px):
        list_input.remove(ans)
        ans = int(ans)
        update_board(ans, px)

    if px == 1:
        ans = input(f'{p1} - Enter a number (1-9): ')
        while not ans.isdigit() or ans not in list_input:
            print('Invalid input!')
            ans = input(f'{p1} - Enter a number (1-9): ')
        clean_update(ans,px)
    if px == 2:
        ans = input(f'{p2} - Enter a number (1-9): ')
        while not ans.isdigit() or ans not in list_input:
            print('Invalid input!')
            ans = input(f'{p2} - Enter a number (1-9): ')
        clean_update(ans,px)

def check_winner():
    global r1,r2,r3
    rows = [r1,r2,r3]
    columns = zip(r3,r2,r1)
    columns = list(columns)
    columns = [list(columns[0]), list(columns[1]), list(columns[2])]
    d1 = [r3[0],r2[1],r1[2]]
    d2 = [r3[2],r2[1],r1[0]]
    diagonals = [d1,d2]

    def check(rcd):
        for entry in rcd:
            if len(set(entry)) == 1:
                if entry[0] == 'X':
                    declare_winner(1)
                if entry[0] == 'O':
                    declare_winner(2)
                else:
                    pass

    check(rows)
    check(columns)
    check(diagonals)

def declare_winner(px):
    if px == 1:
        print(f'Congratulations, {p1}!\n')
        play_again()
    if px == 2:
        print(f'Congratulations, {p2}!\n')
        play_again()

def play_again():
    ans = 'N'
    while ans != 'Y':
        ans = input("Play again? (Y or N): ")
        if ans == 'N':
            print("Bye!")
            quit()
        elif ans != 'Y':
            print("Invalid Input!")
    main()


def disp_check_key():
    display_board(r1,r2,r3)
    check_winner()
    display_keypad()

def main():
    display_keypad()
    initialize_list_input()
    clear_board()
    ctr = 1
    while True:
        if ctr%2 != 0:
            accept_input(1)
            disp_check_key()
        
        if ctr%2 == 0:
            accept_input(2)
            disp_check_key()

        ctr += 1


display_intro()
start_game()
player_names()
main()

