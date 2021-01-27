"""
TIC TAC TOE
"""
import random

def dsply_board(pos):
    """
    :param pos: pos dict to play
    :type pos: dict
    """
    i = 1
    print("\n-------------------------------------------------")
    for _ in range(3):
        for _ in range(3):
            print(f"|\t{pos[i]}\t", end='|')
            i = i + 1
        print("\n-------------------------------------------------")

def set_board(pos, postn, xo, pos_lst):
    """
    :param pos: pos dict to play
    :type pos: dict
    :param postn: position to place
    :type postn: int
    :param xo: X or O
    :type xo: str
    :param pos_lst: list of available positions
    :type pos_lst: list
    """
    pos[postn] = xo
    pos_lst.remove(postn)
    print(pos)


def check_match(pos):
    """
    :param pos: playing board
    :type pos: dict
    :return: true if game over
    :rtype: bool
    """
    matches = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 5, 9),
               (3, 5, 7), (1, 4, 7), (2, 5, 8), (3, 6, 9)]
    for i in matches:
        if pos[i[0]] == pos[i[1]] == pos[i[2]]:
            return True
    return False


def play(xo="X"):
    """
    :param xo: user char
    :type xo: str
    :return: none
    :rtype: none
    """
    pos_lst = [i for i in range(1,10)]
    pos = {i: f"{i}" for i in pos_lst}
    user_xo = xo
    cmp_xo = "O" if xo == "X" else "X"
    while True:
        dsply_board(pos)

        postn = int(input("Where would you like to place {}: ".format(user_xo)))
        if postn in pos_lst:
            set_board(pos, postn, user_xo, pos_lst)
        else:
            print("Oh oh. Did you enter a valid position? Try again.")
            continue
        if check_match(pos):
            print("CONGRATULATIONS! YOU WON!")
            break
        postn = random.choice(pos_lst)
        set_board(pos, postn, cmp_xo, pos_lst)
        if check_match(pos):
            print("OH OH! BETTER LUCK NEXT TIME.")
            break


if __name__ == "__main__":
    print("WELCOME TO TIC TAC TOE!")
    if input("ARE YOU READY TO PLAY?(Y/N)").upper() != "Y":
        print("Aww! That's too bad. Maybe next time!")
    else:
        xo = input("Would you like to be player X or O (or anything else): ").upper()
        play(xo)

