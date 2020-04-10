# Given a maze from a textfile
# Staring position is b, ending position is x, 0 are walls and 1 is a path tile
# Find the length from b to x

import sys

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3


class Node:
    def __init__(self, index=None, parent=None):
        self.index = index
        self.parent = parent

        # distance from start node
        self.g = 0
        # distance from start node + distance from end node
        self.f = 0


class Search:
    maze = []
    row_num = 0
    column_num = 0
    open_spots = []
    closed_spots = []
    path = []

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

    def find_points(self, start_end):
        # find start and end points
        for i in range(self.row_num):
            for j in range(self.column_num):
                c = 'b' if start_end is 'begin' else 'x'
                if self.maze[i][j] is c:
                    return i, j

    def smallest_distance(self):
        # returns node with lowest f cost in open list
        distance = sys.maxsize
        smallest = None
        for spot in self.open_spots:
            if distance > spot.f:
                smallest = spot
                distance = spot.f
        return smallest

    def find_neighbors(self, curr, neighbors):
        # looks all neighbors to current node
        for i in range(4):
            self.confirm_neighbor(curr, i, neighbors)

    def confirm_neighbor(self, curr, move, neighbors):
        # helper function to confirm neighbor is appropriate
        x = curr.index[0]
        y = curr.index[1]
        if move is UP:
            x = x + 1
        elif move is DOWN:
            x = x - 1
        elif move is LEFT:
            y = y - 1
        elif move is RIGHT:
            y = y + 1

        # if values are negative or go out of bounds
        if (x < 0 or x >= self.row_num) or (y < 0 or y >= self.column_num):
            return

        # if index is a wall
        if self.maze[x][y] is '0':
            return

        new_node = Node((x, y), curr)

        # see if node is in closed list
        if self.index(self.closed_spots, new_node):
            return

        # index is valid and not in closed list so add it to neighbor list
        neighbors.append(new_node)

    def calc_distance(self, n1, n2):
        # find distance between two nodes
        return abs(n1.index[0] - n2.index[0]) + abs(n1.index[1] - n2.index[1])

    def index(self, list, item):
        # check the values in item and return that item if it has a match
        for l in list:
            if l.index == item.index:
                return l
        return False

    def traverse(self):
        # find start and end points
        start_node = Node(self.find_points('begin'))
        end_node = Node(self.find_points('end'))

        # start node is appended to open list starting the loop
        self.open_spots.append(start_node)

        while len(self.open_spots) != 0:
            # find node with smallest f cost
            curr = self.smallest_distance()

            # remove that node from open list and add it to closed list
            self.open_spots.remove(curr)
            self.closed_spots.append(curr)
            neighbors = []

            if curr.index == end_node.index:
                # we found the end point
                current = curr

                # construct the list
                while current.parent:
                    self.path.append(current.index)
                    current = current.parent
                self.path = self.path[::-1]
                return True
            else:
                # we are not at the end, so we look for neighbors
                self.find_neighbors(curr, neighbors)

            for n in neighbors:
                # update current neighbor distance from start
                n.g = curr.g + 1

                # update current neighbor distance from start + distance from end
                n.f = n.g + self.calc_distance(n, end_node)

                # see if node is already in open list
                index = self.index(self.open_spots, n)
                if index:
                    if n.f > index.f:
                        # if node in open list but has higher f cost then ignore current neighbor
                        continue

                # neighbor either is not in open list or has a shorter f cost we add neighbor
                self.open_spots.append(n)

    def print_path(self):
        for p in self.path:
            print(p)
        print(len(self.path))


if __name__ == "__main__":
    search = Search('maze.txt')
    if search.traverse():
        search.print_path()
    else:
        print("No path exists")
