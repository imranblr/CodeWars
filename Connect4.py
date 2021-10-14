class Connect4():

    def __init__(self):
        self.row = 0
        self.matrix = []
        for j in range(0, 6):
            r = []
            for i in range(0, 7):
                r.append(0)
            self.matrix.append(r)
        self.rw = 0
        self.player = 1
        self.c1 = 0
        self.c2 = 0
        self.game = 0
        # self.cl = 0
    def tpos(self, board):
        board_T = []
        for j in range(len(board)+1):
            rw = []
            for i in range(len(board[-1])-1):
                rw.append(board[i][j])
            board_T.append(rw)
        return board_T

    def check(self, board, c1, c2):
        draw = 0
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                # print("Values ->", c1, c2)
                # print(board)
                if board[i][j] == 1:
                    c2 = 0
                    c1 += 1
                    # print("Values c1 ->", c1)
                    if c1 == 4 :
                        self.game = 1
                        return "Player 1 wins!"
                elif board[i][j] == 2:
                    c1 = 0
                    c2 += 1
                    # print("Values c2 ->", c2)
                    if c2 == 4:
                        self.game = 1
                        return "Player 2 wins!"
                else :
                    c1 = 0
                    c2 = 0
        return None

        # if draw is 0:
        #     return draw
        # elif tpos is 1:
        #     return -1

    def play(self, col):
        if self.game == 1 : return "Game has finished!"
        played = 0
        for x in range (0, 6):
            if self.matrix[x][col] == 0:
                if self.player == 1:
                    self.matrix[x][col] = 1
                    played = 1
                    self.player = 2
                    if self.check(self.matrix, self.c1, self.c2):
                        return self.check(self.matrix, self.c1, self.c2)
                    elif self.check(self.tpos(self.matrix), self.c1, self.c2):
                        return self.check(self.tpos(self.matrix), self.c1, self.c2)
                    else: return "Player 1 has a turn"

                else:
                    self.matrix[x][col] = 2
                    played = 1
                    self.player = 1
                    if self.check(self.matrix, self.c1, self.c2):
                        return self.check(self.matrix, self.c1, self.c2)
                    elif self.check(self.tpos(self.matrix), self.c1, self.c2):
                        return self.check(self.tpos(self.matrix), self.c1, self.c2)
                    else:
                        return "Player 2 has a turn"

        if played is 0:
            return "Column full!"
        print(self.matrix)




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
print(game.play(0), "Player 2 has a turn")
print(game.play(1), "Player 1 has a turn")
print(game.play(1), "Player 2 has a turn")
print(game.play(2), "Player 1 has a turn")
print(game.play(2), "Player 2 has a turn")
print(game.play(3), "Player 1 wins!")


game = Connect4()

print(game.play(0), "Player 1 has a turn")
print(game.play(0), "Player 2 has a turn")

game = Connect4()
print(game.play(0), "Player 1 has a turn")
print(game.play(1), "Player 2 has a turn")
print(game.play(0), "Player 1 has a turn")
print(game.play(1), "Player 2 has a turn")
print(game.play(0), "Player 1 has a turn")
print(game.play(1), "Player 2 has a turn")
print(game.play(0), "Player 1 wins!")

game = Connect4()
print(game.play(4), "Player 1 has a turn")
print(game.play(4), "Player 2 has a turn")
print(game.play(4), "Player 1 has a turn")
print(game.play(4), "Player 2 has a turn")
print(game.play(4), "Player 1 has a turn")
print(game.play(4), "Player 2 has a turn")
print(game.play(4), "Column full!")

game = Connect4()
print(game.play(1), "Player 1 has a turn")
print(game.play(1), "Player 2 has a turn")
print(game.play(2), "Player 1 has a turn")
print(game.play(2), "Player 2 has a turn")
print(game.play(3), "Player 1 has a turn")
print(game.play(3), "Player 2 has a turn")
print(game.play(4), "Player 1 wins!")
print(game.play(4), "Game has finished!")