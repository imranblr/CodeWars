def is_solved(board):

    if board[0][0] == board[1][1] == board[2][2] == 1: return 1
    if board[0][2] == board[1][1] == board[2][0] == 1: return 1

    if board[0][0] == board[1][1] == board[2][2] == 2: return 2
    if board[0][2] == board[1][1] == board[2][0] == 2: return 2

    def check(board, tpos):
        draw = 0
        for x, y, z in board:
            if x == 0 and x == y and  x == z : return -1
            elif x == 1 and x == y and y == z : return 1
            elif x == 2 and x == y and y == z : return 2
            elif x is 0 or y is 0 or z is 0: draw = 1
            else: continue
        if draw is 0:
            return draw
        elif tpos is 1:
            return -1

    if check(board, tpos=0):
        return check(board, tpos=0)
    else:
        board_T = []
        for j in range(len(board)):
            row = []
            for i in range(len(board[0])):
                row.append(board[i][j])
            board_T.append(row)
        return check(board_T, tpos=1)





       # print(x, y, z)

board = [[0, 0, 1],
         [0, 1, 2],
         [2, 1, 0]]
print(is_solved(board), -1)

# winning row
board = [[1, 1, 1],
         [0, 2, 2],
         [0, 0, 0]]
print(is_solved(board), 1)

# # winning column
board = [[2, 1, 2],
         [2, 1, 1],
         [1, 1, 2]]
print(is_solved(board), 1)
#
board = [[2, 1, 2],
         [2, 1, 1],
         [1, 1, 2]]
print(is_solved(board), 1)
#
# # draw
board = [[2, 1, 2],
         [2, 1, 1],
         [1, 2, 1]]
print(is_solved(board), 0)