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
    visited_spots = []

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

        # if self.maze[x][y] == '0':
        if (x, y) in self.visited_spots or self.maze[x][y] == '0':
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
            self.visited_spots.clear()
            self.visited_spots.append((x, y))

            # main path finding function
            found_path = self.search_path(x, y, 0, moves)
        return found_path

    def search_path(self, x, y, path_length, set_of_moves):
        # hard copy of set of moves to continue testing this set of direction
        moves = []
        for move in set_of_moves:
            moves.append(move)

        # remove moves that are illegal
        self.remove_impossible_moves(x, y, moves)

        for move in moves:
            temp_x, temp_y = self.search_spot(x, y, move)

            # found x so we are finished, extra value needs to be removed from path_length
            if self.maze[temp_x][temp_y] == 'x':
                # keep track of shortest path length
                if self.path_num > path_length:
                    self.path_num = path_length
                return True

            # add spot to visited spot array
            self.visited_spots.append((temp_x, temp_y))

            # continues recursion until 'x marks the stop'
            if self.search_path(temp_x, temp_y, path_length + 1, set_of_moves):
                return True

            # taken path was not correct so remove visited spot from array
            self.visited_spots.remove((temp_x, temp_y))
        return False

    def print_path_length(self):
        print(self.path_num)


if __name__ == "__main__":
    search = Search('maze.txt')
    if search.traverse():
        search.print_path_length()
    else:
        print("No path exists")
