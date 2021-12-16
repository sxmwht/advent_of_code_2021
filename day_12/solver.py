#!/usr/bin/env

class node:
    def __init__(self, name):
        self.name = name
        self.is_small = name == name.lower()
        self.linked_nodes = []

def find_path(node, visited_nodes, part):
    if node.name == "end":
        return node.name
    else:
        vc = visited_nodes.copy()
        vc.append(node)

        legal_nodes = [ln for ln in node.linked_nodes if not ln.name == "start"]

        if legal_nodes != []:
            rc = []
            vn = vc.copy()
            for ln in legal_nodes:
                if part == 1:
                    if ln.is_small and ln in vn:
                        continue
                elif part == 2:
                    if ln.is_small and ln.name != "end" and ln in vn:
                        # get all the small nodes in the list of ones we've visited
                        small_nodes = [n for n in vn if n.is_small]
                        been_to_a_small_node_twice = False
                        for sn in small_nodes:
                            if vn.count(sn) > 1:
                                been_to_a_small_node_twice = True
                                break
                        if been_to_a_small_node_twice:
                            continue

                paths = find_path(ln, vn, part)
                if type(paths) == str:
                    rc.append([node.name, paths])
                else:
                    for p in paths:
                        rc.append([node.name, *p])

            return rc
        else:
            return node.name

nodes = []
if __name__ == "__main__":
    data = open("input.txt").read().splitlines()
    for line in data:
        line_nodes = line.split('-')
        for n in line_nodes:
            if not any(existing_node.name == n for existing_node in nodes):
                nodes.append(node(n))
        for i,n in enumerate(line_nodes):
            for existing_node in nodes:
                if existing_node.name == n:
                    existing_node.linked_nodes += [node for node in nodes if node.name == line_nodes[abs(i-1)]]

#    for node in nodes:
#        print(node.name, [n.name for n in node.linked_nodes])

    print()

    # part 1
    paths = [find_path(n, [], 1) for n in nodes if n.name == "start"][0]
    print(len([p for p in paths if p[-1] == "end"]))

    # part 2
    paths = [find_path(n, [], 2) for n in nodes if n.name == "start"][0]
    print(len([p for p in paths if p[-1] == "end"]))



