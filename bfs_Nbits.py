from bfs import bfs_travesal, predicate_finder
from abc import ABC

class Nbits(RootedGraph):
    def __init__(self, roots, N):
        self._roots = roots
        self._n = N
        
    def roots(self):
        return self._roots

    def neighbors(self, S):
        neighborsList = []
        for i in range(self._n):
            neighborsList.append(S^(1<<i))
        return neighborsList

print(predicate_finder(Nbits([1], 4), lambda n: n == 16))