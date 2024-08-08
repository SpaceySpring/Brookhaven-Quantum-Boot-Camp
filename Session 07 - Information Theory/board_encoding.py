import numpy as np


def check_winner(b, j, x):
    s = False
    if s is False:
        for i in range(0, 3):
            z = b[i]  # row search 0 to 2
            if sum(z) == j and i == 0:
                s = True
                print(
                    f"{j} is {[
                [x,x,x],
                [0,0,0],
                [0,0,0],
            ]}",
                    end=", ",
                )
                print(f"Player {x} Wins!!")
                return s
            elif sum(z) == j and i == 1:
                s = True
                print(
                    f"{j} is {[
                [0,0,0],
                [x,x,x],
                [0,0,0],
            ]}",
                    end=", ",
                )
                print(f"Player {x} Wins!!")
                return s
            elif sum(z) == j and i == 2:
                s = True
                print(
                    f"{j} is {[
                [0,0,0],
                [0,0,0],
                [x,x,x],
            ]}",
                    end=", ",
                )
                print(f"Player {x} Wins!!")
                return s
            else:
                continue
        for i in range(0, 3):
            w = [row[i] for row in b]  # column search 0 to 5
            if sum(w) == j and i == 0:
                s = True
                print(
                    f"{j} is {[
                [x,0,0],
                [x,0,0],
                [x,0,0],
            ]}",
                    end=", ",
                )
                print(f"Player {x} Wins!!")
                return s
            elif sum(w) == j and i == 1:
                s = True
                print(
                    f"{j} is {[
                [0,x,0],
                [0,x,0],
                [0,x,0],
            ]}",
                    end=", ",
                )
                print(f"Player {x} Wins!!")
                return s
            elif sum(w) == j and i == 2:
                s = True
                print(
                    f"{j} is {[
                [0,0,x],
                [0,0,x],
                [0,0,x],
            ]}",
                    end=", ",
                )
                print(f"Player {x} Wins!!")
                return s
            else:
                continue
        y = np.diagonal(
            b
        )  # -2 to 3 scans diagonally from second row 0 to the first row column four
        if sum(y) == j:
            s = True
            print(
                f"{j} is {[
                [x,0,0],
                [0,x,0],
                [0,0,x],
            ]}",
                end=",",
            )
            print(f"Player {x} Wins!!")
            return s
        else:
            u = np.fliplr(b).diagonal()  # Flip the board over the y axis
            if sum(u) == j:
                s = True
                print(
                    f"{j} is {[
                    [0,0,x],
                    [0,x,0],
                    [x,0,0],
                ]}",
                    end=", ",
                )
                print(f"Player {x} Wins!!")
                return s
            else:
                return False


y = [2271, 1638, 12065]
for i in y:
    x = 1
    b = [
        [x * (3) ** 0, x * (3) ** 1, x * (3) ** 2],
        [x * (3) ** 3, x * (3) ** 4, x * (3) ** 5],
        [x * (3) ** 6, x * (3) ** 7, x * (3) ** 8],
    ]
    ck = check_winner(b, i, x)
    if ck is False:
        x = 2
        b = [
            [x * (3) ** 0, x * (3) ** 1, x * (3) ** 2],
            [x * (3) ** 3, x * (3) ** 4, x * (3) ** 5],
            [x * (3) ** 6, x * (3) ** 7, x * (3) ** 8],
        ]
        ck = check_winner(b, i, x)
        if ck is False:
            print(
                f"{i} is {[
                            [1,2,2],
                            [2,1,1],
                            [2,1,2],
                        ]}",
                end=", ",
            )
            print("No Winner")
