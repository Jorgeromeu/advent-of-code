from collections import defaultdict, Counter
from dataclasses import dataclass

@dataclass
class Graph:
    neighbors: defaultdict

    def __init__(self, file_path):
        self.neighbors = defaultdict(lambda: [])

        lines = [s.strip() for s in open(file_path).readlines()]
        for line in lines:
            s, t = line.split('-')
            self.neighbors[s].append(t)
            self.neighbors[t].append(s)

def has_small_cave_been_visited_twice(path):
    for node, count in Counter(path).items():
        if node[0].islower() and count >= 2:
            return True
    return False

if __name__ == "__main__":

    graph = Graph('input.txt')

    # keep list of all valid paths
    all_paths = []

    # keep queue of paths
    queue = [['start']]

    # do bfs
    while queue:

        path = queue.pop()
        last = path[-1]

        if last == 'end':
            all_paths.append(path)

        for neighbor in graph.neighbors[last]:

            # add the neighbor to the path
            newpath = path + [neighbor]

            # large cave, always visitable
            if neighbor[0].isupper():
                queue.append(newpath)

            # start end end caves, can only be visited once
            elif neighbor in ['start', 'end'] and neighbor not in path:
                queue.append(newpath)

            # small caves
            else:

                # if a small cave has already been visited twice:
                if has_small_cave_been_visited_twice(path):
                    if neighbor not in path:
                        queue.append(newpath)

                # small case has not been visited twice
                else:
                    queue.append(newpath)

    for path in sorted(all_paths, key=lambda p: len(p)):
        print(path)

    print(len(all_paths))
