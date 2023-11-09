# This module is currently under development and requires additinal optimizations.

class UnionFind:
    """A union find (disjoint set) implementation.

    Attributes:
        parent (List[int]): Parent node of each node.
        rank (List[int]): Rank (depth) of earch node.
    """

    def __init__(self, size):
        self.size = size
        self.parent = [i for i in range(self.size)]
        self.rank = [1] * self.size

    def find(self, x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)
