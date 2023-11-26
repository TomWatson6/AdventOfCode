
def find_paths(nodes, current_node, current_path, extra_small_visited):
    if current_node == "end":
        output = [x for x in current_path]
        output.append(current_node)
        
        return 1
    else:
        num_paths = 0
        next = nodes[current_node]
        to_explore = []
        for n in next:
            if n.isupper() or n not in current_path:
                to_explore.append(n)
            elif not extra_small_visited and n not in ["start", "end"]:
                to_explore.append(n)
        if len(to_explore) == 0:
            return 0
        else:
            previous_nodes = [x for x in current_path]
            previous_nodes.append(current_node)
            for n in to_explore:
                if n in current_path and n.islower():
                    num_paths += find_paths(nodes, n, previous_nodes, True)
                else:
                    num_paths += find_paths(nodes, n, previous_nodes, extra_small_visited)
            return num_paths


def p1(output):
    print("Part 1:", output)

def p2(output):
    print("Part 2:", output)

with open("input.txt") as f:
    nodes_list = [x.strip().split("-") for x in f.readlines()]

nodes = dict()

for node in nodes_list:
    start, end = node

    if nodes.get(start) is not None:
        nodes[start].append(end)
    else:
        nodes[start] = [end]

    if nodes.get(end) is not None:
        nodes[end].append(start)
    else:
        nodes[end] = [start]

paths = find_paths(nodes, "start", [], True)
p1(paths)

paths = find_paths(nodes, "start", [], False)

p2(paths)