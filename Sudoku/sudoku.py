class Sudoku:
    puzzle = None

    def __init__(self, file_name):
        self.puzzle = self.read_file(file_name)

    def read_file(self, file_name):
        file = open(file_name, 'r')
        lines = file.readlines()
        grid = []

        for line in lines:
            row = []
            for num in line.split(' '):
                row.append(int(num))
            grid.append(row)
        return grid

    def remove_row_values(self, arr, x):
        # remove elements that appear in the row
        for i in range(9):
            num = self.puzzle[x][i]
            if num in arr:
                arr.remove(num)

    def remove_column_values(self, arr, y):
        # remove elements that appear in the column
        for i in range(9):
            num = self.puzzle[i][y]
            if num in arr:
                arr.remove(num)

    def remove_box_values(self, arr, x, y):
        # remove elements that appear in the 3x3
        x_start, x_end = self.box_range(x)
        y_start, y_end = self.box_range(y)

        for i in range(x_start, x_end):
            for j in range(y_start, y_end):
                num = self.puzzle[i][j]
                if num in arr:
                    arr.remove(num)

    def box_range(self, num):
        # return the start and stop for box
        for i in range(4):
            if i * 3 <= num < (i + 1) * 3:
                return i * 3, (i + 1) * 3

    def print_grid(self):
        for row in self.puzzle:
            for value in row:
                print(value, end=' ')
            print()

    def next_unassigned(self, index):
        # looks for the next unassigned spot
        for i in range(9):
            for j in range(9):
                if self.puzzle[i][j] == 0:
                    # index get the position of the unassigned spot
                    index[0] = i
                    index[1] = j
                    return True
        return False

    def solve_puzzle(self):
        index = [0, 0]
        if not self.next_unassigned(index):
            # if all spots are assigned then we are complete
            return True

        # values were obtained from next_unassigned
        x = index[0]
        y = index[1]

        # array of all possible values
        possible_values = [x for x in range(1, 10)]

        # removing values that are already used
        self.remove_row_values(possible_values, x)
        self.remove_column_values(possible_values, y)
        self.remove_box_values(possible_values, x, y)

        for value in possible_values:
            # attempt value in unassigned spot
            self.puzzle[x][y] = value

            # calls func again until all spots are assigned properly
            if self.solve_puzzle():
                return True

            # attempted value breaks future assignments, assign spot to empty value
            self.puzzle[x][y] = 0

        # list of possible values does not follow rule, previous assignment will be undone
        return False


if __name__ == "__main__":
    solve = Sudoku('puzzle.txt')
    if solve.solve_puzzle():
        solve.print_grid()
    else:
        print("No solution")
