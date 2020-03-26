# Given a maze from a textfile
# Staring position is b, ending position is x, 0 are walls and 1 is a path tile
# Find the length from b to x

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3


class Search:
    maze = []
    row_num = 0
    column_num = 0
    path_num = 0

    def __init__(self, filename):
        self.read_file(filename)

    def read_file(self, filename):
        # reads maze setup from filename
        file = open(filename, 'r')
        lines = file.readlines()

        for line in lines:
            row = []
            for value in line.split(' '):
                row.append(value.strip())
            self.maze.append(row)

        # num of rows and column of maze
        self.row_num = len(self.maze)
        self.column_num = len(self.maze[0])

    def find_beginning(self):
        # finds the start of the maze
        for x in range(self.row_num):
            for y in range(self.column_num):
                if self.maze[x][y] == 'b':
                    return x, y

    def remove_impossible_moves(self, x, y, moves):
        # removes that moves that go out of bounds or hits walls
        for move in range(4):
            if not self.search_spot(x, y, move):
                moves.remove(move)

    def search_spot(self, x, y, move):
        # checks the array for what moves will be legal
        # return positions if legal else False
        if move == UP:
            x = x - 1
            if x < 0:
                return False
        elif move == DOWN:
            x = x + 1
            if x >= self.row_num:
                return False
        elif move == LEFT:
            y = y - 1
            if y < 0:
                return False
        elif move == RIGHT:
            y = y + 1
            if y >= self.column_num:
                return False

        if self.maze[x][y] == '0':
            return False

        return x, y

    def traverse(self):
        x, y = self.find_beginning()

        # after finding where to start recursion to locate x
        return self.search_path(x, y)

    def search_path(self, x, y, prev_move=None):
        # found x so we are finished
        if self.maze[x][y] == 'x':
            return True

        moves = [UP, DOWN, LEFT, RIGHT]

        # remove moves that are illegal
        self.remove_impossible_moves(x, y, moves)

        # ensures that we do not test the previous block or continuous recursion will occur
        if prev_move == UP:
            moves.remove(DOWN)
        elif prev_move == DOWN:
            moves.remove(UP)
        elif prev_move == LEFT:
            moves.remove(RIGHT)
        elif prev_move == RIGHT:
            moves.remove(LEFT)

        for move in moves:
            temp_x, temp_y = self.search_spot(x, y, move)

            # x is not a number so we need to check for that
            is_num = self.maze[temp_x][temp_y].isdigit()
            if is_num:
                self.path_num = self.path_num + int(self.maze[temp_x][temp_y])

            # continues recursion until 'x marks the stop'
            if self.search_path(temp_x, temp_y, prev_move=move):
                return True
            if is_num:
                self.path_num = self.path_num - int(self.maze[temp_x][temp_y])
        return False

    def print_path_length(self):
        print(self.path_num)


if __name__ == "__main__":
    search = Search('maze.txt')
    if search.traverse():
        search.print_path_length()
    else:
        print("No path exists")
