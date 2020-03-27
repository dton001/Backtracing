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
        return self.search_path(x, y, 0)

    def search_path(self, x, y, path_length):
        # found x so we are finished, extra value needs to be removed from path_length
        if self.maze[x][y] == 'x':
            self.path_num = path_length - 1
            return True

        # order determine best to traverse maze
        moves = [RIGHT, DOWN, LEFT, UP]

        # remove moves that are illegal
        self.remove_impossible_moves(x, y, moves)

        for move in moves:
            temp_x, temp_y = self.search_spot(x, y, move)

            # spot has been visited so remove it from being revisited
            # cannot override 'x' endpoint
            if self.maze[temp_x][temp_y] is not 'x':
                self.maze[temp_x][temp_y] = '0'

            # continues recursion until 'x marks the stop'
            if self.search_path(temp_x, temp_y, path_length + 1):
                return True

            # taken path was not correct to reopen closed path
            self.maze[temp_x][temp_y] = '1'
        return False

    def print_path_length(self):
        print(self.path_num)


if __name__ == "__main__":
    search = Search('maze.txt')
    if search.traverse():
        search.print_path_length()
    else:
        print("No path exists")
