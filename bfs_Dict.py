from bfs import bfs_travesal, predicate_finder
from abc import ABC

class DictRootedGraph(RootedGraph):
    def __init__(self, data, roots):
        self._data = data
        self._roots = roots
    
    def roots(self):
        return self._roots
    
    def neighbors(self, n):
        return self._data[n]

def pred(n, opaque):
    if n == 4:
        opaque[0] = True
    else:
        opaque[0] = False
    return opaque[0]

graph_data = {
    1: [2, 3],
    2: [3, 4, 1],
    3: [3],
    4: []
}
roots = [1, 3, 1]

graph = DictRootedGraph(graph_data, roots)
print(bfs_travesal(graph, pred, [False]))