# Game
from click import option


game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def game_board():
    print("   0, 1, 2")
    i = 0
    for row in game:
        print(i, row)
        i = i + 1


# Win


def win_game(z):

    e = [x, y]
    c = 0
    for g in range(2):
        if c > 1:
            c = c - 2
        break
    z = z * 1

    options = {
        0: game[0][0] == game[0][1] == game[0][2] != 0,
        1: game[1][0] == game[1][1] == game[1][2] != 0,
        2: game[2][0] == game[2][1] == game[2][2] != 0,
        3: game[0][0] == game[1][0] == game[2][0] != 0,
        4: game[0][1] == game[1][1] == game[2][1] != 0,
        5: game[0][2] == game[1][2] == game[2][2] != 0,
        6: game[0][0] == game[1][1] == game[2][2] != 0,
        7: game[2][0] == game[1][1] == game[0][2] != 0,
    }

    if list(options.values())[0]:
        print(f"Congratulations {e[c]}!\nYou have won the Game")
        return z * 2
    elif list(options.values())[1]:
        print(f"Congratulations {e[c]}!\nYou have won the Game")
        return z * 2
    elif list(options.values())[2]:
        print(f"Congratulations {e[c]}!\nYou have won the Game")
        return z * 2
    elif list(options.values())[3]:
        print(f"Congratulations {e[c]}!\nYou have won the Game")
        return z * 2
    elif list(options.values())[4]:
        print(f"Congratulations {e[c]}!\nYou have won the Game")
        return z * 2
    elif list(options.values())[5]:
        print(f"Congratulations {e[c]}!\nYou have won the Game")
        return z * 2
    elif list(options.values())[6]:
        print(f"Congratulations {e[c]}!\nYou have won the Game")
        return z * 2
    elif list(options.values())[7]:
        print(f"Congratulations {e[c]}!\nYou have won the Game")
        return z * 2

    else:
        if (
            game[0][0] != 0
            and game[0][1] != 0
            and game[0][2] != 0
            and game[1][0] != 0
            and game[1][1] != 0
            and game[1][2] != 0
            and game[2][0] != 0
            and game[2][1] != 0
            and game[2][2] != 0
        ):
            print("Game Tie")
        else:
            pass


# Greetings
print("Welcome to Number based Tic Tac Toe\n")

rules = """Rules to play the game:
1) The game is played on a grid that's 3 squares(0) by 3 squares(0).
2) You are 1, your friend is 2. Players take turns putting their marks in empty squares(0).
3) The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.
4) When all 9 squares are full, the game is over.\n\n"""
print(rules)

# Playing Game
f = [2, 1]
d = 0
c = 0

m = int(input("To play the game enter '0':\n"))
if m == 0:
    for g in range(2):
        if c > 1:
            c = c - 2
            break
    while d != 10:
        x = input("Player 1\nEnter your name:\n")
        x = x.upper()

        y = input("Player 2\nEnter your name:\n")
        y = y.upper()

        e = [x, y]

        game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        game_board()
        d = 0
        win = False
        while not win:
            for i in range(2):
                if d > 1:
                    d = d - 2
                print(f"\n{e[d]}'s Turn:\n")
                d = d + 1
                if d == 2:
                    d = d - 2
                break

            a = int(input("In which row you wanna play:\n"))
            if a > 2:
                print("the value cannot exceed 2\nPlease try again")
            b = int(input("In which column you wanna play:\n"))
            if b > 2:
                print("the value cannot exceed 2\nPlease try again")

            if game[a][b] != 0:
                print("This position is already chosen\nYour Turn has been skipped\n")

            else:
                game[a][b] = f[d]
            game_board()
            p = win_game(1)
            if p == 2:
                break
            c = c + 1
        u = int(input("\n\nDo you want to play again? [Yes(0)/No(1)]\n"))
        if u == 1:
            print("Thank You for Playing")
            break
