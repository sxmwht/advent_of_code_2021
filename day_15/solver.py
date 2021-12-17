#!/usr/bin/env python

import heapq

class area:
    def __init__(self, x, y, val):
        self.x               = x
        self.y               = y
        self.risk            = int(val)
        self.shortest_path   = float('inf')
        self.adjacent_points = None
        self.visited         = False

class cave_map:
    def __init__(self, input_grid):
        self.width  = len(input_grid[0])
        self.height = len(input_grid)
        self.contents = []
        for y in range(len(input_grid)):
            self.contents.append([])
            for x in range(len(input_grid[0])):
                self.contents[-1].append(area(x,y,input_grid[y][x]))
        self.contents[0][0].shortest_path = 0

    def get_adjacent_points(self, point):
        if point.adjacent_points == None:
            adjacent_points = []
            adjacent_points_x = list(set([*range(self.width)]).intersection([point.x-1, point.x+1]))
            adjacent_points_y = list(set([*range(self.height)]).intersection([point.y-1, point.y+1]))
            # horizontal
            for x in adjacent_points_x:
                adjacent_points.append(self.contents[point.y][x])
            # vertical
            for y in adjacent_points_y:
                adjacent_points.append(self.contents[y][point.x])
            ## diagonal
            #for x in adjacent_points_x:
            #    for y in adjacent_points_y:
            #        adjacent_points.append(self.contents[y][x])
            point.adjacent_points = adjacent_points
            #point.adjacent_points.sort(key = lambda x: x.risk)
        return point.adjacent_points

    def get_all_adjacent_points(self):
        for row in self.contents:
            for point in row:
                self.get_adjacent_points(point)

def djikstra(grid, initial_node, end_node):
    q = []
    heapq.heappush(q, (initial_node.shortest_path, hash(initial_node), initial_node))
    while not end_node.visited:
        _n, _h, smallest_node = heapq.heappop(q)
        for n in grid.get_adjacent_points(smallest_node):
            if n.visited == False:
                new_dist = smallest_node.shortest_path + n.risk
                if new_dist < n.shortest_path:
                    n.shortest_path = new_dist
                    heapq.heappush(q, (new_dist,  hash(n), n))
        smallest_node.visited = True
    return end_node.shortest_path


if __name__ == "__main__":
    input_data = [list(map(int, list(l))) for l in open("input.txt").read().splitlines()]
    cm = cave_map(input_data)

    print(djikstra(cm, cm.contents[0][0], cm.contents[-1][-1]))

    large_map = []
    for y in range(5):

        for row in input_data:
            new_row = []
            for x in range(5):
                new_row.append([i+x-(9*int(i+x>9)) for i in row])
            new_row = [i+y-(9*int(i+y>9)) for r in new_row for i in r]
            large_map.append(new_row)

    #for i in range(len(large_map[-1])):
    #    large_map[-1][i]= 0
    #for i in range(len(large_map)):
    #    large_map[i][0] = 0

    cm = cave_map(large_map)

    print(djikstra(cm, cm.contents[0][0], cm.contents[-1][-1]))
