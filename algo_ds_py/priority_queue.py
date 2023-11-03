import heapq

class PriorityQueue:

    def __init__(self, heap=None, max_heap=False):
        if heap is None:
            heap = []
        self.max_heap = max_heap
        if self.max_heap:
            heap = [-x for x in heap]
        self.heap = heap
        heapq.heapify(self.heap)

    def push(self, item):
        if self.max_heap:
            item = -item
        heapq.heappush(self.heap, item)

    def pop(self):
        item = heapq.heappop(self.heap)
        if self.max_heap:
            item = -item
        return item

    def size(self):
        return len(self.heap)

    def get_heap(self):
        if self.max_heap:
            return [-x for x in self.heap]
        else:
            return self.heap
