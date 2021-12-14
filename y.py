import random

def show(board):
    r = ""
    for i in range(6):
        for j in board:
            for k in range(len(j)):
                if i == k:
                    if j[k] == 0:
                        r += "  "
                    elif j[k] == 1:
                        r += "X "
                    elif j[k] == -1:
                        r += "O "
        print("|"+r[:-1]+"|")
        r = ""
    print("|"+" ".join([str(i) for i in range(7)])+"|")


def top(board, row):
    index = -1
    if row < 0 or row > 6:
        return index
    for i in board[row]:
        if i != 0:
            return index
        index += 1
    return index

def play(board, row, v):
    o = top(board, row)
    if o >= 0:
        board[row][o] = v
        return True
    return False

def count(board, px, py, vx, vy, v):
    c = 0
    m = 0
    px -= vx
    py -= vy
    while px+vx in range(7) and py+vy in range(6):
        px += vx
        py += vy
        if board[px][py] == v:
            c += 1
            m = max(m, c)
        else:
            c = 0
    m = max(m, c)
    return m

def check(board, v):
    m = 0
    for i in range(7):
        c = count(board, i, 0, 0, 1, v)
        m = max(m, c)
    for i in range(6):
        c = count(board, 0, i, 1, 0, v)
        m = max(m, c)
    for i in range(7):
        c = count(board, i, 0, 1, 1, v)
        m = max(m, c)
        c = count(board, i, 0, -1, 1, v)
        m = max(m, c)
    for i in range(6):
        c = count(board, 0, i, 1, 1, v)
        m = max(m, c)
    for i in range(6):
        c = count(board, 6, i, -1, 1, v)
        m = max(m, c)
    return m

def minmax(board, v, d):
    moves = []
    for i in range(7):
        cpboard = [i[:] for i in board]
        play(cpboard, i, v)
        if check(cpboard, v) >= 4:
            moves.append(1)
        else:
            moves.append(0)
    m = max(moves)
    c = []
    for i in range(len(moves)):
        print("yes")
    return m
    
    

board = [[0 for j in range(6)] for i in range(7)]
player = 1
playing = True

while playing:
    show(board)
    p = "X"
    if player == -1:
        p = "O"
    if player == -1:
        inp = str(minmax(board, player, 1))
    else:
        inp = input(p+" > ")
    if inp.isnumeric():
        if play(board, int(inp), player):
            if check(board, player) >= 4:
                print("GAñ222222222222")
                show(board)
                playing = False
            player = -player
