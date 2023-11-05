import heapq
from typing import Any, List, Optional

Item = Any  # int, float, string, tuple, etc.


class ReversedItem:

    def __init__(self, item: Item):
        self.item = item

    def __lt__(self, other: 'ReversedItem') -> bool:
        return self.item > other.item

    def __eq__(self, other: 'ReversedItem') -> bool:
        return self.item == other.item

    def __repr__(self) -> str:
        return repr(self.item)


class PriorityQueue:
    """A priority queue implementation using a heap.

    Attributes:
        heap (List): The underlying heap data structure.
        mex_heap (bool): True for a max-heap, False for a min-heap (default).

    Methods:
        push(item): Inserts an item into the priority queue.
        pop(): Remove and returns the highest priority item.
        peek(): Returns the highest priotiy item without removing it.
        size(): Returns the number of items in the priority queue.
        get_heap(): Returns a copy of the item in the heap.
    """

    def __init__(
        self,
        heap: Optional[List[Item]] = None,
        max_heap: bool = False,
    ):
        """Initializes the priority queue.

        Args:
            heap (List, optional): An initial list of items to populate the priority queue.
            max_heap (bool, optional): True for a max-heap, False for a min-heap (default).
        """
        self.max_heap = max_heap
        if heap is None:
            self.heap = []
        else:
            if self.max_heap:
                self.heap = [ReversedItem(x) for x in heap]
            else:
                self.heap = heap.copy()
        heapq.heapify(self.heap)

    def push(self, item: Item):
        """Inserts an item into the priority queue.

        Args:
            item (Any): The item to be inserted into the priority queue.
        """
        if self.max_heap:
            item = ReversedItem(item)
        heapq.heappush(self.heap, item)

    def pop(self) -> Item:
        """Remove and returns the highest priority item.

        Returns:
            The highest priority item in the priority queue.
        """
        item = heapq.heappop(self.heap)
        if self.max_heap:
            # Retrieve original item from ReversedItem
            item = item.item
        return item

    def peek(self) -> Item:
        """Returns the highest priority item without removing it.

        Returns:
            The highest priority item in the priority queue.
        """
        item = self.heap[0]
        if self.max_heap:
            # Retrieve original item from ReversedItem
            item = item.item
        return item

    def size(self) -> int:
        """Returns the number of items in the priority queue.

        Returns:
            The number of items in the priority queue.
        """
        return len(self.heap)

    def get_heap(self) -> List[Item]:
        """Returns a copy of the heap.

        Returns:
            a copy of the heap.
        """
        if self.max_heap:
            return [x.item for x in self.heap]
        else:
            return self.heap

    def __repr__(self) -> str:
        if self.max_heap:
            items = [x.item for x in self.heap]
        else:
            items = self.heap
        return f'PriorityQueue({items}, max_heap={self.max_heap})'

    def __str__(self) -> str:
        return self.__repr__()
