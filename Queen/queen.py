# Given NxN grid place N queens on the board
# without them being able to attack each other
# change variable when initializing Queen class


class Queen:
    board = []
    amount = 0

    # setup empty NxN board
    def __init__(self, amount):
        self.amount = amount
        for i in range(self.amount):
            row = []
            for j in range(self.amount):
                row.append(0)
            self.board.append(row)

    def check_safe(self, x, y):
        # check no other queens in same row
        for i in range(self.amount):
            if self.board[i][y] is 1:
                return False

        # list of diagonal direction
        diagonal = [(1, 1), (-1, 1), (1, -1), (-1, -1)]

        # current diagonal direction
        for diag in diagonal:
            x2 = x
            y2 = y

            # continue traveling in direction until out of bounds
            while True:
                x2 = x2 + diag[0]
                y2 = y2 + diag[1]

                # make sure x and y are still in bounds
                if not(0 <= x2 < self.amount and 0 <= y2 < self.amount):
                    break

                # if queen in current diagonal is found
                if self.board[x2][y2] is 1:
                    return False

        # no queen found in row and all found diagonal directions
        return True

    def unique_queen(self):
        # calls main recursion function
        return self.queen_rec(0)

    def queen_rec(self, column):
        # when number of queen equal column number, we have placed all the queens
        if self.amount is column:
            return True

        # get a list of possible spot for queens
        possible_spots = []
        for i in range(self.amount):
            if self.check_safe(column, i):
                possible_spots.append([column, i])

        for x, y in possible_spots:
            # place queen at current spot
            self.board[x][y] = 1

            # see if this placement works with future placements
            if self.queen_rec(x+1):
                return True

            # future placements did not work so remove queen from spot
            self.board[x][y] = 0
        return False

    def print_board(self):
        for row in self.board:
            for value in row:
                print(value, end=' ')
            print()


if __name__ == "__main__":
    queen = Queen(7)
    if queen.unique_queen():
        queen.print_board()
    else:
        print("Cannot be done")
