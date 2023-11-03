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

    def __init__(
        self,
        heap: Optional[List[Item]] = None,
        max_heap: bool = False,
    ):
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
        if self.max_heap:
            item = ReversedItem(item)
        heapq.heappush(self.heap, item)

    def pop(self) -> Item:
        item = heapq.heappop(self.heap)
        if self.max_heap:
            # Retreve original item from ReversedItem
            item = item.item
        return item

    def size(self) -> int:
        return len(self.heap)

    def get_heap(self) -> List[Item]:
        if self.max_heap:
            return [x.item for x in self.heap]
        else:
            return self.heap
