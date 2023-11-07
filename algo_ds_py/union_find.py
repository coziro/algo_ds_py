# This module is currently under development and requires additinal optimizations.

class UnionFind:
    """A union find (disjoint set) implementation."""

    def __init__(self, size):
        self.size = size
        self.root = [i for i in range(self.size)]

    def find(self, x):
        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            for i in range(self.size):
                if self.root[i] == root_y:
                    self.root[i] = root_x

