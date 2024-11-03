import random

available = [i for i in range(1, 26)]

# SETTNGS
REMOVED_NUMBER = "█" # "֍"  "•"  "Ø"   



def create_board():
    # create a 2D board to play

    # 1. create an array of 1-25 numbers : nums
    # 2. create a 2D array, initialize it with 0s : board
    # 3. iterate below steps 25 times (2 for loops 5x5)
    #  3.1. randomly select one number from nums : x
    #  3.2. put it in board
    #  3.3. remove the x from the nums so that we don't select same number again
    # 4. return board : a 2D array contains randomly placed numbers from 1-25 without repetition

    nums = [i for i in range(1, 26)]
    board = [[0 for _ in range(5)] for _ in range(5)]

    for i in range(5):
        for j in range(5):
            x = random.choice(nums)
            board[i][j] = x
            nums.remove(x)

    return board



def find_key_mark(b1, b2, key):
    # marking number selected by players in both tables
    for i in range(5):
        for j in range(5):
            if b1[i][j] == key:
                b1[i][j] = REMOVED_NUMBER

            if b2[i][j] == key:
                b2[i][j] = REMOVED_NUMBER




def ask_computer(computer_b):
    # ask computer for a number to mark

    # ------------------------------------------------------
    # 1.EASY (select a random number from available numbers)

    # x = random.choice(available)
    # available.remove(x)
    # return x
    # ------------------------------------------------------

    # 2.MEDIUM (calculate a score for every element return best number)

    """
    ============================================================================
    WE TRY TO RETURN THE BEST POSSIBLE NUMBER/MOVE FROM THE GIVEN BOARD.

    1. if middle number is not marked :

       return number in the middle(computer_b[2][2]) of the board
       as 'first move' to improve chances.

    2. if middle number is already marked :

       we check if any row/column contains 4 "█"(or REMOVED_NUMBER)
       if yes return the 5th number
       eg :-
        ["█",3,"█","█","█"]  --> return 3

    3. if middle number is already marked and there is no row/column
       contains 4 "█"(or REMOVED_NUMBER) :

       we calculate a score for every number in the board
       and return the number with high score

       eg:-
       given board =
        [
            [1, "█", "█", 4, 5],
            [6, "█", "█", "█", 10],
            [11, 12, 13, 14, "█"],
            [16, 17, 18, 19, "█"],
            [21, 22, 23, 24, "█"],
        ]

        here 10 is best option,
        [
            [  ,   ,    ,    , 5  ],
            [6 ,"█", "█", "█", 10 ],
            [  ,   ,    ,    , "█"],
            [  ,   ,    ,    , "█"],
            [  ,   ,    ,    , "█"],
        ]

        no. of "█"(or REMOVED_NUMBER) in the row of 10 = 3
        no. of "█"(or REMOVED_NUMBER) in the col of 10 = 3

        Total no. of "█"(or REMOVED_NUMBER) corresponding 10 = 3+3 = 6
        Total no. of number spaces corresponding 10 = 9
          --> [6 ,"█", "█", "█", 10 ] row corresponding 10
          --> [5 , 10, "█", "█", "█"] column corresponding 10
          --> total 9 number spaces(number 10 exist in both row and col)

        score calculation for number 10 = 6/9 = 0.6666666666666666
        (this score is the best when comparing with the score of other numbers)
    ============================================================================
    """

    # -------------------------------------
    def score(x, p, q):
        # score calculation for computer
        count = 0
        for k in range(5):
            if x[k][q] == REMOVED_NUMBER:
                count += 1
            if x[p][k] == REMOVED_NUMBER:
                count += 1
        return count / 9

    # -------------------------------------

    # cross the middle element as first move to improve chances
    if computer_b[2][2] in available:
        return computer_b[2][2]

    else:

        # 1.check for any rows/cols have 4 "█"(or REMOVED_NUMBER) if yes select the 5th number
        y = [[computer_b[j][i] for j in range(5)] for i in range(5)]

        for i in range(5):
            if (computer_b[i].count(REMOVED_NUMBER)) == 4:
                for j in range(5):
                    if computer_b[i][j] != REMOVED_NUMBER:
                        return computer_b[i][j]

            if (y[i].count(REMOVED_NUMBER)) == 4:
                for j in range(5):
                    if y[i][j] != REMOVED_NUMBER:
                        return y[i][j]

        # 2.if there is no row which have 4 "█"(or REMOVED_NUMBER)
        # we will return best number by calculating the high_score
        high_score = -1
        best = -1

        for i in range(5):
            for j in range(5):

                if computer_b[i][j] == REMOVED_NUMBER:
                    continue

                temp = score(computer_b, i, j)

                if temp >= high_score:
                    high_score = temp
                    best = computer_b[i][j]

        # print(high_score, best)

        return best


def check_bingo(b):
    # if every element in the row/column == REMOVED NUMBER: increment count

    count = 0
    # row
    for i in range(5):
        if all([spot == REMOVED_NUMBER for spot in b[i]]):
            # print("row")
            count += 1

    # column
    column = [[b[i][j] for i in range(5)] for j in range(5)]
    for i in range(5):
        if all([spot == REMOVED_NUMBER for spot in column[i]]):
            # print("column")
            count += 1

    # # diagonals (not considered in bingo at my school :))

    diagonal1 = [b[i][i] for i in range(5)]
    if all([spot == REMOVED_NUMBER for spot in diagonal1]):
        # print("dia1")
        count += 1

    diagonal2 = [b[i][5 - i - 1] for i in range(5)]
    if all([spot == REMOVED_NUMBER for spot in diagonal2]):
        # print("dia2")
        count += 1

    return count

