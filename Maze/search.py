# Given a maze from a textfile
# Staring position is b, ending position is x, 0 are walls and 1 is a path tile
# Find the length from b to x

import sys

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3


class Search:
    maze = []
    row_num = 0
    column_num = 0
    path_num = sys.maxsize

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

    def print_maze(self, maze):
        for row in maze:
            for value in row:
                print(value, end=' ')
            print()

    def find_beginning(self):
        # finds the start of the maze
        for x in range(self.row_num):
            for y in range(self.column_num):
                if self.maze[x][y] == 'b':
                    return x, y

    def remove_impossible_moves(self, maze, x, y, moves):
        # removes that moves that go out of bounds or hits walls
        for move in range(4):
            if not self.search_spot(maze, x, y, move):
                moves.remove(move)

    def search_spot(self, maze, x, y, move):
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

        if maze[x][y] == '0':
            return False

        return x, y

    def traverse(self):
        found_path = False
        x, y = self.find_beginning()

        # order determine best to traverse maze
        # avoid having two opposing directions next to each other
        set_of_moves = [
            [RIGHT, DOWN, LEFT, UP], [RIGHT, UP, LEFT, DOWN], [DOWN, RIGHT, UP, LEFT],
            [LEFT, DOWN, RIGHT, UP], [LEFT, UP, RIGHT, DOWN], [UP, RIGHT, DOWN, LEFT],
            [DOWN, LEFT, UP, RIGHT], [UP, LEFT, DOWN, RIGHT]
        ]

        # test each set priority moves
        for moves in set_of_moves:

            # make a hard copy of the puzzle for repeat testing
            temp_maze = []
            for row in self.maze:
                temp_row = []
                for value in row:
                    temp_row.append(value)
                temp_maze.append(temp_row)

            # main path finding function
            found_path = self.search_path(temp_maze, x, y, 0, moves)
        return found_path

    def search_path(self, maze, x, y, path_length, set_of_moves):
        # hard copy of set of moves to continue testing this set of direction
        moves = []
        for move in set_of_moves:
            moves.append(move)

        # remove moves that are illegal
        self.remove_impossible_moves(maze, x, y, moves)

        for move in moves:
            temp_x, temp_y = self.search_spot(maze, x, y, move)

            # found x so we are finished, extra value needs to be removed from path_length
            if maze[temp_x][temp_y] == 'x':
                # keep track of shortest path length
                if self.path_num > path_length:
                    self.path_num = path_length
                return True

            # spot has been visited so remove it from being revisited
            maze[temp_x][temp_y] = '0'

            # continues recursion until 'x marks the stop'
            if self.search_path(maze, temp_x, temp_y, path_length + 1, set_of_moves):
                return True

            # taken path was not correct so reopen closed path
            maze[temp_x][temp_y] = '1'
        return False

    def print_path_length(self):
        print(self.path_num)


if __name__ == "__main__":
    search = Search('maze.txt')
    if search.traverse():
        search.print_path_length()
    else:
        print("No path exists")
