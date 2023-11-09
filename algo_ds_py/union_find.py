class UnionFind:
    """A union find (disjoint set) implementation.

    Attributes:
        size (int): The total number of nodes.
        parent (List[int]): A list holding the index of the parent node for each node.
        rank (List[int]): A list holding the rank (the height of the tree) for each node.
    """

    def __init__(self, size):
        """Initializes the UnionFind instance.

        Args:
            size (int): The total number of nodes.
        """
        self.size = size
        self.parent = [i for i in range(self.size)]
        self.rank = [1] * self.size

    def find(self, x):
        """Finds the roor node of node x.

        Uses path compression to improve search efficiency.

        Args:
            x (int): Traget node.
        """
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """Unites two nodes x and y into the same group.

        Uses union by rank to improve the efficiency.

        Args:
            x (int): The first node to unite.
            y (int): The second node to unite.
        """
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
        """Determines whether two nodes belong to the samge group.

        Args:
            x (int): The first node to check.
            y (int): The second node to check.
        """
        return self.find(x) == self.find(y)
