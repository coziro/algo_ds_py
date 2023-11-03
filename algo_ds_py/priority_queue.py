import heapq
from typing import Any, List, Optional

Item = Any  # int, float, string, tuple, etc.

class PriorityQueue:

    def __init__(
        self,
        heap: Optional[List[Item]] = None,
        max_heap: bool = False,
    ):
        if heap is None:
            self.heap = []
        else:
            self.heap = heap.copy()

        self.max_heap = max_heap
        if self.max_heap:
            self.heap = [-x for x in self.heap]

        heapq.heapify(self.heap)

    def push(self, item: Item):
        if self.max_heap:
            item = -item
        heapq.heappush(self.heap, item)

    def pop(self) -> Item:
        item = heapq.heappop(self.heap)
        if self.max_heap:
            item = -item
        return item

    def size(self) -> int:
        return len(self.heap)

    def get_heap(self) -> List[Item]:
        if self.max_heap:
            return [-x for x in self.heap]
        else:
            return self.heap
