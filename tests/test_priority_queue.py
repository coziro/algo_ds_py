from algo_ds_py import PriorityQueue

def test_push_pop_min_heap():
    pq = PriorityQueue()
    pq.push(10)
    pq.push(30)
    pq.push(20)
    assert pq.pop() == 10
    assert pq.pop() == 20
    assert pq.pop() == 30

def test_push_pop_max_heap():
    pq = PriorityQueue(max_heap=True)
    pq.push(10)
    pq.push(30)
    pq.push(20)
    assert pq.pop() == 30
    assert pq.pop() == 20
    assert pq.pop() == 10

def test_heapify_list():
    pq = PriorityQueue([10, 30, 20])
    assert pq.pop() == 10
    assert pq.pop() == 20
    assert pq.pop() == 30

def test_size():
    pq = PriorityQueue()
    assert pq.size() == 0
    pq.push(10)
    assert pq.size() == 1
    pq.pop()
    assert pq.size() == 0