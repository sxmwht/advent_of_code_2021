#!/usr/bin/env

class node:
    def __init__(self, name):
        self.name = name
        self.is_small = name == name.lower()
        self.linked_nodes = []

def find_path(node, source_node, visited_nodes):
    print(node.name, [f.name for f in node.linked_nodes])
    visited_nodes.append(node)
    print(node.name)
    if source_node != None:
        print(source_node.name)
    else:
        print("START")

    legal_nodes = [ln for ln in node.linked_nodes if ln != source_node and not(ln.is_small and ln in visited_nodes)]
    if node.name != "end" and legal_nodes != []:
        return [[name for name in [node.name, *[new_list]]]  for ln in legal_nodes for new_list in find_path(ln,node,visited_nodes)]
    else:
        visited_nodes = []
        return [node.name]

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

    print(find_path(nodes[12], None, []))

