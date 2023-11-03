import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from algo_ds_py import PriorityQueue  # noqa: E402

print('---- min_heap ----')
pq = PriorityQueue()
pq.push(10)
pq.push(30)
pq.push(20)
print(pq.pop())
print(pq.pop())
print(pq.pop())

print('---- max_heap ----')
pq = PriorityQueue(max_heap=True)
pq.push(10)
pq.push(30)
pq.push(20)
print(pq.pop())
print(pq.pop())
print(pq.pop())

print('---- heapify ----')
pq = PriorityQueue([10, 30, 20])
print(pq.pop())
print(pq.pop())
print(pq.pop())
