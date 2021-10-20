class Connect4():

    def __init__(self):
        self.player_due = 1
        self.result = None
        self.matrix = []
        for j in range(0, 6):
            r = []
            for i in range(0, 7):
                r.append(0)
            self.matrix.append(r)

    def tpos(self, board):
        board_T = []
        for j in range(len(board) + 1):
            rw = []
            for i in range(len(board[-1]) - 1):
                rw.append(board[i][j])
            board_T.append(rw)
        return board_T

    def check(self, board, trans=False):
        cl = len(board[0])
        rl = len(board)
        # print(board)
        for i in range(0, rl):
            for j in range(0, cl):
                # print(board[i][j])
                if not trans:
                    if i <= 2 and j <= 3:
                        # print(board[i][j], )
                        # print("Horizontal ->", board[i][j], board[i][j+1], board[i][j+2], board[i][j+3])
                        # print("Veritical ->", board[i][j], board[i+1][j], board[i+2][j], board[i+3][j])
                        # print("top down Across ->", board[i][j], board[i + 1][j + 1], board[i + 2][j + 2], board[i + 3][j + 3])
                        # print("bottom up Across ->", board[rl-i-1][j], board[rl-i-2][j+1], board[rl-i-3][j+2], board[rl-i-4][j+3])
                        if board[i][j] == board[i][j + 1] == board[i][j + 2] == board[i][j + 3] == 1: return "Player 1 wins!"
                        elif board[i][j] == board[i+1][j] == board[i+2][j] == board[i+3][j] == 1 : return "Player 1 wins!"
                        elif board[i][j] == board[i + 1][j + 1] == board[i + 2][j + 2] == board[i + 3][j + 3] == 1: return "Player 1 wins!"
                        elif board[rl-i-1][j] == board[rl-i-2][j+1] == board[rl-i-3][j+2] == board[rl-i-4][j+3]== 1: return "Player 1 wins!"
                        elif board[i][cl-j-1] == board[i+1][cl-j-2] == board[i+2][cl-j-3] == board[i+3][cl-j-4] == 1: return "Player 1 wins!"
                        elif board[i][j] == board[i][j + 1] == board[i][j + 2] == board[i][j + 3] == 2: return "Player 2 wins!"
                        elif board[i][j] == board[i+1][j] == board[i+2][j] == board[i+3][j] == 2 : return "Player 2 wins!"
                        elif board[i][j] == board[i + 1][j + 1] == board[i + 2][j + 2] == board[i + 3][j + 3] == 2: return "Player 2 wins!"
                        elif board[rl-i-1][j] == board[rl-i-2][j+1] == board[rl-i-3][j+2] == board[rl-i-4][j+3] == 2: return "Player 2 wins!"
                        elif board[i][cl-j-1] == board[i+1][cl-j-2] == board[i+2][cl-j-3] ==  board[i+3][cl-j-4] == 1 : return "Player 2 wins!"


                else:
                    if i <= 3 and j <= 2:
                        if board[i][j] == board[i][j + 1] == board[i][j + 2] == board[i][j + 3] == 1: return "Player 1 wins!"
                        elif board[i][j] == board[i + 1][j] == board[i + 2][j] == board[i + 3][j] == 1 : return "Player 1 wins!"
                        elif board[i][j] == board[i][j + 1] == board[i][j + 2] == board[i][j + 3] == 2: return "Player 2 wins!"
                        elif board[i][j] == board[i + 1][j] == board[i + 2][j] == board[i + 3][j] == 2: return "Player 2 wins!"

        return None

    def check_across(self, board):
        cl = len(board[0])
        rl = len(board)
        for i in range(0, rl):
            for j in range(0, cl):
                if i <= 2 and j <=3:
                    # print(board[i][j], board[i+1][j+1], board[i+2][j+2], board[i+3][j+3])
                    if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3] == 1: return "Player 1 wins!"
                    elif board[rl-i-1][cl-j-1] == board[rl-i-2][cl-j-2]  == board[rl-i-3][cl-j-3] == board[rl-i-4][cl-j-4] == 1: return "Player 1 wins!"
                    elif board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3] == 2: return "Player 2 wins!"
                    elif board[rl-i-1][cl-j-1] == board[rl-i-2][cl-j-2]  == board[rl-i-3][cl-j-3] == board[rl-i-4][cl-j-4] == 2: return "Player 2 wins!"
        return None

    def play(self, col):
        if self.result is not None: return "Game has finished!"
        self.played = False
        self.player = self.player_due
        for x in range(0, 6):
            if self.matrix[x][col] == 0:
                if self.player == 1:
                    self.matrix[x][col] = 1
                    self.played = True
                    self.player_due = 2
                    self.result = self.check(self.matrix)
                    if self.result is not None: return self.result
                    # self.result = self.check(self.tpos(self.matrix), True)
                    # if self.result is not None: return self.result
                    # self.result = self.check_across(self.matrix)
                    # if self.result is not None: return self.result
                    else: return "Player 1 has a turn"
                else:
                    self.matrix[x][col] = 2
                    self.played = True
                    self.player_due = 1
                    self.result = self.check(self.matrix)
                    if self.result is not None: return self.result
                    # self.result = self.check(self.tpos(self.matrix), True)
                    # if self.result is not None: return self.result
                    # self.result = self.check_across(self.matrix)
                    # if self.result is not None: return self.result
                    else: return "Player 2 has a turn"
        if self.played is False: return "Column full!"

        # print(self.matrix)




        # if (col >= 0 or col < 6) and (self.row >= 0 or self.row < 5):
            # if self.matrix[self.rw][col] == 0:
            #     if self.player == 1:
            #         self.matrix[self.rw][col] = 1
            #         self.player = 2
            #         self.check(self.matrix, self.c1, self.c2)
            #         print("\n Player 1 has a turn")
            #
            #
            #     else:
            #         self.matrix[self.rw][col] = 2
            #         self.player = 1
            #         self.check(self.matrix, self.c1, self.c2)
            #         print("\n Player 2 has a turn")
            #     if self.rw < 5: self.rw += 1
            # else: print("Column full!")

        # print(self.matrix)
game = Connect4()
print(game.play(0), "Player 1 has a turn")
print(game.play(1), "Player 2 has a turn")
print(game.play(1), "Player 1 has a turn")
print(game.play(2), "Player 2 has a turn")
print(game.play(2), "Player 1 has a turn")
print(game.play(3), "Player 2 has a turn")
print(game.play(2), "Player 1 has a turn")
print(game.play(3), "Player 2 has a turn")
print(game.play(4), "Player 1 has a turn")
print(game.play(3), "Player 2 has a turn")
print(game.play(3), "Player 1 wins!")

# game = Connect4()
# print(game.play(0), "Player 1 has a turn")
# print(game.play(1), "Player 2 has a turn")
# print(game.play(2), "Player 1 has a turn")
# print(game.play(4), "Player 2 has a turn")
# print(game.play(3), "Player 1 has a turn")
# print(game.play(2), "Player 2 has a turn")
# print(game.play(3), "Player 1 has a turn")
# print(game.play(3), "Player 2 has a turn")
# print(game.play(3), "Player 1 has a turn")
# print(game.play(4), "Player 2 has a turn")
# print(game.play(4), "Player 1 has a turn")
# print(game.play(4), "Player 2 wins!")
#
# game = Connect4()
# print(game.play(0), "Player 1 has a turn")
# print(game.play(0), "Player 2 has a turn")
# print(game.play(1), "Player 1 has a turn")
# print(game.play(1), "Player 2 has a turn")
# print(game.play(2), "Player 1 has a turn")
# print(game.play(2), "Player 2 has a turn")
# print(game.play(3), "Player 1 wins!")
#
#
# game = Connect4()
#
# print(game.play(0), "Player 1 has a turn")
# print(game.play(0), "Player 2 has a turn")
#
# game = Connect4()
# print(game.play(0), "Player 1 has a turn")
# print(game.play(1), "Player 2 has a turn")
# print(game.play(0), "Player 1 has a turn")
# print(game.play(1), "Player 2 has a turn")
# print(game.play(0), "Player 1 has a turn")
# print(game.play(1), "Player 2 has a turn")
# print(game.play(0), "Player 1 wins!")
#
# game = Connect4()
# print(game.play(4), "Player 1 has a turn")
# print(game.play(4), "Player 2 has a turn")
# print(game.play(4), "Player 1 has a turn")
# print(game.play(4), "Player 2 has a turn")
# print(game.play(4), "Player 1 has a turn")
# print(game.play(4), "Player 2 has a turn")
# print(game.play(3), "Player 1 has a turn")
# print(game.play(4), "Column full!")
# print(game.play(3), "Player 2 has a turn")
#
# game = Connect4()
# print(game.play(1), "Player 1 has a turn")
# print(game.play(1), "Player 2 has a turn")
# print(game.play(2), "Player 1 has a turn")
# print(game.play(2), "Player 2 has a turn")
# print(game.play(3), "Player 1 has a turn")
# print(game.play(3), "Player 2 has a turn")
# print(game.play(4), "Player 1 wins!")
# print(game.play(4), "Game has finished!")