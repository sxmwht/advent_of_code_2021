#!/usr/bin/env

class node:
    def __init__(self, name):
        self.name = name
        self.is_small = name == name.lower()
        self.linked_nodes = []

def find_path(node, source_node, visited_nodes):
    if node.name == "end":
        return node.name
    else:
        vc = visited_nodes.copy()
        vc.append(node)

        legal_nodes = [ln for ln in node.linked_nodes if not(ln.is_small and ln in vc)]

        if legal_nodes != []:
            rc = []
            vn = vc.copy()
            for ln in legal_nodes:
                paths = find_path(ln, node, vn)
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

    for node in nodes:
        print(node.name, [n.name for n in node.linked_nodes])

    print()
    print()

    paths = [find_path(n, None, []) for n in nodes if n.name == "start"][0]
    for p in [",".join(p) for p in paths if p[-1] == "end"]:
        print(p)
    print(len([p for p in paths if p[-1] == "end"]))


