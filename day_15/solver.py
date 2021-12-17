#!/usr/bin/env python

import heapq
from time import time

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
            x= point.x
            y= point.y
            n = set()
            if y < self.height-1:
                n.add(self.contents[y+1][x])
            if y > 0:
                n.add(self.contents[y-1][x])
            if x > 0:
                n.add(self.contents[y][x-1])
            if x < self.width-1:
                n.add(self.contents[y][x+1])
            point.adjacent_points = n
        return point.adjacent_points

    def get_all_adjacent_points(self):
        for row in self.contents:
            for point in row:
                self.get_adjacent_points(point)

def djikstra(grid, initial_node, end_node):
    q = []
    heapq.heappush(q, (initial_node.shortest_path, (initial_node.x, initial_node.y), initial_node))
    while heapq:
        mindist, _h, smallest_node = heapq.heappop(q)
        if smallest_node.visited:
            continue
        if smallest_node == end_node:
            print("Exiting")
            return end_node.shortest_path
        smallest_node.visited = True
        for n in grid.get_adjacent_points(smallest_node):
            if n.visited:
                continue
            new_dist = mindist + n.risk
            if new_dist < n.shortest_path:
                n.shortest_path = new_dist
                heapq.heappush(q, (new_dist,  (n.x, n.y), n))
    return end_node.shortest_path

def get_neighbours(x, y, w, h):
    n = set()
    if y < h:
        n.add((x, y+1))
    if y > 0:
        n.add((x, y-1))
    if x > 0:
        n.add((x-1, y))
    if x < w:
        n.add((x+1, y))
    return n


def djikstra2(grid):
    q = []
    visited = set()
    source = (0,0)
    w = len(grid[0])-1
    h = len(grid)-1
    dest = (w,h)

    min_dist = []
    for i in range(h+1):
        min_dist.append([float('inf')]*(w+1))

    heapq.heappush(q, (0, source))
    while heapq:
        dist, c = heapq.heappop(q)

        if c == dest:
            return min_dist[dest[1]][dest[0]]

        if c in visited:
            continue

        visited.add(c)
        for p in get_neighbours(c[0], c[1], w, h):
            if p in visited:
                continue

            new_dist = dist + grid[p[1]][p[0]]
            if new_dist < min_dist[p[1]][p[0]]:
                min_dist[p[1]][p[0]] = new_dist
                heapq.heappush(q, (new_dist, p))
    return float('inf')

if __name__ == "__main__":
    input_data = [list(map(int, list(l))) for l in open("input.txt").read().splitlines()]
    cm = cave_map(input_data)

    t0 = time()
    print(djikstra(cm, cm.contents[0][0], cm.contents[-1][-1]))
    t1 = time()
    print(t1-t0)
    t0 = time()
    print(djikstra2(input_data))
    t1 = time()
    print(t1-t0)

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

    t0 = time()
    print(djikstra(cm, cm.contents[0][0], cm.contents[-1][-1]))
    t1 = time()
    print(t1-t0)

    
    t0 = time()
    print(djikstra2(large_map))
    t1 = time()
    print(t1-t0)

