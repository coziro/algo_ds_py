from collections import defaultdict
from typing import List


class UnionFind:
    """A union find (disjoint set) implementation.

    Attributes:
        size (int): The total number of nodes.
        parent (List[int]): A list holding the index of the parent node for each node.
        rank (List[int]): A list holding the rank (the height of the tree) for each node.
    """

    def __init__(self, size: int):
        """Initializes the UnionFind instance.

        Args:
            size (int): The total number of nodes.
        """
        self.size = size
        self.parent = [i for i in range(self.size)]
        self.rank = [1] * self.size

    def find(self, x: int) -> int:
        """Finds the roor node of node x.

        Uses path compression to improve search efficiency.

        Args:
            x (int): Traget node.

        Returns:
            The index of the root node.
        """
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int):
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

    def same(self, x: int, y: int) -> bool:
        """Determines whether two nodes belong to the samge group.

        Args:
            x (int): The first node to check.
            y (int): The second node to check.

        Returns:
            True if the nodes are in the same group, False othewise.
        """
        return self.find(x) == self.find(y)

    def roots(self) -> List[int]:
        """Return a list of all root nodes.

        Returns:
            A list of all root nodes.
        """
        root_list = []
        for i in range(self.size):
            if self.parent[i] == i:
                root_list.append(i)
        return root_list

    def group_count(self) -> int:
        """Return a number of groups.

        Returns:
            Number of groups.
        """
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for n in range(self.size):
            group_members[self.find(n)].append(n)
        return group_members


