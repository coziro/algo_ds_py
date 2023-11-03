from algo_ds_py import PriorityQueue


def test_push_pop_min_heap():
    pq = PriorityQueue()
    pq.push(10)
    pq.push(30)
    pq.push(20)
    assert pq.peek() == 10
    assert pq.pop() == 10
    assert pq.pop() == 20
    assert pq.pop() == 30

def test_push_pop_max_heap():
    pq = PriorityQueue(max_heap=True)
    pq.push(10)
    pq.push(30)
    pq.push(20)
    assert pq.peek() == 30
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
    pq.push(1.6)
    pq.push(1.4)
    assert pq.peek() == 1.2
    assert pq.pop() == 1.2
    assert pq.pop() == 1.4
    assert pq.pop() == 1.6

def test_float_max_heap():
    pq = PriorityQueue(max_heap=True)
    pq.push(1.2)
    pq.push(1.6)
    pq.push(1.4)
    assert pq.peek() == 1.6
    assert pq.pop() == 1.6
    assert pq.pop() == 1.4
    assert pq.pop() == 1.2

def test_tuple_min_heap():
    pq = PriorityQueue()
    pq.push((10, 'apple'))
    pq.push((30, 'banana'))
    pq.push((20, 'cherry'))
    assert pq.peek() == (10, 'apple')
    assert pq.pop() == (10, 'apple')
    assert pq.pop() == (20, 'cherry')
    assert pq.pop() == (30, 'banana')

def test_tuple_max_heap():
    pq = PriorityQueue(max_heap=True)
    pq.push((10, 'apple'))
    pq.push((30, 'banana'))
    pq.push((20, 'cherry'))
    assert pq.peek() == (30, 'banana')
    assert pq.pop() == (30, 'banana')
    assert pq.pop() == (20, 'cherry')
    assert pq.pop() == (10, 'apple')

def test_string_min_heap():
    pq = PriorityQueue()
    pq.push('apple')
    pq.push('cherry')
    pq.push('banana')
    assert pq.peek() == 'apple'
    assert pq.pop() == 'apple'
    assert pq.pop() == 'banana'
    assert pq.pop() == 'cherry'

def test_string_max_heap():
    pq = PriorityQueue(max_heap=True)
    pq.push('apple')
    pq.push('cherry')
    pq.push('banana')
    assert pq.peek() == 'cherry'
    assert pq.pop() == 'cherry'
    assert pq.pop() == 'banana'
    assert pq.pop() == 'apple'

def test_repr_min_head():
    pq = PriorityQueue([10, 20])
    assert repr(pq) == 'PriorityQueue([10, 20], max_heap=False)'

def test_repr_max_head():
    pq = PriorityQueue([10, 20], max_heap=True)
    assert repr(pq) == 'PriorityQueue([20, 10], max_heap=True)'

def test_str_min_head():
    pq = PriorityQueue([10, 20])
    assert str(pq) == 'PriorityQueue([10, 20], max_heap=False)'

def test_str_max_head():
    pq = PriorityQueue([10, 20], max_heap=True)
    assert str(pq) == 'PriorityQueue([20, 10], max_heap=True)'
