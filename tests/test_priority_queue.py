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
    pq = PriorityQueue(heap=[10, 30, 20])
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

def test_get_heap_min_heap():
    pq = PriorityQueue(heap=[10, 30, 20])
    assert pq.get_heap() == [10, 20, 30] or pq.get_heap() == [10, 30, 20]

def test_get_heap_max_heap():
    pq = PriorityQueue(heap=[10, 30, 20], max_heap=True)
    assert pq.get_heap() == [30, 20, 10] or pq.get_heap() == [30, 10, 20]

def test_float_min_heap():
    pq = PriorityQueue()
    pq.push(1.2)
    pq.push(3.6)
    pq.push(2.4)
    assert pq.pop() == 1.2
    assert pq.pop() == 2.4
    assert pq.pop() == 3.6

def test_string_min_heap():
    pq = PriorityQueue()
    pq.push('apple')
    pq.push('cherry')
    pq.push('banana')
    assert pq.pop() == 'apple'
    assert pq.pop() == 'banana'
    assert pq.pop() == 'cherry'

def test_tuple_min_heap():
    pq = PriorityQueue()
    pq.push((10, 'apple'))
    pq.push((30, 'banana'))
    pq.push((20, 'cherry'))
    assert pq.pop() == (10, 'apple')
    assert pq.pop() == (20, 'cherry')
    assert pq.pop() == (30, 'banana')
