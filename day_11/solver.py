#!/usr/bin/env python

class octopus_grid:
    def __init__(self, input_grid):
        self.width  = len(input_grid[0])
        self.height = len(input_grid)
        self.contents = []
        for y in range(len(input_grid)):
            self.contents.append([])
            for x in range(len(input_grid[0])):
                self.contents[-1].append(octopus(x,y,input_grid[y][x]))

    def get_adjacent_points(self, point):
        if point.adjacent_points == None:
            adjacent_points = []
            adjacent_points_x = list(set([*range(self.width)]).intersection([point.x-1, point.x+1]))
            adjacent_points_y = list(set([*range(self.height)]).intersection([point.y-1, point.y+1]))
            #input()
            for x in adjacent_points_x:
                adjacent_points.append(self.contents[point.y][x])
            for y in adjacent_points_y:
                adjacent_points.append(self.contents[y][point.x])
            for x in adjacent_points_x:
                for y in adjacent_points_y:
                    adjacent_points.append(self.contents[y][x])
            point.adjacent_points = adjacent_points
        return point.adjacent_points

    def get_all_adjacent_points(self):
        for row in self.contents:
            for point in row:
                self.get_adjacent_points(point)

class octopus:
    def __init__(self, x, y, val):
        self.x = x
        self.y = y
        self.energy = int(val)
        self.adjacent_points = None
        self.has_flashed_this_step = False

def debug_print_grid(grid):
    for row in grid.contents:
        print(" ".join(["{:2}".format(octo.energy) for octo in row]))
    print()
    input()

def step(grid):
    flashes = 0
    previous_flashes = -1

    #print("Start:")
    #debug_print_grid(grid)

    # every octopus energy level increases by 1
    for row in grid.contents:
        for octo in row:
            octo.energy += 1
    #print("Increased by 1")
    #debug_print_grid(grid)

    # octopi with energy level > 9 flash. All surrounding octopi increase by 1 # again. Each octopus can only flash once per step. A step ends when there
    # is no octopus left to flash
    #print("Checking for flashers")
    while previous_flashes != flashes:
        previous_flashes = flashes
        for row in grid.contents:
            for octo in row:
                if octo.energy > 9 and not octo.has_flashed_this_step:
                    octo.has_flashed_this_step = True
                    flashes += 1
                    #print((octo.x, octo.y, octo.adjacent_points))
                    for pus in octo.adjacent_points:
                        pus.energy += 1
                    #debug_print_grid(grid)

    # reset flashed status
    for row in grid.contents:
        for octo in row:
            if octo.has_flashed_this_step:
                octo.energy = 0
                octo.has_flashed_this_step = False
    return flashes


if __name__ == "__main__":
    # create read the octopi into a grid
    data = open("input.txt").read().splitlines()
    ogrid = octopus_grid([list(line) for line in data])
    ogrid.get_all_adjacent_points()
    flashes_in_100_steps = 0
    steps = 0
    for i in range(100):
        flashes_in_100_steps += step(ogrid)
        steps += 1
    print(flashes_in_100_steps)
    print(steps)
    while not all([octo.energy == 0 for row in ogrid.contents for octo in row]):
        step(ogrid)
        steps += 1
    print(steps)


