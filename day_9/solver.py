#!/usr/bin/env python

class point:
    def __init__(self, x, y, val):
        self.x = x
        self.y = y
        self.val = val
        self.adjacent_points = None
    def is_minimum(self):
        return all([point.val > self.val for point in self.adjacent_points])

class grid:
    def __init__(self, input_grid):
        self.width  = len(input_grid[0])
        self.height = len(input_grid)
        self.contents = []
        for y in range(len(input_)):
            self.contents.append([])
            for x in range(len(input_[0])):
                self.contents[-1].append(point(x,y,input_grid[y][x]))

    def get_adjacent_points(self, point):
        if point.adjacent_points == None:
            adjacent_points = []
            adjacent_points_x = list(set([*range(self.width)]).intersection([point.x-1, point.x+1]))
            adjacent_points_y = list(set([*range(self.height)]).intersection([point.y-1, point.y+1]))
            for x in adjacent_points_x:
                adjacent_points.append(self.contents[point.y][x])
            for y in adjacent_points_y:
                adjacent_points.append(self.contents[y][point.x])
            point.adjacent_points = adjacent_points
        return point.adjacent_points

    def get_all_adjacent_points(self):
        for row in self.contents:
            for point in row:
                self.get_adjacent_points(point)

if __name__ == "__main__": 
    input_lines = open("input.txt").read().splitlines()
    input_ = [list(map(int, list(l))) for l in input_lines]

    grid_ = grid(input_)
    grid_.get_all_adjacent_points()

    # part 1
    print(sum([point.val+1 for row in grid_.contents for point in row if point.is_minimum()]))

    # part 2
