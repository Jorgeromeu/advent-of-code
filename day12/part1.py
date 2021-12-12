from collections import defaultdict
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

if __name__ == "__main__":

    graph = Graph('input.txt')

    # keep list of all valid paths
    all_paths = []

    # keep queue of paths
    queue = [['start']]

    while queue:

        path = queue.pop()
        last = path[-1]

        if last == 'end':
            all_paths.append(path)

        for neighbor in graph.neighbors[last]:
            if neighbor not in path or neighbor[0].isupper():
                newpath = path + [neighbor]
                queue.append(newpath)

    print(len(all_paths))
